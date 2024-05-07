from typing import List


class BinaryNode:
    def __init__(self, value: int, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

def traverse(current: BinaryNode, results: List[int]) -> None:
    # Base Case
    if current is None:
        return

    # Pre recursion
    # Recurse
    traverse(current.left, results)
    traverse(current.right, results)

    # Post recursion
    results.append(current.value)


def post_order_search(head: BinaryNode) -> List[int]:
    path = []
    traverse(head, path)

    return path
