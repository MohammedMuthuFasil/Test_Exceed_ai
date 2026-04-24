"""Edge case and input validation tests across utility modules.

Generated using GitHub Copilot AI — systematically tests boundary conditions,
type mismatches, and unexpected inputs using pytest.mark.parametrize and
class-based test organization.
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from calculator import add, subtract, multiply, divide
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin
from string_helper import reverse_string, count_vowels, count_letter_in_list


class TestCalculatorEdgeCases:
    """Validate calculator functions handle edge case numeric inputs correctly."""

    @pytest.mark.parametrize("a, b, expected", [
        (0, 0, 0),
        (-1, 1, 0),
        (999999, 1, 1000000),
        (1.5, 2.5, 4.0),
        (-0.1, 0.1, 0.0),
    ], ids=["zero+zero", "neg+pos", "large_number", "floats", "neg_float+pos_float"])
    def test_add_edge_inputs(self, a: float, b: float, expected: float) -> None:
        """Verify add() handles zeros, negatives, large numbers, and floats."""
        assert add(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("a, b, expected", [
        (0, 0, 0),
        (0, 5, -5),
        (-3, -3, 0),
        (1e10, 1, 1e10 - 1),
    ], ids=["zero-zero", "zero-positive", "neg-neg", "large_minus_small"])
    def test_subtract_edge_inputs(self, a: float, b: float, expected: float) -> None:
        """Verify subtract() with boundary numeric values."""
        assert subtract(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("a, b, expected", [
        (0, 100, 0),
        (-1, -1, 1),
        (0.1, 10, 1.0),
    ], ids=["zero_mult", "neg_times_neg", "float_precision"])
    def test_multiply_edge_inputs(self, a: float, b: float, expected: float) -> None:
        """Verify multiply() preserves sign rules and float precision."""
        assert multiply(a, b) == pytest.approx(expected)

    def test_divide_returns_float(self) -> None:
        """Verify divide() always returns a float, even for integer inputs."""
        result = divide(10, 3)
        assert isinstance(result, float)
        assert result == pytest.approx(3.3333, rel=1e-3)

    def test_divide_negative_by_negative(self) -> None:
        """Verify divide() with two negatives returns positive."""
        assert divide(-10, -2) == pytest.approx(5.0)


class TestTemperatureEdgeCases:
    """Validate temperature conversions at physical boundary values."""

    @pytest.mark.parametrize("celsius, fahrenheit", [
        (-273.15, -459.67),
        (-40, -40),
        (0, 32),
        (100, 212),
    ], ids=["absolute_zero", "crossover_point", "water_freeze", "water_boil"])
    def test_c_to_f_known_values(self, celsius: float, fahrenheit: float) -> None:
        """Verify Celsius-to-Fahrenheit against known physical constants."""
        assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit, rel=1e-4)

    @pytest.mark.parametrize("fahrenheit, celsius", [
        (-459.67, -273.15),
        (0, -17.7778),
        (98.6, 37.0),
    ], ids=["absolute_zero_f", "zero_f", "body_temp"])
    def test_f_to_c_known_values(self, fahrenheit: float, celsius: float) -> None:
        """Verify Fahrenheit-to-Celsius against known physical constants."""
        assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(celsius, rel=1e-3)

    def test_kelvin_never_negative_at_absolute_zero(self) -> None:
        """Verify absolute zero in Celsius converts to exactly 0 Kelvin."""
        assert celsius_to_kelvin(-273.15) == pytest.approx(0.0, abs=1e-10)

    def test_roundtrip_c_f_c(self) -> None:
        """Verify converting C→F→C returns the original value (roundtrip)."""
        original = 25.0
        roundtrip = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
        assert roundtrip == pytest.approx(original)


class TestStringEdgeCases:
    """Validate string helper functions with unusual and boundary inputs."""

    @pytest.mark.parametrize("input_str, expected", [
        ("a", "a"),
        ("ab", "ba"),
        ("  ", "  "),
        ("a b c", "c b a"),
    ], ids=["single_char", "two_chars", "spaces_only", "with_spaces"])
    def test_reverse_string_boundaries(self, input_str: str, expected: str) -> None:
        """Verify reverse_string handles minimal and whitespace inputs."""
        assert reverse_string(input_str) == expected

    @pytest.mark.parametrize("input_str, expected", [
        ("aeiouAEIOU", 10),
        ("12345!@#$%", 0),
        ("rhythm", 0),
        ("a", 1),
    ], ids=["all_vowels_mixed_case", "no_letters", "no_vowels_word", "single_vowel"])
    def test_count_vowels_boundaries(self, input_str: str, expected: int) -> None:
        """Verify count_vowels with edge case character sets."""
        assert count_vowels(input_str) == expected

    def test_count_letter_in_list_with_numbers(self) -> None:
        """Verify count_letter_in_list works with non-string items."""
        result = count_letter_in_list([1, 2, 1, 3, 2, 1])
        assert result == {1: 3, 2: 2, 3: 1}

    def test_count_letter_in_list_single_item(self) -> None:
        """Verify count_letter_in_list with a single-element list."""
        assert count_letter_in_list(["only"]) == {"only": 1}
