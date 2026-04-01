"""Linked List Tests.

Tests for the LinkedList implementation in linked_list.py.
Also extends the LinkedList with additional operations:
prepend, delete, search, reverse, and length.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from linked_list import Node, LinkedList


# -- Extended LinkedList for testing additional operations --

class ExtendedLinkedList(LinkedList):
    """Extends the base LinkedList with more operations."""

    def prepend(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Remove the first node containing the given data."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """Return True if data exists in the list, False otherwise."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# -- Tests for base LinkedList --

def test_linked_list_append_single():
    ll = LinkedList()
    ll.append(10)
    assert ll.display() == [10]


def test_linked_list_append_multiple():
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    assert ll.display() == [1, 2, 3, 4, 5]


def test_linked_list_empty_display():
    ll = LinkedList()
    assert ll.display() == []


def test_linked_list_append_preserves_order():
    ll = LinkedList()
    ll.append(100)
    ll.append(200)
    ll.append(300)
    assert ll.display() == [100, 200, 300]


# -- Tests for extended operations --

def test_prepend_to_empty_list():
    ll = ExtendedLinkedList()
    ll.prepend(5)
    assert ll.display() == [5]


def test_prepend_adds_to_front():
    ll = ExtendedLinkedList()
    ll.append(2)
    ll.append(3)
    ll.prepend(1)
    assert ll.display() == [1, 2, 3]


def test_prepend_multiple():
    ll = ExtendedLinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert ll.display() == [1, 2, 3]


def test_delete_head_node():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.delete(1)
    assert ll.display() == [2, 3]


def test_delete_middle_node():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.delete(2)
    assert ll.display() == [1, 3]


def test_delete_tail_node():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.delete(3)
    assert ll.display() == [1, 2]


def test_delete_non_existent_value():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.delete(99)
    assert ll.display() == [1, 2, 3]


def test_delete_from_empty_list():
    ll = ExtendedLinkedList()
    ll.delete(1)
    assert ll.display() == []


def test_search_existing_value():
    ll = ExtendedLinkedList()
    for v in [10, 20, 30]:
        ll.append(v)
    assert ll.search(20) is True


def test_search_missing_value():
    ll = ExtendedLinkedList()
    for v in [10, 20, 30]:
        ll.append(v)
    assert ll.search(99) is False


def test_search_empty_list():
    ll = ExtendedLinkedList()
    assert ll.search(1) is False


def test_length_empty():
    ll = ExtendedLinkedList()
    assert ll.length() == 0


def test_length_after_appends():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
    assert ll.length() == 5


def test_length_after_delete():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.delete(2)
    assert ll.length() == 2


def test_reverse_list():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
    ll.reverse()
    assert ll.display() == [5, 4, 3, 2, 1]


def test_reverse_single_element():
    ll = ExtendedLinkedList()
    ll.append(42)
    ll.reverse()
    assert ll.display() == [42]


def test_reverse_empty_list():
    ll = ExtendedLinkedList()
    ll.reverse()
    assert ll.display() == []


def test_reverse_twice_gives_original():
    ll = ExtendedLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.reverse()
    ll.reverse()
    assert ll.display() == [1, 2, 3]
