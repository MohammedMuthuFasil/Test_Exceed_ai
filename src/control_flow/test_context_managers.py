"""Context manager tests generated using Copilot AI.

Covers with statement protocol (__enter__/__exit__), contextlib utilities,
custom context managers, nested contexts, and exception suppression
with class-based test organization and typed signatures.
"""

import pytest
import os
import tempfile
from contextlib import contextmanager, suppress


@contextmanager
def temp_value(container: dict, key: str, value):
    """Context manager that temporarily sets a dict key, restoring on exit."""
    old = container.get(key)
    existed = key in container
    container[key] = value
    try:
        yield container
    finally:
        if existed:
            container[key] = old
        else:
            del container[key]


class ResourceTracker:
    """Custom context manager that tracks enter/exit lifecycle."""

    def __init__(self) -> None:
        self.entered = False
        self.exited = False
        self.exception_type = None

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exited = True
        self.exception_type = exc_type
        return False  # Don't suppress exceptions


class TestWithStatement:
    """Verify the with statement correctly invokes __enter__ and __exit__."""

    def test_enter_called(self) -> None:
        """__enter__ is invoked when entering the with block."""
        tracker = ResourceTracker()
        with tracker:
            assert tracker.entered is True

    def test_exit_called_on_normal_exit(self) -> None:
        """__exit__ is invoked when the with block completes normally."""
        tracker = ResourceTracker()
        with tracker:
            pass
        assert tracker.exited is True

    def test_exit_called_on_exception(self) -> None:
        """__exit__ is invoked even when an exception occurs."""
        tracker = ResourceTracker()
        with pytest.raises(ValueError):
            with tracker:
                raise ValueError("test error")
        assert tracker.exited is True
        assert tracker.exception_type is ValueError

    def test_as_variable_receives_enter_return(self) -> None:
        """The 'as' variable receives the return value of __enter__."""
        with ResourceTracker() as t:
            assert isinstance(t, ResourceTracker)
            assert t.entered is True


class TestContextlibContextManager:
    """Verify @contextmanager generator-based context managers."""

    def test_temp_value_sets_key(self) -> None:
        """Context manager temporarily sets the dictionary key."""
        d = {"color": "blue"}
        with temp_value(d, "color", "red") as ctx:
            assert ctx["color"] == "red"

    def test_temp_value_restores_on_exit(self) -> None:
        """Original value is restored after with block exits."""
        d = {"color": "blue"}
        with temp_value(d, "color", "red"):
            pass
        assert d["color"] == "blue"

    def test_temp_value_removes_new_key_on_exit(self) -> None:
        """Newly added key is removed when context exits."""
        d = {}
        with temp_value(d, "temp", 42):
            assert d["temp"] == 42
        assert "temp" not in d

    def test_temp_value_restores_after_exception(self) -> None:
        """Original value restored even when exception occurs inside with."""
        d = {"x": 1}
        with pytest.raises(RuntimeError):
            with temp_value(d, "x", 999):
                raise RuntimeError("oops")
        assert d["x"] == 1


class TestFileContextManager:
    """Verify file objects work correctly as context managers."""

    def test_file_auto_closes(self) -> None:
        """File is automatically closed after with block exits."""
        path = os.path.join(tempfile.gettempdir(), "ctx_test.txt")
        with open(path, "w") as f:
            f.write("test")
        assert f.closed
        os.remove(path)

    def test_file_writable_inside_with(self) -> None:
        """File is writable inside the with block."""
        path = os.path.join(tempfile.gettempdir(), "ctx_write.txt")
        with open(path, "w") as f:
            assert not f.closed
            f.write("data")
        with open(path, "r") as f:
            assert f.read() == "data"
        os.remove(path)


class TestSuppress:
    """Verify contextlib.suppress silences specified exceptions."""

    def test_suppress_catches_specified_exception(self) -> None:
        """suppress(ValueError) silences ValueError without crashing."""
        with suppress(ValueError):
            int("not_a_number")
        # If we reach here, the exception was suppressed

    def test_suppress_does_not_catch_other_exceptions(self) -> None:
        """suppress(ValueError) does not silence TypeError."""
        with pytest.raises(TypeError):
            with suppress(ValueError):
                int(None)

    def test_suppress_multiple_types(self) -> None:
        """suppress can handle multiple exception types."""
        with suppress(ValueError, KeyError):
            d = {}
            _ = d["missing"]
        # KeyError suppressed


class TestNestedContextManagers:
    """Verify multiple context managers can be nested correctly."""

    def test_nested_with_statements(self) -> None:
        """Nested with blocks both invoke enter/exit in correct order."""
        outer = ResourceTracker()
        inner = ResourceTracker()
        with outer:
            with inner:
                assert outer.entered and inner.entered
        assert outer.exited and inner.exited

    def test_combined_with_statement(self) -> None:
        """Multiple context managers in single with statement."""
        t1 = ResourceTracker()
        t2 = ResourceTracker()
        with t1, t2:
            assert t1.entered and t2.entered
        assert t1.exited and t2.exited
