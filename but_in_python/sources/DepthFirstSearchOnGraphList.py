from typing import List, Optional


def walk(graph: List[List[object]], current: int, needle: int, seen: List[bool], path: List[int]) -> bool:
    # Base Case
    if seen[current]:
        return False

    # Pre
    seen[current] = True
    path.append(current)
    if current == needle:
        return True

    # Recurse
    adjacents_list = graph[current]
    for i in range(len(adjacents_list)):
        connection = adjacents_list[i]

        if walk(graph, connection['to'], needle, seen, path):
            return True

    # Post
    path.pop()
    return False

def dfs(graph: List[List[object]], source: int, needle: int) -> Optional[int]:
    path = []
    walk(graph, source, needle, [False] * len(graph), path)

    return path if len(path) > 0 else None