"""Additional list comprehension tests - manually written."""


def test_basic_comprehension():
    result = [x * 2 for x in range(5)]
    assert result == [0, 2, 4, 6, 8]

def test_filtered_comprehension():
    result = [x for x in range(10) if x % 3 == 0]
    assert result == [0, 3, 6, 9]

def test_string_comprehension():
    words = ["hello", "world"]
    result = [w.upper() for w in words]
    assert result == ["HELLO", "WORLD"]

def test_nested_comprehension_flatten():
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [num for row in matrix for num in row]
    assert flat == [1, 2, 3, 4, 5, 6]

def test_dict_comprehension():
    result = {k: v for k, v in zip("abc", [1, 2, 3])}
    assert result == {"a": 1, "b": 2, "c": 3}

def test_set_comprehension():
    result = {x % 3 for x in range(10)}
    assert result == {0, 1, 2}

def test_conditional_expression_in_comprehension():
    result = ["even" if x % 2 == 0 else "odd" for x in range(4)]
    assert result == ["even", "odd", "even", "odd"]

def test_comprehension_with_function():
    result = [len(w) for w in ["hi", "hello", "hey"]]
    assert result == [2, 5, 3]

def test_comprehension_empty_result():
    result = [x for x in range(10) if x > 100]
    assert result == []

def test_enumerate_in_comprehension():
    result = [(i, v) for i, v in enumerate(["a", "b"])]
    assert result == [(0, "a"), (1, "b")]
