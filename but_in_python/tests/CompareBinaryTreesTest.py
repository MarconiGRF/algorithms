import unittest

from but_in_python.sources.CompareBinaryTrees import compare
from but_in_python.tests.auxiliary.tree import get_test_tree_1, get_test_tree_2


class CompareBinaryTreesTest(unittest.TestCase):
    tree = get_test_tree_1()
    tree_2 = get_test_tree_2()

    def test_tree_comparison(self):
        self.assertEqual(compare(self.tree, self.tree_2), False)


if __name__ == '__main__':
    unittest.main()