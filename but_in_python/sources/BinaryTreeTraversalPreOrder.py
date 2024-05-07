from typing import List

from but_in_python.sources.common.BinaryNode import BinaryNode


def traverse(current: BinaryNode, results: List[int]) -> None:
    # Base Case
    if current is None:
        return

    # Pre recursion
    results.append(current.value)

    # Recurse
    traverse(current.left, results)
    traverse(current.right, results)

    # Post recursion
    # Nothing to do!


def pre_order_search(head: BinaryNode) -> List[int]:
    path = []
    traverse(head, path)

    return path