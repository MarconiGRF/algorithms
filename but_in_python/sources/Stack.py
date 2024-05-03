from typing import Optional

class SNode:
    value = Optional[object]
    previous: Optional[object]

    def __init__(self, value):
        self.value = value
        self.previous = None


class Stack:
    length: int
    head: Optional[SNode]

    def __init__(self):
        self.length = 0
        self.head = None

    def __len__(self):
        return self.length

    def push(self, value):
        if self.length == 0:
            self.head = SNode(value)
        else:
            new_head = SNode(value)
            new_head.previous = self.head
            self.head = new_head
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        old_head = self.head
        self.head = self.head.previous
        old_head.previous = None

        self.length -= 1
        return old_head.value

    def peek(self):
        return self.head.value if self.head else None