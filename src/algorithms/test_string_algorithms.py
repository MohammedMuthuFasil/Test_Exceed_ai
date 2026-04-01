"""String Algorithms.

Implementations and tests for common string manipulation algorithms:
- Anagram detection
- Longest common prefix
- Count vowels and consonants
- Reverse words in a sentence
- Caesar cipher encode/decode
- Run-length encoding
- Check pangram
"""

import pytest


def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams of each other (case-insensitive).

    Two strings are anagrams if they contain the same characters
    with the same frequencies, ignoring spaces and case.
    """
    clean = lambda s: sorted(s.lower().replace(" ", ""))
    return clean(s1) == clean(s2)


def longest_common_prefix(words):
    """Return the longest common prefix string among a list of words.

    Returns an empty string if there is no common prefix or the list is empty.
    """
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def count_vowels_consonants(text):
    """Return a dict with counts of vowels and consonants in text (ignoring non-alpha chars)."""
    vowels = set("aeiouAEIOU")
    result = {"vowels": 0, "consonants": 0}
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                result["vowels"] += 1
            else:
                result["consonants"] += 1
    return result


def reverse_words(sentence):
    """Reverse the order of words in a sentence, preserving single spacing."""
    return " ".join(sentence.split()[::-1])


def caesar_cipher(text, shift):
    """Encode text using the Caesar cipher with the given shift.

    Only shifts alphabetic characters; preserves case and non-alpha characters.
    """
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def run_length_encode(s):
    """Compress a string using run-length encoding.

    Example: "aaabbc" -> "a3b2c1"
    """
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)


def run_length_decode(s):
    """Decompress a run-length encoded string.

    Example: "a3b2c1" -> "aaabbc"
    """
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        result.append(char * int(num_str))
    return "".join(result)


def is_pangram(sentence):
    """Return True if the sentence contains every letter of the alphabet at least once."""
    return set("abcdefghijklmnopqrstuvwxyz").issubset(set(sentence.lower()))


# -- Anagram Tests --

def test_anagram_simple():
    assert is_anagram("listen", "silent") is True


def test_anagram_with_spaces():
    assert is_anagram("Astronomer", "Moon starer") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_anagram_case_insensitive():
    assert is_anagram("Listen", "Silent") is True


def test_anagram_different_lengths():
    assert is_anagram("abc", "ab") is False


def test_anagram_empty_strings():
    assert is_anagram("", "") is True


# -- Longest Common Prefix Tests --

def test_lcp_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"


def test_lcp_no_common_prefix():
    assert longest_common_prefix(["dog", "car", "race"]) == ""


def test_lcp_single_word():
    assert longest_common_prefix(["only"]) == "only"


def test_lcp_empty_list():
    assert longest_common_prefix([]) == ""


def test_lcp_identical_words():
    assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"


def test_lcp_one_empty_string():
    assert longest_common_prefix(["", "abc"]) == ""


# -- Vowel/Consonant Count Tests --

def test_count_vowels_consonants_basic():
    result = count_vowels_consonants("hello")
    assert result["vowels"] == 2
    assert result["consonants"] == 3


def test_count_vowels_consonants_ignores_non_alpha():
    result = count_vowels_consonants("h3ll0 w0rld!")
    assert result["vowels"] == 0
    assert result["consonants"] == 7


def test_count_vowels_consonants_empty():
    result = count_vowels_consonants("")
    assert result["vowels"] == 0
    assert result["consonants"] == 0


def test_count_vowels_consonants_all_vowels():
    result = count_vowels_consonants("aeiou")
    assert result["vowels"] == 5
    assert result["consonants"] == 0


# -- Reverse Words Tests --

def test_reverse_words_basic():
    assert reverse_words("Hello World") == "World Hello"


def test_reverse_words_single_word():
    assert reverse_words("Python") == "Python"


def test_reverse_words_extra_spaces():
    assert reverse_words("  hello   world  ") == "world hello"


def test_reverse_words_empty():
    assert reverse_words("") == ""


# -- Caesar Cipher Tests --

def test_caesar_shift_3():
    assert caesar_cipher("ABC", 3) == "DEF"


def test_caesar_wraps_around():
    assert caesar_cipher("XYZ", 3) == "ABC"


def test_caesar_decode():
    encoded = caesar_cipher("Hello, World!", 13)
    decoded = caesar_cipher(encoded, -13)
    assert decoded == "Hello, World!"


def test_caesar_preserves_non_alpha():
    assert caesar_cipher("Hello, World!", 0) == "Hello, World!"


def test_caesar_lowercase():
    assert caesar_cipher("abc", 1) == "bcd"


# -- Run-Length Encoding Tests --

def test_rle_encode_basic():
    assert run_length_encode("aaabbc") == "a3b2c1"


def test_rle_encode_no_repeats():
    assert run_length_encode("abc") == "a1b1c1"


def test_rle_encode_single_char():
    assert run_length_encode("a") == "a1"


def test_rle_encode_empty():
    assert run_length_encode("") == ""


def test_rle_decode_basic():
    assert run_length_decode("a3b2c1") == "aaabbc"


def test_rle_roundtrip():
    original = "aaabbccddddee"
    assert run_length_decode(run_length_encode(original)) == original


# -- Pangram Tests --

def test_pangram_true():
    assert is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_pangram_false():
    assert is_pangram("Hello World") is False


def test_pangram_empty():
    assert is_pangram("") is False


def test_pangram_case_insensitive():
    assert is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") is True
