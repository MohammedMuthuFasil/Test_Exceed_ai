"""String helper tests generated using copilot AI.

Covers reverse_string, count_vowels, count_letter_in_list,
count_more_letter_in_list, and count_lettes functions.
"""

from string_helper import (
    reverse_string,
    count_vowels,
    count_letter_in_list,
    count_more_letter_in_list,
    count_lettes,
)


# --- reverse_string tests ---

def test_reverse_basic():
    assert reverse_string("hello") == "olleh"

def test_reverse_palindrome():
    assert reverse_string("racecar") == "racecar"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_single_char():
    assert reverse_string("a") == "a"

def test_reverse_with_spaces():
    assert reverse_string("hi there") == "ereht ih"


# --- count_vowels tests ---

def test_vowels_basic():
    assert count_vowels("hello") == 2

def test_vowels_all_vowels():
    assert count_vowels("aeiou") == 5

def test_vowels_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_vowels_empty():
    assert count_vowels("") == 0

def test_vowels_mixed_case():
    assert count_vowels("AeIoU") == 5

def test_vowels_with_numbers():
    assert count_vowels("h3ll0 w0rld") == 0


# --- count_letter_in_list tests ---

def test_letter_count_basic():
    assert count_letter_in_list(["a", "b", "a", "c"]) == {"a": 2, "b": 1, "c": 1}

def test_letter_count_single():
    assert count_letter_in_list(["x"]) == {"x": 1}

def test_letter_count_empty():
    assert count_letter_in_list([]) == {}

def test_letter_count_all_same():
    assert count_letter_in_list(["z", "z", "z"]) == {"z": 3}


# --- count_more_letter_in_list tests ---

def test_duplicates_basic():
    counts, dups = count_more_letter_in_list(["a", "b", "a", "c", "b", "a"])
    assert counts == {"a": 3, "b": 2, "c": 1}
    assert sorted(dups) == ["a", "b"]

def test_duplicates_none():
    counts, dups = count_more_letter_in_list(["a", "b", "c"])
    assert counts == {"a": 1, "b": 1, "c": 1}
    assert dups == []

def test_duplicates_empty():
    counts, dups = count_more_letter_in_list([])
    assert counts == {}
    assert dups == []

def test_duplicates_all_same():
    counts, dups = count_more_letter_in_list(["x", "x", "x"])
    assert counts == {"x": 3}
    assert dups == ["x"]


# --- count_lettes (Counter) tests ---

def test_counter_basic():
    result = count_lettes(["a", "b", "a"])
    assert result["a"] == 2
    assert result["b"] == 1

def test_counter_empty():
    result = count_lettes([])
    assert len(result) == 0

def test_counter_single():
    result = count_lettes(["hello"])
    assert result["hello"] == 1
