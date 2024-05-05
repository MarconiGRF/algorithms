from typing import Optional
from array import array


class ArrayList:

    def __init__(self, capacity=5):
        self.length = 0
        self.capacity = capacity
        self.array = array('i', [0] * self.capacity)

    def __len__(self):
        return self.length

    def prepend(self, value: int) -> None:
        if self.length + 1 > self.capacity:
            self.__double_array_size()

        if self.length != 0:
            self.__shift('r', 0)
        self.array[0] = value
        self.length += 1

    def __double_array_size(self):
        self.capacity = self.capacity * 2
        old_array = self.array

        self.array = array('i', [0] * self.capacity)
        for i in range(len(old_array)):
            self.array.insert(i, old_array[i])

        del old_array


    def __shift(self, direction, idx):
        if direction == 'r':
            i = len(self.array) - 1
            while i > idx:
                self.array[i] = self.array[i - 1]
                i -= 1
        else:
            i = idx
            while i < self.length - 1:
                self.array[i] = self.array[i + 1]
                i += 1

    def insert_at(self, value: int, idx) -> None:
        self.array[idx] = value
        self.length += 1

    def append(self, value: int) -> None:
        if self.length + 1 > self.capacity:
            self.__double_array_size()

        self.array[self.length] = value
        self.length += 1

    def remove(self, value: int) -> Optional[object]:
        removal_index = -1
        for i in range(self.length):
            if self.array[i] == value:
                removal_index = i
                break
        if removal_index == -1:
            return None
        else:
            return self.remove_at(removal_index)

    def get(self, idx) -> Optional[object]:
        if idx >= self.length:
            return None
        return self.array[idx]

    def remove_at(self, idx) -> Optional[object]:
        returnable = None

        if idx >= self.length:
            return None
        elif idx != self.length - 1:
            returnable = self.array[idx]
            self.__shift('l', idx)
        else:
            returnable = self.array[idx]

        self.length -= 1
        return returnable