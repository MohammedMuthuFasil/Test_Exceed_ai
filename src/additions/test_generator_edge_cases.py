"""Extended generator tests generated using Copilot AI.

Covers generator exhaustion, send/throw protocol, yield from delegation,
infinite generators with islice, and generator expressions with
class-based test organization and docstrings.
"""

import pytest
from itertools import islice


def countdown(n):
    """Simple countdown generator yielding from n down to 1."""
    while n > 0:
        yield n
        n -= 1


def fibonacci_gen():
    """Infinite Fibonacci generator using yield."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def echo_generator():
    """Generator that echoes back values sent to it via .send()."""
    received = yield "ready"
    while True:
        received = yield f"echo: {received}"


def chain_generators(*iterables):
    """Delegate to sub-iterables using yield from."""
    for it in iterables:
        yield from it


class TestBasicGeneratorBehavior:
    """Verify fundamental generator mechanics: iteration, exhaustion, type."""

    def test_generator_is_iterator(self) -> None:
        """Generator objects implement the iterator protocol."""
        gen = countdown(3)
        assert hasattr(gen, '__next__')
        assert hasattr(gen, '__iter__')

    def test_generator_yields_expected_sequence(self) -> None:
        """Countdown generator produces values in descending order."""
        assert list(countdown(5)) == [5, 4, 3, 2, 1]

    def test_generator_empty_input(self) -> None:
        """Generator with n=0 yields nothing."""
        assert list(countdown(0)) == []

    def test_generator_single_yield(self) -> None:
        """Generator with n=1 yields exactly one value."""
        assert list(countdown(1)) == [1]

    def test_generator_exhaustion_raises_stopiteration(self) -> None:
        """Calling next() on exhausted generator raises StopIteration."""
        gen = countdown(1)
        next(gen)
        with pytest.raises(StopIteration):
            next(gen)

    def test_exhausted_generator_stays_empty(self) -> None:
        """Re-iterating an exhausted generator produces nothing."""
        gen = countdown(2)
        first_pass = list(gen)
        second_pass = list(gen)
        assert first_pass == [2, 1]
        assert second_pass == []


class TestInfiniteGenerator:
    """Verify infinite generators work correctly with islice limiting."""

    def test_fibonacci_first_ten(self) -> None:
        """First 10 Fibonacci numbers match known sequence."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        result = list(islice(fibonacci_gen(), 10))
        assert result == expected

    def test_fibonacci_first_value(self) -> None:
        """First Fibonacci value is 0."""
        gen = fibonacci_gen()
        assert next(gen) == 0

    def test_islice_limits_infinite_generator(self) -> None:
        """islice correctly caps output from infinite generator."""
        result = list(islice(fibonacci_gen(), 5))
        assert len(result) == 5


class TestSendProtocol:
    """Verify generator .send() protocol for two-way communication."""

    def test_send_initial_value(self) -> None:
        """First next() on echo generator returns 'ready'."""
        gen = echo_generator()
        initial = next(gen)
        assert initial == "ready"

    def test_send_receives_value(self) -> None:
        """Sending a value to generator returns it echoed back."""
        gen = echo_generator()
        next(gen)
        result = gen.send("hello")
        assert result == "echo: hello"

    def test_send_multiple_values(self) -> None:
        """Multiple sends each produce the corresponding echo."""
        gen = echo_generator()
        next(gen)
        assert gen.send("first") == "echo: first"
        assert gen.send("second") == "echo: second"


class TestYieldFrom:
    """Verify yield from delegation to sub-iterables."""

    def test_chain_two_lists(self) -> None:
        """yield from chains two lists into a single sequence."""
        result = list(chain_generators([1, 2], [3, 4]))
        assert result == [1, 2, 3, 4]

    def test_chain_with_empty(self) -> None:
        """yield from skips empty iterables gracefully."""
        result = list(chain_generators([1], [], [2]))
        assert result == [1, 2]

    def test_chain_generators(self) -> None:
        """yield from works with generator sub-iterables."""
        result = list(chain_generators(countdown(2), countdown(3)))
        assert result == [2, 1, 3, 2, 1]


class TestGeneratorExpression:
    """Verify generator expressions (inline generators) behavior."""

    def test_genexpr_sum(self) -> None:
        """Generator expression can be consumed by sum()."""
        total = sum(x * x for x in range(5))
        assert total == 30  # 0+1+4+9+16

    def test_genexpr_is_lazy(self) -> None:
        """Generator expression does not evaluate all values upfront."""
        gen = (x for x in range(1000000))
        first = next(gen)
        assert first == 0

    def test_genexpr_with_filter(self) -> None:
        """Generator expression with condition filters correctly."""
        evens = list(x for x in range(10) if x % 2 == 0)
        assert evens == [0, 2, 4, 6, 8]
