import pytest

from rate_limiter import TokenBucket


def test_token_bucket_initial_capacity_allows_consumption():
    bucket = TokenBucket(capacity=5, refill_rate=1, now=0)
    assert bucket.consume(1, now=0) is True
    assert bucket.consume(4, now=0) is True
    assert bucket.consume(1, now=0) is False


def test_token_bucket_refills_over_time():
    bucket = TokenBucket(capacity=2, refill_rate=1, now=0)
    assert bucket.consume(2, now=0) is True
    assert bucket.consume(1, now=0) is False

    assert bucket.consume(1, now=1) is True
    assert bucket.consume(1, now=1) is False


@pytest.mark.parametrize("tokens", [0, -1])
def test_token_bucket_rejects_non_positive_tokens(tokens):
    bucket = TokenBucket(capacity=1, refill_rate=1, now=0)
    with pytest.raises(ValueError):
        bucket.consume(tokens, now=0)
