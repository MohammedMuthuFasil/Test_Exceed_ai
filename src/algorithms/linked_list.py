class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list implementation."""
    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self) -> list:
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.display())