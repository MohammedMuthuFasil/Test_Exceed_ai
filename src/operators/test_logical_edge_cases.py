"""Additional logical operator tests - manually written for short-circuit and truthiness."""


def test_and_short_circuit():
    result = False and (1 / 0)
    assert result == False

def test_or_short_circuit():
    result = True or (1 / 0)
    assert result == True

def test_and_returns_first_falsy():
    assert (0 and "hello") == 0
    assert ("" and "hello") == ""

def test_and_returns_last_truthy():
    assert ("a" and "b") == "b"
    assert (1 and 2 and 3) == 3

def test_or_returns_first_truthy():
    assert (0 or "hello") == "hello"
    assert ("" or 0 or "found") == "found"

def test_or_returns_last_if_all_falsy():
    assert (0 or "" or None) is None

def test_not_basic():
    assert not False
    assert not 0
    assert not ""
    assert not None

def test_chained_comparison():
    x = 5
    assert 1 < x < 10
    assert not (10 < x < 20)

def test_none_is_falsy():
    assert not None
    assert (None or "default") == "default"

def test_empty_collections_falsy():
    assert not []
    assert not {}
    assert not set()
    assert not ()
