"""Search Algorithms.

Implementations and tests of common search algorithms in Python.
Covers linear search, binary search, and jump search.
"""

import math
import pytest


def linear_search(arr, target):
    """Search for a target value using linear search.

    Iterates through each element until the target is found.
    Returns the index if found, -1 otherwise.
    Time complexity: O(n).
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def binary_search(arr, target):
    """Search for a target value in a sorted list using binary search.

    Repeatedly divides the search interval in half.
    Returns the index if found, -1 otherwise.
    Time complexity: O(log n). Requires sorted input.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    """Recursive implementation of binary search.

    Returns the index of target in arr, or -1 if not found.
    """
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def jump_search(arr, target):
    """Search for a target value in a sorted list using jump search.

    Jumps ahead by fixed steps to find the block containing the target,
    then performs a linear search within that block.
    Time complexity: O(√n). Requires sorted input.
    """
    n = len(arr)
    if n == 0:
        return -1
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


# -- Tests --

@pytest.fixture
def sorted_numbers():
    return [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]


def test_linear_search_found(sorted_numbers):
    assert linear_search(sorted_numbers, 23) == 5


def test_linear_search_first_element(sorted_numbers):
    assert linear_search(sorted_numbers, 2) == 0


def test_linear_search_last_element(sorted_numbers):
    assert linear_search(sorted_numbers, 91) == 9


def test_linear_search_not_found(sorted_numbers):
    assert linear_search(sorted_numbers, 99) == -1


def test_linear_search_empty_list():
    assert linear_search([], 5) == -1


def test_binary_search_found(sorted_numbers):
    assert binary_search(sorted_numbers, 23) == 5


def test_binary_search_first_element(sorted_numbers):
    assert binary_search(sorted_numbers, 2) == 0


def test_binary_search_last_element(sorted_numbers):
    assert binary_search(sorted_numbers, 91) == 9


def test_binary_search_not_found(sorted_numbers):
    assert binary_search(sorted_numbers, 10) == -1


def test_binary_search_empty_list():
    assert binary_search([], 5) == -1


def test_binary_search_single_element_found():
    assert binary_search([42], 42) == 0


def test_binary_search_single_element_not_found():
    assert binary_search([42], 10) == -1


def test_binary_search_recursive_found(sorted_numbers):
    assert binary_search_recursive(sorted_numbers, 56) == 7


def test_binary_search_recursive_not_found(sorted_numbers):
    assert binary_search_recursive(sorted_numbers, 100) == -1


def test_jump_search_found(sorted_numbers):
    assert jump_search(sorted_numbers, 38) == 6


def test_jump_search_first_element(sorted_numbers):
    assert jump_search(sorted_numbers, 2) == 0


def test_jump_search_last_element(sorted_numbers):
    assert jump_search(sorted_numbers, 91) == 9


def test_jump_search_not_found(sorted_numbers):
    assert jump_search(sorted_numbers, 50) == -1


def test_jump_search_empty():
    assert jump_search([], 5) == -1


def test_all_searches_agree(sorted_numbers):
    """Linear and binary search should return the same index for the same target."""
    for target in sorted_numbers:
        li = linear_search(sorted_numbers, target)
        bi = binary_search(sorted_numbers, target)
        assert li == bi
