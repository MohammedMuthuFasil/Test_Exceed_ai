import random

import pytest

from backoff import exponential_backoff_delay


@pytest.mark.parametrize(
    "attempt,expected_base",
    [
        (0, 0.1),
        (1, 0.2),
        (2, 0.4),
        (3, 0.8),
    ],
)
def test_exponential_backoff_no_jitter_matches_expected(attempt, expected_base):
    delay = exponential_backoff_delay(
        attempt,
        base_delay=0.1,
        factor=2.0,
        jitter_ratio=0.0,
        max_delay=None,
    )
    assert delay == expected_base


def test_exponential_backoff_caps_at_max_delay():
    delay = exponential_backoff_delay(
        10,
        base_delay=1.0,
        factor=2.0,
        jitter_ratio=0.0,
        max_delay=3.0,
    )
    assert delay == 3.0


def test_exponential_backoff_jitter_is_deterministic_with_rng():
    rng = random.Random(123)
    a = exponential_backoff_delay(2, base_delay=0.1, jitter_ratio=0.5, rng=rng)

    rng = random.Random(123)
    b = exponential_backoff_delay(2, base_delay=0.1, jitter_ratio=0.5, rng=rng)

    assert a == b


@pytest.mark.parametrize("bad_attempt", [-1, -5])
def test_exponential_backoff_rejects_negative_attempt(bad_attempt):
    with pytest.raises(ValueError):
        exponential_backoff_delay(bad_attempt)
