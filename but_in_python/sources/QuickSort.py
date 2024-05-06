from typing import List


def swap(values: List[int], origin_index: int, destination_index: int) -> None:
    tmp = values[destination_index]
    values[destination_index] = values[origin_index]
    values[origin_index] = tmp

def partition(values: List[int], low: int, high: int) -> int:
    pivot_itself = values[high]

    insertion_index = low - 1
    walking_index = low
    while walking_index < high:
        if values[walking_index] <= pivot_itself:
            insertion_index += 1
            swap(values, walking_index, insertion_index)
        walking_index += 1

    insertion_index += 1
    swap(values, insertion_index, high)

    return insertion_index

def qs(values: List[int], low: int, high: int) -> None:
    if (high - low) < 1:
        return

    pivot_index = partition(values, low, high)

    # Sort left side
    qs(values, low, pivot_index - 1)

    # Sort right side
    qs(values, pivot_index + 1, high)


def quick_sort(values: List[int]) -> None:
    qs(values, 0, len(values) - 1)
