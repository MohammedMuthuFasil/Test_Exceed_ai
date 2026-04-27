"""Extended regex pattern matching tests generated using Copilot AI.

Covers re.match, re.search, re.findall, re.sub, re.split, and compiled
patterns with systematic valid/invalid input parametrization.
"""

import pytest
import re


class TestReMatch:
    """Verify re.match anchors pattern to the start of the string."""

    @pytest.mark.parametrize("pattern, string, expected_group", [
        (r'\d+', '123abc', '123'),
        (r'[A-Z]', 'Hello', 'H'),
        (r'http', 'http://example.com', 'http'),
    ], ids=["digits_at_start", "uppercase_at_start", "protocol_prefix"])
    def test_match_at_start(self, pattern: str, string: str, expected_group: str) -> None:
        """re.match finds pattern only at the beginning of string."""
        m = re.match(pattern, string)
        assert m is not None
        assert m.group() == expected_group

    @pytest.mark.parametrize("pattern, string", [
        (r'\d+', 'abc123'),
        (r'world', 'hello world'),
    ], ids=["digits_not_at_start", "word_in_middle"])
    def test_match_fails_when_not_at_start(self, pattern: str, string: str) -> None:
        """re.match returns None when pattern is not at position 0."""
        assert re.match(pattern, string) is None


class TestReSearch:
    """Verify re.search scans the entire string for first match."""

    @pytest.mark.parametrize("pattern, string, expected", [
        (r'\d+', 'abc123def', '123'),
        (r'[aeiou]', 'bcdfg_a', 'a'),
        (r'\bworld\b', 'hello world', 'world'),
    ], ids=["digits_in_middle", "vowel_at_end", "whole_word"])
    def test_search_finds_anywhere(self, pattern: str, string: str, expected: str) -> None:
        """re.search finds the first occurrence anywhere in string."""
        m = re.search(pattern, string)
        assert m is not None
        assert m.group() == expected

    def test_search_returns_none_on_no_match(self) -> None:
        """re.search returns None when pattern is absent."""
        assert re.search(r'\d+', 'no digits here') is None


class TestReFindall:
    """Verify re.findall returns all non-overlapping matches."""

    @pytest.mark.parametrize("pattern, string, expected", [
        (r'\d+', 'a1b22c333', ['1', '22', '333']),
        (r'[A-Z]', 'Hello World', ['H', 'W']),
        (r'\b\w{3}\b', 'I am the one', ['the', 'one']),
    ], ids=["all_digit_groups", "uppercase_letters", "three_letter_words"])
    def test_findall_returns_list(self, pattern: str, string: str, expected: list) -> None:
        """re.findall returns a list of all matching substrings."""
        assert re.findall(pattern, string) == expected

    def test_findall_empty_on_no_match(self) -> None:
        """re.findall returns empty list when no matches exist."""
        assert re.findall(r'\d+', 'no numbers') == []


class TestReSub:
    """Verify re.sub replaces matched patterns correctly."""

    @pytest.mark.parametrize("pattern, replacement, string, expected", [
        (r'\d', '#', 'a1b2c3', 'a#b#c#'),
        (r'\s+', ' ', 'too   many    spaces', 'too many spaces'),
        (r'[aeiou]', '*', 'hello', 'h*ll*'),
    ], ids=["digits_to_hash", "collapse_whitespace", "vowels_to_star"])
    def test_sub_replaces(self, pattern: str, replacement: str, string: str, expected: str) -> None:
        """re.sub replaces all occurrences of pattern."""
        assert re.sub(pattern, replacement, string) == expected

    def test_sub_with_count_limits(self) -> None:
        """re.sub with count parameter limits replacements."""
        result = re.sub(r'\d', 'X', '1a2b3c', count=2)
        assert result == 'XaXb3c'


class TestReSplit:
    """Verify re.split divides strings by pattern matches."""

    @pytest.mark.parametrize("pattern, string, expected", [
        (r'[,;]', 'a,b;c', ['a', 'b', 'c']),
        (r'\s+', 'one  two   three', ['one', 'two', 'three']),
        (r'-', 'no-dashes-here', ['no', 'dashes', 'here']),
    ], ids=["comma_or_semicolon", "multiple_whitespace", "dashes"])
    def test_split_by_pattern(self, pattern: str, string: str, expected: list) -> None:
        """re.split divides string at each pattern match."""
        assert re.split(pattern, string) == expected


class TestCompiledPattern:
    """Verify compiled regex patterns behave identically to inline."""

    def test_compiled_match(self) -> None:
        """Compiled pattern produces same result as re.match."""
        pattern = re.compile(r'\d{3}')
        m = pattern.match('456abc')
        assert m is not None
        assert m.group() == '456'

    def test_compiled_findall(self) -> None:
        """Compiled pattern findall matches inline findall."""
        pattern = re.compile(r'[a-z]+')
        assert pattern.findall('abc 123 def') == ['abc', 'def']

    def test_compiled_reusable(self) -> None:
        """Same compiled pattern works across multiple strings."""
        email_re = re.compile(r'[\w.]+@[\w.]+')
        assert email_re.search('contact user@test.com here') is not None
        assert email_re.search('no email here') is None
