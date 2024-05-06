from typing import List


class MazePoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __str__(self):
        return f'X {self.x}, Y {self.y}'

class MazeSolver:

    DIR = {
        'TOP': [0, -1],
        'RIGHT': [1, 0],
        'LEFT': [-1, 0],
        'DOWN': [0, 1]
    }

    def __init__(self):
        pass

    def walk(self, maze: List[str], wall: str, end: MazePoint, current: MazePoint, seen: List[List[bool]], path: List[MazePoint]) -> bool:
        if (current.x < 0 or current.x >= len(maze[0])) or (current.y < 0 or current.y >= len(maze)):
            return False
        elif maze[current.y][current.x] == wall:
            return False
        elif current.y == end.y and current.x == end.x:
            path.append(end)
            return True
        elif seen[current.y][current.x]:
            return False

        # Pre
        seen[current.y][current.x] = True
        path.append(current)

        # Recurse
        if self.walk(maze, wall, end, MazePoint(current.x + self.DIR['TOP'][0],   current.y + self.DIR['TOP'][1]), seen, path):
            return True
        elif self.walk(maze, wall, end, MazePoint(current.x + self.DIR['RIGHT'][0], current.y + self.DIR['RIGHT'][1]), seen, path):
            return True
        elif self.walk(maze, wall, end, MazePoint(current.x + self.DIR['DOWN'][0],  current.y + self.DIR['DOWN'][1]), seen, path):
            return True
        elif self.walk(maze, wall, end, MazePoint(current.x + self.DIR['LEFT'][0],  current.y + self.DIR['LEFT'][1]), seen, path):
            return True

        # Post
        path.pop()

        return False

    def solve(self, maze: List[str], wall: str, start: MazePoint, end: MazePoint) -> List[MazePoint]:
        seen = []
        path = []

        i = 0
        while i < len(maze):
            seen.append( [False] * len(maze[0]) )
            i += 1

        self.walk(maze, wall, end, start,  seen, path)
        return path
