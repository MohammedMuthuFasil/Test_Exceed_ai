"""Additional dictionary tests - manually split into granular test functions."""


def test_dict_get_existing_key():
    d = {"a": 1, "b": 2}
    assert d.get("a") == 1

def test_dict_get_missing_key_default():
    d = {"a": 1}
    assert d.get("z", 0) == 0

def test_dict_get_missing_key_none():
    d = {"a": 1}
    assert d.get("z") is None

def test_dict_pop_removes_key():
    d = {"a": 1, "b": 2}
    val = d.pop("a")
    assert val == 1
    assert "a" not in d

def test_dict_pop_default():
    d = {"a": 1}
    val = d.pop("z", 99)
    assert val == 99

def test_dict_update_merges():
    d = {"a": 1}
    d.update({"b": 2, "c": 3})
    assert d == {"a": 1, "b": 2, "c": 3}

def test_dict_update_overwrites():
    d = {"a": 1, "b": 2}
    d.update({"b": 99})
    assert d["b"] == 99

def test_dict_keys():
    d = {"x": 10, "y": 20}
    assert sorted(d.keys()) == ["x", "y"]

def test_dict_values():
    d = {"x": 10, "y": 20}
    assert sorted(d.values()) == [10, 20]

def test_dict_items():
    d = {"x": 10}
    assert list(d.items()) == [("x", 10)]

def test_dict_clear():
    d = {"a": 1, "b": 2}
    d.clear()
    assert d == {}
    assert len(d) == 0

def test_dict_copy_is_independent():
    d = {"a": 1}
    d2 = d.copy()
    d2["a"] = 99
    assert d["a"] == 1

def test_dict_setdefault_missing():
    d = {"a": 1}
    val = d.setdefault("b", 5)
    assert val == 5
    assert d["b"] == 5

def test_dict_setdefault_existing():
    d = {"a": 1}
    val = d.setdefault("a", 99)
    assert val == 1
