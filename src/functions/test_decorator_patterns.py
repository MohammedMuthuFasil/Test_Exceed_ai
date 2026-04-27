"""Decorator pattern tests generated using Claude AI.

Covers function wrapping, argument forwarding, stacking decorators,
decorator factories with parameters, and functools.wraps preservation
using class-based test organization and typed signatures.
"""

import pytest
import functools
from typing import Callable


def simple_decorator(func: Callable) -> Callable:
    """Wraps function, adding 'decorated' attribute."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.decorated = True
    return wrapper


def repeat(n: int) -> Callable:
    """Decorator factory that repeats function execution n times."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


def memoize(func: Callable) -> Callable:
    """Caching decorator that stores previously computed results."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper


def validate_positive(func: Callable) -> Callable:
    """Decorator that validates all positional args are positive numbers."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Expected positive number, got {arg}")
        return func(*args, **kwargs)
    return wrapper


class TestSimpleDecorator:
    """Verify basic decorator wrapping behavior."""

    def test_preserves_return_value(self) -> None:
        """Decorated function returns the same value as original."""
        @simple_decorator
        def greet():
            return "hello"
        assert greet() == "hello"

    def test_adds_attribute(self) -> None:
        """Decorator attaches custom attribute to wrapper."""
        @simple_decorator
        def noop():
            pass
        assert hasattr(noop, 'decorated')
        assert noop.decorated is True

    def test_preserves_function_name(self) -> None:
        """functools.wraps preserves original function __name__."""
        @simple_decorator
        def my_func():
            pass
        assert my_func.__name__ == "my_func"

    def test_preserves_docstring(self) -> None:
        """functools.wraps preserves original function __doc__."""
        @simple_decorator
        def documented():
            """My docstring."""
            pass
        assert documented.__doc__ == "My docstring."

    def test_forwards_arguments(self) -> None:
        """Decorated function correctly receives args and kwargs."""
        @simple_decorator
        def add(a, b, extra=0):
            return a + b + extra
        assert add(2, 3, extra=5) == 10


class TestDecoratorFactory:
    """Verify parameterized decorator factory behavior."""

    def test_repeat_executes_n_times(self) -> None:
        """@repeat(n) calls the function exactly n times."""
        call_count = 0
        @repeat(3)
        def increment():
            nonlocal call_count
            call_count += 1
            return call_count
        results = increment()
        assert len(results) == 3
        assert call_count == 3

    @pytest.mark.parametrize("n, expected_len", [
        (1, 1),
        (5, 5),
        (0, 0),
    ], ids=["once", "five_times", "zero_times"])
    def test_repeat_various_counts(self, n: int, expected_len: int) -> None:
        """@repeat(n) returns list of length n."""
        @repeat(n)
        def constant():
            return 42
        assert len(constant()) == expected_len

    def test_repeat_preserves_return_values(self) -> None:
        """Each repetition captures the function's return value."""
        @repeat(3)
        def get_value():
            return "ok"
        assert get_value() == ["ok", "ok", "ok"]


class TestMemoizeDecorator:
    """Verify caching decorator stores and reuses computed results."""

    def test_caches_result(self) -> None:
        """Second call with same args returns cached result without recomputing."""
        call_count = 0
        @memoize
        def expensive(n):
            nonlocal call_count
            call_count += 1
            return n * n
        expensive(5)
        expensive(5)
        assert call_count == 1

    def test_different_args_not_cached(self) -> None:
        """Different arguments produce separate cache entries."""
        @memoize
        def square(n):
            return n * n
        assert square(3) == 9
        assert square(4) == 16
        assert len(square.cache) == 2

    def test_cache_returns_correct_value(self) -> None:
        """Cached return value matches original computation."""
        @memoize
        def double(n):
            return n * 2
        first = double(7)
        second = double(7)
        assert first == second == 14


class TestValidationDecorator:
    """Verify argument validation decorator rejects invalid inputs."""

    def test_accepts_positive_args(self) -> None:
        """Valid positive arguments pass through successfully."""
        @validate_positive
        def multiply(a, b):
            return a * b
        assert multiply(3, 4) == 12

    @pytest.mark.parametrize("args", [
        (-1, 2),
        (1, 0),
        (1, -5),
    ], ids=["first_negative", "second_zero", "second_negative"])
    def test_rejects_non_positive_args(self, args) -> None:
        """Non-positive arguments raise ValueError."""
        @validate_positive
        def add(a, b):
            return a + b
        with pytest.raises(ValueError):
            add(*args)


class TestStackedDecorators:
    """Verify multiple decorators applied to the same function."""

    def test_stacked_order_matters(self) -> None:
        """Decorators apply bottom-up: @repeat wraps first, then @simple_decorator."""
        @simple_decorator
        @repeat(2)
        def greet():
            return "hi"
        result = greet()
        assert result == ["hi", "hi"]
        assert greet.decorated is True
