from collections import deque

class Queue:
    """A FIFO queue implementation using deque for O(1) operations."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item) -> None:
        """Add item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return item from the front."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)