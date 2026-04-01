"""Stack and Queue Data Structures.

Implementations and tests for Stack (LIFO) and Queue (FIFO)
data structures built from scratch in Python.
"""

import pytest


class Stack:
    """A Last-In-First-Out (LIFO) data structure.

    Supports push, pop, peek, is_empty, and size operations.
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item onto the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)


class Queue:
    """A First-In-First-Out (FIFO) data structure.

    Supports enqueue, dequeue, peek, is_empty, and size operations.
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        """Return the front item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """Return True if the queue contains no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)


def is_balanced_parentheses(expression):
    """Check whether parentheses/brackets/braces in an expression are balanced.

    Uses a stack to track opening symbols and match them with closing ones.
    Returns True if balanced, False otherwise.
    """
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != matching[char]:
                return False
    return stack.is_empty()


# -- Stack Tests --

def test_stack_push_and_peek():
    s = Stack()
    s.push(1)
    assert s.peek() == 1


def test_stack_push_multiple_peek_returns_last():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3


def test_stack_pop_returns_last_pushed():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20


def test_stack_pop_decreases_size():
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    assert s.size() == 1


def test_stack_is_empty_on_new_stack():
    assert Stack().is_empty() is True


def test_stack_is_not_empty_after_push():
    s = Stack()
    s.push(99)
    assert s.is_empty() is False


def test_stack_is_empty_after_all_pops():
    s = Stack()
    s.push(1)
    s.pop()
    assert s.is_empty() is True


def test_stack_size():
    s = Stack()
    for i in range(5):
        s.push(i)
    assert s.size() == 5


def test_stack_pop_empty_raises():
    with pytest.raises(IndexError):
        Stack().pop()


def test_stack_peek_empty_raises():
    with pytest.raises(IndexError):
        Stack().peek()


def test_stack_lifo_order():
    s = Stack()
    for val in [1, 2, 3, 4, 5]:
        s.push(val)
    result = [s.pop() for _ in range(5)]
    assert result == [5, 4, 3, 2, 1]


# -- Queue Tests --

def test_queue_enqueue_and_peek():
    q = Queue()
    q.enqueue("first")
    assert q.peek() == "first"


def test_queue_fifo_order():
    q = Queue()
    for val in [1, 2, 3]:
        q.enqueue(val)
    result = [q.dequeue() for _ in range(3)]
    assert result == [1, 2, 3]


def test_queue_dequeue_returns_front():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"


def test_queue_dequeue_reduces_size():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    assert q.size() == 1


def test_queue_is_empty_on_new_queue():
    assert Queue().is_empty() is True


def test_queue_is_not_empty_after_enqueue():
    q = Queue()
    q.enqueue(42)
    assert q.is_empty() is False


def test_queue_is_empty_after_all_dequeues():
    q = Queue()
    q.enqueue(1)
    q.dequeue()
    assert q.is_empty() is True


def test_queue_size():
    q = Queue()
    for i in range(4):
        q.enqueue(i)
    assert q.size() == 4


def test_queue_dequeue_empty_raises():
    with pytest.raises(IndexError):
        Queue().dequeue()


def test_queue_peek_empty_raises():
    with pytest.raises(IndexError):
        Queue().peek()


# -- Balanced Parentheses Tests --

def test_balanced_simple_parens():
    assert is_balanced_parentheses("()") is True


def test_balanced_nested():
    assert is_balanced_parentheses("({[]})") is True


def test_balanced_complex_expression():
    assert is_balanced_parentheses("[(a + b) * (c - d)]") is True


def test_unbalanced_missing_closing():
    assert is_balanced_parentheses("(()") is False


def test_unbalanced_wrong_order():
    assert is_balanced_parentheses(")(") is False


def test_unbalanced_mismatched():
    assert is_balanced_parentheses("({)}") is False


def test_balanced_empty_string():
    assert is_balanced_parentheses("") is True


def test_balanced_no_brackets():
    assert is_balanced_parentheses("hello world") is True
