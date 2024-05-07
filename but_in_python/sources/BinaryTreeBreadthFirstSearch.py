from but_in_python.sources.common.BinaryNode import BinaryNode


def bfs(head: BinaryNode, needle: int) -> bool:
    processing_queue = [head]

    while len(processing_queue) != 0:
        current = processing_queue.pop(0)
        if current.value == needle:
            return True
        else:
            processing_queue.append(current.left) if current.left else None
            processing_queue.append(current.right) if current.right else None

    return False