from but_in_python.sources.common.BinaryNode import BinaryNode

def search(current: BinaryNode, needle: int) -> bool:
    print(f'Current node is {current}')
    # Base cases
    if current is None:
        return False
    
    if current.value == needle:
        return True

    # Recurse
    if needle < current.value:
        return search(current.left, needle)
    else:
        return search(current.right, needle)

def dfs(head: BinaryNode, needle: int) -> bool:
    return search(head, needle)
