from __future__ import annotations


class TokenBucket:
    def __init__(self, *, capacity: float, refill_rate: float, now: float = 0.0):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        if refill_rate <= 0:
            raise ValueError("refill_rate must be > 0")

        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate)
        self.tokens = float(capacity)
        self.last_updated = float(now)

    def _refill(self, now: float) -> None:
        now = float(now)
        elapsed = max(0.0, now - self.last_updated)
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_updated = now

    def can_consume(self, tokens: float = 1.0, *, now: float) -> bool:
        if tokens <= 0:
            raise ValueError("tokens must be > 0")

        self._refill(now)
        return self.tokens >= float(tokens)

    def consume(self, tokens: float = 1.0, *, now: float) -> bool:
        if not self.can_consume(tokens, now=now):
            return False
        self.tokens -= float(tokens)
        return True
