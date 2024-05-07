import unittest

from but_in_python.sources.BinaryTreeTraversalPostOrder import post_order_search
from but_in_python.tests.auxiliary.tree import get_test_tree_1


class BinaryTreeTraversalPostOrderTest(unittest.TestCase):
    tree = get_test_tree_1()

    def test_post_order_traversal(self):
        self.assertEqual(post_order_search(self.tree), [
            7,
            5,
            15,
            10,
            29,
            45,
            30,
            100,
            50,
            20,
        ])


if __name__ == '__main__':
    unittest.main()