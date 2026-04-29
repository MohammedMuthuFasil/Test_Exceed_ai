from __future__ import annotations

import time
from collections.abc import Callable


def call_with_retry(
    func: Callable[[], object],
    *,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
    max_attempts: int = 3,
    delay_provider: Callable[[int], float] | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> object:
    if max_attempts < 1:
        raise ValueError("max_attempts must be >= 1")

    attempt = 0
    while True:
        try:
            return func()
        except exceptions:
            attempt += 1
            if attempt >= max_attempts:
                raise

            if delay_provider is not None:
                delay = float(delay_provider(attempt))
                if delay > 0:
                    sleep(delay)
