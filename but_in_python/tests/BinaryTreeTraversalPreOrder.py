import unittest

from but_in_python.sources.BinaryTreeTraversalPreOrder import pre_order_search
from but_in_python.tests.auxiliary.tree import get_test_tree_1


class BinaryTreeTraversalPreOrderTest(unittest.TestCase):
    tree = get_test_tree_1()

    def test_pre_order_traversal(self):
        self.assertEqual(pre_order_search(self.tree), [
            20,
            10,
            5,
            7,
            15,
            50,
            30,
            29,
            45,
            100
        ])


if __name__ == '__main__':
    unittest.main()