import unittest

from but_in_python.sources.MazeSolver import MazeSolver, MazePoint


class MazeSolverTest(unittest.TestCase):

    def test_maze_solver(self):
        maze = [
            "XXXXXXXXXX X",
            "X        X X",
            "X        X X",
            "X XXXXXXXX X",
            "X          X",
            "X XXXXXXXXXX"
        ]

        solver = MazeSolver()
        result = solver.solve(maze, "X", MazePoint(10, 0), MazePoint(1, 5))

        self.assertEqual(
            solver.solve(maze, "X", MazePoint(10, 0), MazePoint(1, 5)),
            [
                MazePoint(10, 0),
                MazePoint(10, 1),
                MazePoint(10, 2),
                MazePoint(10, 3),
                MazePoint(10, 4),
                MazePoint(9, 4),
                MazePoint(8, 4),
                MazePoint(7, 4),
                MazePoint(6, 4),
                MazePoint(5, 4),
                MazePoint(4, 4),
                MazePoint(3, 4),
                MazePoint(2, 4),
                MazePoint(1, 4),
                MazePoint(1, 5)
            ]
        )

if __name__ == '__main__':
    unittest.main()