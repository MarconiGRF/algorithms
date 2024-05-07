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


class DoublyLinkedList:
    length: int
    head: Optional[DLNode]
    tail: Optional[DLNode]

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def prepend(self, value: int) -> None:
        new_node = DLNode(value)

        if self.length == 0:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node

        self.head = new_node
        self.length += 1


    def insert_at(self, value: int, idx) -> None:
        if idx > self.length:
            raise EnvironmentError("Can't add value above existing length")
        elif idx == 0:
            self.prepend(value)
            return
        elif idx == self.length:
            self.append(value)
            return

        i = 0
        current = self.head
        while i < self.length - 1 and current is not None:
            if i == idx:
                new_node = DLNode(value)
                new_node.next = current
                new_node.previous = current.previous

                new_node.previous.next = current
                new_node.next.previous = current
                self.length += 1
            else:
                current = current.next
                i += 1

    def append(self, value: int) -> None:
        new_node = DLNode(value)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

    def get(self, idx) -> Optional[object]:
        if idx >= self.length:
            return None

        current = self.head
        i = 0
        while i < idx:
            current = current.next
            i += 1

        return current.value

    def _remove_and_unlink(self, current: DLNode, i) -> int:
        if i == 0:
            self.head = current.next
            self.head.previous = None
        elif i == self.length - 1:
            self.tail = current.previous
            self.tail.next = None
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

        returnable = current.value
        del current

        self.length -= 1
        return returnable

    def remove(self, value: int) -> Optional[int]:
        if self.length == 0:
            self.head = self.tail = None
            return None

        i = 0
        current = self.head
        while i < self.length - 1 and current is not None:
            if current.value == value:
                return self._remove_and_unlink(current, i)
            else:
                current = current.next
                i += 1

    def remove_at(self, idx) -> Optional[int]:
        if idx >= self.length or self.length == 0:
            self.head = self.tail = None
            return None

        if idx == 0:
            old_head = self.head
            self.head = self.head.next

            old_head.next = None

            self.length -= 1
            if self.length == 0:
                self.tail = None

            return old_head.value

        current = self.head
        i = 0
        while i < self.length - 1:
            if i == idx:
                return self._remove_and_unlink(current, i)
            else:
                current = current.next
                i += 1
