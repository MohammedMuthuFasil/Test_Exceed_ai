class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()  # bug: crashes on empty stack

    def peek(self):
        return self.items[-1]  # bug: crashes on empty stack

    def is_empty(self):
        return len(self.items) == 0