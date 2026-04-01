"""Sorting Algorithms.

Implementations and tests of common sorting algorithms in Python.
Covers bubble sort, merge sort, quick sort, and insertion sort.
"""

import pytest


def bubble_sort(arr):
    """Sort a list using the bubble sort algorithm.

    Repeatedly steps through the list, compares adjacent elements and swaps them
    if they are in the wrong order. Time complexity: O(n^2).
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(arr):
    """Sort a list using the merge sort algorithm.

    Divides the list into halves, recursively sorts each half,
    then merges the sorted halves. Time complexity: O(n log n).
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """Sort a list using the quick sort algorithm.

    Selects a pivot element and partitions the array around it.
    Time complexity: O(n log n) average, O(n^2) worst case.
    """
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    """Sort a list using the insertion sort algorithm.

    Builds the sorted list one element at a time by inserting each new element
    into its correct position. Time complexity: O(n^2).
    """
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# -- Tests --

@pytest.fixture
def unsorted_list():
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def already_sorted():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def reverse_sorted():
    return [5, 4, 3, 2, 1]


def test_bubble_sort_basic(unsorted_list):
    assert bubble_sort(unsorted_list) == [11, 12, 22, 25, 34, 64, 90]


def test_bubble_sort_already_sorted(already_sorted):
    assert bubble_sort(already_sorted) == [1, 2, 3, 4, 5]


def test_bubble_sort_reverse(reverse_sorted):
    assert bubble_sort(reverse_sorted) == [1, 2, 3, 4, 5]


def test_bubble_sort_single_element():
    assert bubble_sort([42]) == [42]


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_does_not_mutate_original(unsorted_list):
    original = unsorted_list[:]
    bubble_sort(unsorted_list)
    assert unsorted_list == original


def test_merge_sort_basic(unsorted_list):
    assert merge_sort(unsorted_list) == [11, 12, 22, 25, 34, 64, 90]


def test_merge_sort_already_sorted(already_sorted):
    assert merge_sort(already_sorted) == [1, 2, 3, 4, 5]


def test_merge_sort_reverse(reverse_sorted):
    assert merge_sort(reverse_sorted) == [1, 2, 3, 4, 5]


def test_merge_sort_single_element():
    assert merge_sort([7]) == [7]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_duplicates():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_quick_sort_basic(unsorted_list):
    assert quick_sort(unsorted_list) == [11, 12, 22, 25, 34, 64, 90]


def test_quick_sort_already_sorted(already_sorted):
    assert quick_sort(already_sorted) == [1, 2, 3, 4, 5]


def test_quick_sort_reverse(reverse_sorted):
    assert quick_sort(reverse_sorted) == [1, 2, 3, 4, 5]


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_insertion_sort_basic(unsorted_list):
    assert insertion_sort(unsorted_list) == [11, 12, 22, 25, 34, 64, 90]


def test_insertion_sort_already_sorted(already_sorted):
    assert insertion_sort(already_sorted) == [1, 2, 3, 4, 5]


def test_insertion_sort_reverse(reverse_sorted):
    assert insertion_sort(reverse_sorted) == [1, 2, 3, 4, 5]


def test_insertion_sort_empty():
    assert insertion_sort([]) == []


def test_all_sorts_agree():
    """All sorting algorithms should produce the same result."""
    data = [38, 27, 43, 3, 9, 82, 10]
    expected = sorted(data)
    assert bubble_sort(data) == expected
    assert merge_sort(data) == expected
    assert quick_sort(data) == expected
    assert insertion_sort(data) == expected
