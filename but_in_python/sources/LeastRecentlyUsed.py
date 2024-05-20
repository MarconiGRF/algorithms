from typing import Optional, Dict

from but_in_python.sources.common.DLNode import DLNode


class LRU:
    length: int
    capacity: int
    head: Optional[DLNode.value]
    tail: Optional[DLNode.value]
    _lookup: Dict[str, DLNode.value]
    _reverse_lookup: Dict[DLNode.value, str]

    def __init__(self, capacity: int=10):
        self.length = 0
        self.capacity = capacity
        self.head = self.tail = None
        self._lookup = {}
        self._reverse_lookup = {}

    def update(self, key: str, value: object) -> None:
        # does it exist? call get()

        if not key in self._lookup:
            # If it doesnt, insert
            node = DLNode(value)
            self.length += 1
            self._prepend(node)
            self._update_cache()

            self._lookup[key] = node
            self._reverse_lookup[id(node)] = key
            node.value = value
        else:
            node = self._lookup[key]
            self.detach(node)
            self._prepend(node)

        # Check capacity and evict if over capacity
        # If it does, update the value and put it in the front of list

        pass

    def _update_cache(self):
        if self.length <= self.capacity:
            return

        tail = self.tail
        self._detach(tail)

        key = self._reverse_lookup[id(tail)]
        self._lookup.pop(key)
        self._reverse_lookup.pop(id(tail))
        self.length -= 1

    def _detach(self, node: DLNode) -> None:
        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous

        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.previous

        node.next = None
        node.previous = None

    def _prepend(self, node: DLNode) -> None:
        if self.head is None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.previous = node
        self.head = node

    def get(self, key: str) -> Optional[object]:
        # Check the cache for existence

        if not key in self._lookup:
            return None
        else:
            # If it exists, update the value and move it to the front, then return
            node = self._lookup[key]
            self._detach(node)
            self._prepend(node)

        return node.value