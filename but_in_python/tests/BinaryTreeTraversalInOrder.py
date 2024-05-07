import unittest

from but_in_python.sources.BinaryTreeTraversalInOrder import in_order_search
from but_in_python.tests.auxiliary.tree import get_test_tree_1


class BinaryTreeTraversalInOrderTest(unittest.TestCase):
    tree = get_test_tree_1()

    def test_in_order_traversal(self):
        self.assertEqual(in_order_search(self.tree), [
            5,
            7,
            10,
            15,
            20,
            29,
            30,
            45,
            50,
            100
        ])


if __name__ == '__main__':
    unittest.main()