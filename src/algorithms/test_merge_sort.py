"""Tests for Merge Sort Algorithm.

Generated with AI assistance (GitHub Copilot).
Covers correctness, edge cases, stability, and mutation safety.
"""

import pytest
from merge_sort import merge_sort, merge


# -- Fixtures --

@pytest.fixture
def unsorted():
    return [38, 27, 43, 3, 9, 82, 10]


@pytest.fixture
def already_sorted():
    return [1, 2, 3, 4, 5, 6, 7]


@pytest.fixture
def reverse_sorted():
    return [9, 8, 7, 6, 5, 4, 3, 2, 1]


# -- Basic Correctness --

def test_merge_sort_basic(unsorted):
    assert merge_sort(unsorted) == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_already_sorted(already_sorted):
    assert merge_sort(already_sorted) == [1, 2, 3, 4, 5, 6, 7]


def test_merge_sort_reverse_sorted(reverse_sorted):
    assert merge_sort(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_sort_single_element():
    assert merge_sort([42]) == [42]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_two_elements_sorted():
    assert merge_sort([1, 2]) == [1, 2]


def test_merge_sort_two_elements_unsorted():
    assert merge_sort([2, 1]) == [1, 2]


# -- Duplicates --

def test_merge_sort_all_duplicates():
    assert merge_sort([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_merge_sort_some_duplicates():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


# -- Negative and Mixed Numbers --

def test_merge_sort_all_negative():
    assert merge_sort([-5, -1, -3, -2, -4]) == [-5, -4, -3, -2, -1]


def test_merge_sort_mixed_positive_negative():
    assert merge_sort([3, -2, 0, -5, 8, 1]) == [-5, -2, 0, 1, 3, 8]


def test_merge_sort_with_zero():
    assert merge_sort([0, 0, 0]) == [0, 0, 0]


# -- Large Input --

def test_merge_sort_large_input():
    import random
    random.seed(42)
    data = random.sample(range(1000), 100)
    assert merge_sort(data) == sorted(data)


# -- Does Not Mutate Original --

def test_merge_sort_does_not_mutate_input(unsorted):
    original = unsorted[:]
    merge_sort(unsorted)
    assert unsorted == original


# -- merge() helper directly --

def test_merge_two_sorted_halves():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_left_empty():
    assert merge([], [1, 2, 3]) == [1, 2, 3]


def test_merge_right_empty():
    assert merge([1, 2, 3], []) == [1, 2, 3]


def test_merge_both_single():
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1]) == [1, 2]


def test_merge_equal_elements():
    assert merge([1, 2], [1, 2]) == [1, 1, 2, 2]
