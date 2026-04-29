from __future__ import annotations

import random


def exponential_backoff_delay(
    attempt: int,
    *,
    base_delay: float = 0.1,
    factor: float = 2.0,
    jitter_ratio: float = 0.1,
    max_delay: float | None = 60.0,
    rng: random.Random | None = None,
) -> float:
    if attempt < 0:
        raise ValueError("attempt must be >= 0")
    if base_delay < 0:
        raise ValueError("base_delay must be >= 0")
    if factor < 1:
        raise ValueError("factor must be >= 1")
    if jitter_ratio < 0:
        raise ValueError("jitter_ratio must be >= 0")
    if max_delay is not None and max_delay < 0:
        raise ValueError("max_delay must be >= 0")

    raw_delay = base_delay * (factor**attempt)
    if max_delay is not None:
        raw_delay = min(raw_delay, max_delay)

    if jitter_ratio == 0 or raw_delay == 0:
        return float(raw_delay)

    local_rng = rng or random
    jitter_amount = raw_delay * jitter_ratio
    jitter = local_rng.uniform(-jitter_amount, jitter_amount)
    return max(0.0, float(raw_delay + jitter))
