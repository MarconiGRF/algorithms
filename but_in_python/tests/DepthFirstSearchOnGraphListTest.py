import unittest

from but_in_python.sources.DepthFirstSearchOnGraphList import dfs
from but_in_python.tests.auxiliary.graph import get_test_list_2


class DepthFirstSearchOnGraphListTest(unittest.TestCase):

    def test_dfs_on_graph_list(self):
        graph = get_test_list_2()
        self.assertEqual(dfs(graph, 0, 6), [
            0,
            1,
            4,
            5,
            6
        ])
        self.assertEqual(dfs(graph, 6, 0), None)

if __name__ == '__main__':
    unittest.main()