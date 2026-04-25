"""Extended exception handling tests generated using Copilot AI.

Covers multiple exception types, nested try blocks, finally clauses,
custom exceptions, and exception chaining with parametrized test cases.
"""

import pytest


class TestBuiltinExceptions:
    """Verify correct handling of Python's built-in exception types."""

    @pytest.mark.parametrize("expression, exception_type", [
        (lambda: 1 / 0, ZeroDivisionError),
        (lambda: int("abc"), ValueError),
        (lambda: [1, 2, 3][10], IndexError),
        (lambda: {"a": 1}["z"], KeyError),
        (lambda: int(None), TypeError),
    ], ids=["division_by_zero", "invalid_int_cast", "index_out_of_range", "missing_key", "none_to_int"])
    def test_expected_exception_raised(self, expression, exception_type) -> None:
        """Verify that specific operations raise the expected exception type."""
        with pytest.raises(exception_type):
            expression()

    @pytest.mark.parametrize("expression, exception_type", [
        (lambda: 1 / 0, ZeroDivisionError),
        (lambda: int("abc"), ValueError),
        (lambda: [][0], IndexError),
    ], ids=["zero_div", "bad_cast", "empty_index"])
    def test_exception_is_instance_of_base(self, expression, exception_type) -> None:
        """Verify caught exceptions are instances of Exception base class."""
        with pytest.raises(exception_type) as exc_info:
            expression()
        assert isinstance(exc_info.value, Exception)


class TestFinallyClause:
    """Verify finally block always executes regardless of exceptions."""

    def test_finally_runs_on_success(self) -> None:
        """Finally executes even when no exception occurs."""
        executed = []
        try:
            executed.append("try")
        finally:
            executed.append("finally")
        assert executed == ["try", "finally"]

    def test_finally_runs_on_exception(self) -> None:
        """Finally executes when an exception is raised and caught."""
        executed = []
        try:
            executed.append("try")
            raise ValueError("test")
        except ValueError:
            executed.append("except")
        finally:
            executed.append("finally")
        assert executed == ["try", "except", "finally"]

    def test_finally_runs_on_uncaught_exception(self) -> None:
        """Finally executes even for exceptions not caught by except."""
        executed = []
        with pytest.raises(TypeError):
            try:
                executed.append("try")
                raise TypeError("oops")
            except ValueError:
                executed.append("wrong except")
            finally:
                executed.append("finally")
        assert executed == ["try", "finally"]


class TestNestedTryBlocks:
    """Verify exception propagation through nested try/except blocks."""

    def test_inner_catch_prevents_outer(self) -> None:
        """Inner except catches exception before outer except sees it."""
        caught_by = None
        try:
            try:
                raise ValueError("inner")
            except ValueError:
                caught_by = "inner"
        except ValueError:
            caught_by = "outer"
        assert caught_by == "inner"

    def test_exception_propagates_to_outer(self) -> None:
        """Unhandled inner exception propagates to outer try block."""
        caught_by = None
        try:
            try:
                raise TypeError("propagate")
            except ValueError:
                caught_by = "inner"
        except TypeError:
            caught_by = "outer"
        assert caught_by == "outer"


class TestCustomException:
    """Verify custom exception classes work correctly with try/except."""

    def test_custom_exception_caught(self) -> None:
        """Custom exception class can be raised and caught."""
        class AppError(Exception):
            pass

        with pytest.raises(AppError):
            raise AppError("custom error")

    def test_custom_exception_with_message(self) -> None:
        """Custom exception preserves its message string."""
        class ValidationError(Exception):
            pass

        with pytest.raises(ValidationError, match="invalid input"):
            raise ValidationError("invalid input")

    def test_custom_exception_inherits_from_base(self) -> None:
        """Custom exceptions inherit from Exception and can be caught as Exception."""
        class DatabaseError(Exception):
            pass

        caught = False
        try:
            raise DatabaseError("connection lost")
        except Exception:
            caught = True
        assert caught


class TestElseClause:
    """Verify try/except/else behavior — else runs only when no exception."""

    def test_else_runs_without_exception(self) -> None:
        """Else clause executes when try block succeeds."""
        result = None
        try:
            val = 10 / 2
        except ZeroDivisionError:
            result = "error"
        else:
            result = val
        assert result == 5.0

    def test_else_skipped_on_exception(self) -> None:
        """Else clause is skipped when except catches an exception."""
        result = None
        try:
            val = 10 / 0
        except ZeroDivisionError:
            result = "error"
        else:
            result = val
        assert result == "error"
