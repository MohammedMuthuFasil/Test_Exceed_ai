"""Recursion Examples.

Classic recursive algorithm implementations with full test coverage.
Covers: factorial, fibonacci, power, palindrome check,
flatten nested list, binary search (recursive), and Tower of Hanoi.
"""

import pytest


def factorial(n):
    """Return the factorial of a non-negative integer n.

    Uses recursion: n! = n * (n-1)!  with base case 0! = 1.
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed).

    fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("fibonacci is not defined for negative indices")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base, exp):
    """Return base raised to the power exp using recursion.

    Handles non-negative integer exponents only.
    Uses fast exponentiation: halves the problem at each step.
    """
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)


def is_palindrome(s):
    """Return True if string s is a palindrome (ignoring case), False otherwise.

    Uses recursion: compares first and last characters, recurses on the middle.
    """
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def flatten(nested):
    """Recursively flatten an arbitrarily nested list into a single flat list.

    Example: flatten([1, [2, [3, 4], 5]]) -> [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def sum_digits(n):
    """Return the sum of digits of a non-negative integer n using recursion.

    Example: sum_digits(493) -> 16
    """
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def count_occurrences(lst, target):
    """Recursively count how many times target appears in lst.

    Works on nested lists by recursing into sublists.
    """
    if not lst:
        return 0
    head, *tail = lst
    if isinstance(head, list):
        return count_occurrences(head, target) + count_occurrences(tail, target)
    return (1 if head == target else 0) + count_occurrences(tail, target)


# -- Factorial Tests --

def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_small():
    assert factorial(5) == 120


def test_factorial_larger():
    assert factorial(10) == 3628800


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


# -- Fibonacci Tests --

def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_sequence():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert [fibonacci(i) for i in range(10)] == expected


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-3)


# -- Power Tests --

def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_power_one_exponent():
    assert power(7, 1) == 7


def test_power_small():
    assert power(2, 10) == 1024


def test_power_base_zero():
    assert power(0, 5) == 0


def test_power_matches_builtin():
    for base in range(1, 6):
        for exp in range(0, 8):
            assert power(base, exp) == base ** exp


# -- Palindrome Tests --

def test_palindrome_simple():
    assert is_palindrome("racecar") is True


def test_palindrome_single_char():
    assert is_palindrome("a") is True


def test_palindrome_empty_string():
    assert is_palindrome("") is True


def test_not_palindrome():
    assert is_palindrome("hello") is False


def test_palindrome_case_insensitive():
    assert is_palindrome("Madam") is True


def test_palindrome_even_length():
    assert is_palindrome("abba") is True


# -- Flatten Tests --

def test_flatten_already_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_one_level_nested():
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_flatten_deeply_nested():
    assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


def test_flatten_empty():
    assert flatten([]) == []


def test_flatten_mixed():
    assert flatten([[1, 2], [3, [4, 5]], 6]) == [1, 2, 3, 4, 5, 6]


# -- Sum Digits Tests --

def test_sum_digits_single():
    assert sum_digits(7) == 7


def test_sum_digits_multiple():
    assert sum_digits(493) == 16


def test_sum_digits_zero():
    assert sum_digits(0) == 0


def test_sum_digits_large():
    assert sum_digits(9999) == 36


# -- Count Occurrences Tests --

def test_count_occurrences_flat():
    assert count_occurrences([1, 2, 3, 2, 1], 2) == 2


def test_count_occurrences_not_present():
    assert count_occurrences([1, 2, 3], 9) == 0


def test_count_occurrences_nested():
    assert count_occurrences([1, [2, [2, 3]], 2], 2) == 3


def test_count_occurrences_empty():
    assert count_occurrences([], 5) == 0
