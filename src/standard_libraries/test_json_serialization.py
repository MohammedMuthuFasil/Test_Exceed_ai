"""Extended JSON serialization/deserialization tests generated using Copilot AI.

Covers json.dumps, json.loads, custom encoders/decoders, pretty printing,
nested structures, and edge cases with class-based organization and
systematic parametrized test cases.
"""

import pytest
import json
from datetime import datetime, date
from typing import Any


class CustomEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles datetime and set objects."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, set):
            return sorted(list(obj))
        return super().default(obj)


class TestJsonDumps:
    """Verify json.dumps serialization for various Python types."""

    @pytest.mark.parametrize("python_obj, expected_json", [
        ({"key": "value"}, '{"key": "value"}'),
        ([1, 2, 3], '[1, 2, 3]'),
        (True, 'true'),
        (None, 'null'),
        (42, '42'),
        ("hello", '"hello"'),
    ], ids=["dict", "list", "bool", "none", "int", "string"])
    def test_basic_type_serialization(self, python_obj: Any, expected_json: str) -> None:
        """Standard Python types serialize to expected JSON strings."""
        assert json.dumps(python_obj) == expected_json

    def test_nested_structure(self) -> None:
        """Deeply nested dicts and lists serialize correctly."""
        data = {"users": [{"name": "Alice", "scores": [90, 85]}]}
        result = json.loads(json.dumps(data))
        assert result == data

    def test_sort_keys(self) -> None:
        """sort_keys=True produces alphabetically ordered output."""
        data = {"b": 2, "a": 1}
        result = json.dumps(data, sort_keys=True)
        assert result == '{"a": 1, "b": 2}'

    def test_indent_formatting(self) -> None:
        """indent parameter produces human-readable output with newlines."""
        data = {"x": 1}
        result = json.dumps(data, indent=2)
        assert "\n" in result
        assert "  " in result


class TestJsonLoads:
    """Verify json.loads deserialization into Python objects."""

    @pytest.mark.parametrize("json_str, expected_type", [
        ('{"a": 1}', dict),
        ('[1, 2]', list),
        ('"hello"', str),
        ('42', int),
        ('3.14', float),
        ('true', bool),
        ('null', type(None)),
    ], ids=["dict", "list", "string", "int", "float", "bool", "null"])
    def test_deserialize_types(self, json_str: str, expected_type: type) -> None:
        """JSON strings deserialize to the expected Python types."""
        result = json.loads(json_str)
        assert isinstance(result, expected_type)

    def test_invalid_json_raises(self) -> None:
        """Invalid JSON string raises json.JSONDecodeError."""
        with pytest.raises(json.JSONDecodeError):
            json.loads("{invalid json}")

    def test_empty_object(self) -> None:
        """Empty JSON object deserializes to empty dict."""
        assert json.loads("{}") == {}

    def test_empty_array(self) -> None:
        """Empty JSON array deserializes to empty list."""
        assert json.loads("[]") == []


class TestJsonRoundtrip:
    """Verify dumps/loads roundtrip preserves data integrity."""

    @pytest.mark.parametrize("data", [
        {"name": "test", "values": [1, 2, 3]},
        [{"nested": True}, {"count": 42}],
        {"empty_list": [], "empty_dict": {}, "null_val": None},
    ], ids=["dict_with_list", "list_of_dicts", "empty_values"])
    def test_roundtrip_preserves_data(self, data: Any) -> None:
        """Serializing then deserializing returns identical data."""
        assert json.loads(json.dumps(data)) == data

    def test_roundtrip_unicode(self) -> None:
        """Unicode strings survive JSON roundtrip intact."""
        data = {"emoji": "hello 🌍", "japanese": "日本語"}
        assert json.loads(json.dumps(data, ensure_ascii=False)) == data


class TestCustomEncoder:
    """Verify custom JSONEncoder handles non-standard types."""

    def test_datetime_serialized(self) -> None:
        """datetime objects serialize to ISO format string."""
        dt = datetime(2026, 4, 27, 12, 0, 0)
        result = json.dumps({"when": dt}, cls=CustomEncoder)
        parsed = json.loads(result)
        assert parsed["when"] == "2026-04-27T12:00:00"

    def test_date_serialized(self) -> None:
        """date objects serialize to ISO format string."""
        d = date(2026, 1, 15)
        result = json.dumps({"date": d}, cls=CustomEncoder)
        parsed = json.loads(result)
        assert parsed["date"] == "2026-01-15"

    def test_set_serialized_as_sorted_list(self) -> None:
        """set objects serialize as sorted lists."""
        s = {3, 1, 2}
        result = json.dumps({"items": s}, cls=CustomEncoder)
        parsed = json.loads(result)
        assert parsed["items"] == [1, 2, 3]

    def test_unhandled_type_still_raises(self) -> None:
        """Types not handled by custom encoder still raise TypeError."""
        with pytest.raises(TypeError):
            json.dumps({"obj": object()}, cls=CustomEncoder)
