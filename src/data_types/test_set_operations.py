"""Additional set operation tests - manually split into granular test functions."""


def test_set_union():
    a = {1, 2, 3}
    b = {3, 4, 5}
    assert a | b == {1, 2, 3, 4, 5}

def test_set_intersection():
    a = {1, 2, 3}
    b = {2, 3, 4}
    assert a & b == {2, 3}

def test_set_difference():
    a = {1, 2, 3}
    b = {2, 3, 4}
    assert a - b == {1}

def test_set_symmetric_difference():
    a = {1, 2, 3}
    b = {2, 3, 4}
    assert a ^ b == {1, 4}

def test_set_issubset():
    a = {1, 2}
    b = {1, 2, 3, 4}
    assert a.issubset(b)

def test_set_issuperset():
    a = {1, 2, 3, 4}
    b = {1, 2}
    assert a.issuperset(b)

def test_set_isdisjoint():
    a = {1, 2}
    b = {3, 4}
    assert a.isdisjoint(b)

def test_set_not_disjoint():
    a = {1, 2}
    b = {2, 3}
    assert not a.isdisjoint(b)

def test_set_add():
    s = {1, 2}
    s.add(3)
    assert s == {1, 2, 3}

def test_set_add_duplicate():
    s = {1, 2}
    s.add(2)
    assert s == {1, 2}

def test_set_discard():
    s = {1, 2, 3}
    s.discard(2)
    assert s == {1, 3}

def test_set_discard_missing_no_error():
    s = {1, 2}
    s.discard(99)
    assert s == {1, 2}

def test_set_from_list_removes_dupes():
    lst = [1, 2, 2, 3, 3, 3]
    assert set(lst) == {1, 2, 3}

def test_set_len():
    assert len({1, 2, 3}) == 3
    assert len(set()) == 0
