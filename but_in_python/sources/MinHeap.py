import math
from typing import List, Optional


class MinHeap:
    length: int
    data: List[int]

    def __init__(self):
        self.length = 0
        self.data = []

    def _swap(self, origin: int, destination: int) -> None:
        tmp = self.data[destination]
        self.data[destination] = self.data[origin]
        self.data[origin] = tmp

    @staticmethod
    def _get_right(index: int) -> int:
        return (2 * index) + 2

    @staticmethod
    def _get_left(index: int) -> int:
        return (2 * index) + 1

    @staticmethod
    def _get_parent(index: int) -> int:
        return math.floor((index - 1) / 2)

    def _heapify_up(self, index):
        if index == 0:
            return

        parent_index = self._get_parent(index)
        if self.data[parent_index] > self.data[index]:
            self._swap(parent_index, index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index) -> None:
        right_index = self._get_right(index)
        left_index = self._get_left(index)
        if index >= self.length or right_index >= self.length or left_index >= self.length:
            return

        if (self.data[right_index] < self.data[left_index]) and (self.data[index] > self.data[right_index]):
            self._swap(index, right_index)
            self._heapify_down(right_index)
        elif (self.data[left_index] < self.data[right_index]) and (self.data[index] > self.data[left_index]):
            self._swap(index, left_index)
            self._heapify_down(left_index)


    def insert(self, value: int) -> None:
        self.data.append(value)
        self._heapify_up(self.length)
        self.length += 1

    def delete(self) -> Optional[int]:
        if self.length == 0:
            return None

        head = self.data[0]
        self.length -= 1

        if self.length == 0:
            self.data = []
        else:
            self.data[0] = self.data[self.length]
            self._heapify_down(0)

        return head
