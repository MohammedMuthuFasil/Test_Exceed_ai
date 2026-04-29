import pytest

from retry import call_with_retry


def test_call_with_retry_succeeds_after_failures():
    state = {"calls": 0}

    def flaky():
        state["calls"] += 1
        if state["calls"] < 3:
            raise ValueError("temporary")
        return "ok"

    slept = []

    def fake_sleep(seconds):
        slept.append(seconds)

    def delay_provider(attempt):
        return 0.01 * attempt

    result = call_with_retry(
        flaky,
        exceptions=(ValueError,),
        max_attempts=5,
        delay_provider=delay_provider,
        sleep=fake_sleep,
    )

    assert result == "ok"
    assert state["calls"] == 3
    assert slept == [0.01, 0.02]


def test_call_with_retry_raises_after_max_attempts():
    def always_fails():
        raise RuntimeError("nope")

    with pytest.raises(RuntimeError):
        call_with_retry(always_fails, exceptions=(RuntimeError,), max_attempts=2)


def test_call_with_retry_validates_max_attempts():
    with pytest.raises(ValueError):
        call_with_retry(lambda: None, max_attempts=0)
