from typing import Optional

class QNode:
    value = object | None
    next: Optional[None]

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    length: int
    head: Optional[QNode]
    tail: Optional[QNode]

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def enqueue(self, value):
        if self.length == 0:
            self.head = QNode(value)
            self.tail = self.head
        else:
            new_tail = QNode(value)
            self.tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def deque(self):
        if self.length == 0:
            return None

        old_head = self.head
        self.head = old_head.next
        old_head.next = None

        self.length -= 1
        if self.length == 0:
            self.tail = None

        return old_head.value

    def peek(self):
        return self.head.value if self.head else None