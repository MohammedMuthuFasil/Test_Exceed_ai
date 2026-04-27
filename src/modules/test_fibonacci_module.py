from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than


def test_fib_position_zero():
    assert fibonacci_at_position(0) == 0

def test_fib_position_one():
    assert fibonacci_at_position(1) == 1

def test_fib_position_five():
    assert fibonacci_at_position(5) == 5

def test_fib_position_ten():
    assert fibonacci_at_position(10) == 55

def test_fib_smaller_than_ten():
    assert fibonacci_smaller_than(10) == [0, 1, 1, 2, 3, 5, 8]

def test_fib_smaller_than_one():
    assert fibonacci_smaller_than(1) == [0]

def test_fib_smaller_than_zero():
    assert fibonacci_smaller_than(0) == []

def test_fib_smaller_than_hundred():
    result = fibonacci_smaller_than(100)
    assert result[-1] == 89
    assert len(result) == 12
