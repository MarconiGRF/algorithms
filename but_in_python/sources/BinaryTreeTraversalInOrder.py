from typing import List

from but_in_python.sources.common.BinaryNode import BinaryNode


def traverse(current: BinaryNode, results: List[int]) -> None:
    # Base Case
    if current is None:
        return

    # Pre recursion
    traverse(current.left, results)

    # Recurse
    results.append(current.value)

    # Post recursion
    traverse(current.right, results)


def in_order_search(head: BinaryNode) -> List[int]:
    path = []
    traverse(head, path)

    return path