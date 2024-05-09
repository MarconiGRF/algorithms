import unittest

from but_in_python.sources.BreadthFirstSearchGraphMatrix import bfs
from but_in_python.tests.auxiliary.graph import get_test_matrix_2


class BreadthFirstSearchGraphMatrixTest(unittest.TestCase):

    def test_bfs_on_graph_matrix(self):
        matrix = get_test_matrix_2()
        self.assertEqual(bfs(matrix, 0, 6), [
            0,
            1,
            4,
            5,
            6
        ])


if __name__ == '__main__':
    unittest.main()