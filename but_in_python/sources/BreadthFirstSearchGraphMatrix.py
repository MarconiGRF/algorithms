from typing import List, Optional


def bfs(graph: List[List[int]], source: int, target: int) -> Optional[List[int]]:
    path_history = [-1] * len(graph[0])
    visited = [False] * (len(graph[0]))

    processing_queue = [source]
    visited[0] = True

    while len(processing_queue) > 0:
        current = processing_queue.pop(0)
        if current == target:
            break

        adjacents_of_current = graph[current]
        i = 0
        while i < len(adjacents_of_current):
            if adjacents_of_current[i] == 0:
                i += 1
                continue
            if visited[i]:
                i += 1
                continue
            else:
                visited[i] = True
                path_history[i] = current
                processing_queue.append(i)
                i += 1

    if path_history[target] == -1:
        return []

    current = target
    final_path = []

    while path_history[current] != -1:
        final_path.append(current)
        current = path_history[current]

    if len(final_path) > 0:
        final_path.reverse()
        final_path.insert(0, source)
        return final_path