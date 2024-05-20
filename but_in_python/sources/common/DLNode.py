from typing import Optional


class DLNode:
    value = Optional[object]
    next: Optional[object]
    previous: Optional[object]

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)