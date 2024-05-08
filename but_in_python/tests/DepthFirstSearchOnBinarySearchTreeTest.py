import unittest

from but_in_python.sources.DepthFirstSearchOnBinarySearchTree import dfs
from but_in_python.tests.auxiliary.tree import get_test_tree_1

class DepthFirstSearchOnBinarySearchTreeTest(unittest.TestCase):
    tree = get_test_tree_1

    def test_dfs_on_bst(self):
        self.assertEqual(dfs(self.tree, 45), True)
        self.assertEqual(dfs(self.tree, 7), True)
        self.assertEqual(dfs(self.tree, 69), False)

if __name__ == '__main__':
    unittest.main()