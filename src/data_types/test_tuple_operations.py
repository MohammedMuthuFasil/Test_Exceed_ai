"""Additional tuple operation tests - manually written."""


def test_tuple_unpacking():
    a, b, c = (1, 2, 3)
    assert a == 1
    assert b == 2
    assert c == 3

def test_tuple_swap():
    x, y = 10, 20
    x, y = y, x
    assert x == 20
    assert y == 10

def test_tuple_concat():
    assert (1, 2) + (3, 4) == (1, 2, 3, 4)

def test_tuple_repeat():
    assert (0,) * 3 == (0, 0, 0)

def test_tuple_count():
    t = (1, 2, 2, 3, 2)
    assert t.count(2) == 3

def test_tuple_index():
    t = ("a", "b", "c")
    assert t.index("b") == 1

def test_tuple_nested():
    t = ((1, 2), (3, 4))
    assert t[0][1] == 2
    assert t[1][0] == 3

def test_tuple_membership():
    t = (10, 20, 30)
    assert 20 in t
    assert 99 not in t

def test_tuple_slicing():
    t = (0, 1, 2, 3, 4)
    assert t[1:3] == (1, 2)
    assert t[::-1] == (4, 3, 2, 1, 0)

def test_tuple_from_list():
    assert tuple([1, 2, 3]) == (1, 2, 3)

def test_tuple_single_element():
    t = (42,)
    assert len(t) == 1
    assert t[0] == 42

def test_empty_tuple():
    t = ()
    assert len(t) == 0
