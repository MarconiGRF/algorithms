import unittest

from but_in_python.sources.BinaryTreeBreadthFirstSearch import bfs
from but_in_python.tests.auxiliary.tree import get_test_tree_1


class BinaryTreeBreadthFirstSearchTest(unittest.TestCase):
    tree = get_test_tree_1()

    def test_bfs(self):
        self.assertEqual(bfs(self.tree, 45), True)
        self.assertEqual(bfs(self.tree, 7), True)
        self.assertEqual(bfs(self.tree, 69), False)


if __name__ == '__main__':
    unittest.main()