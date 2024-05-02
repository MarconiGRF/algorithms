import unittest

from but_in_python.sources.LinearSearchList import linear_search_list


class LinearSearchListTest(unittest.TestCase):
    test_values = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

    def test_present_values(self):
        self.assertEqual(linear_search_list(self.test_values, 69), True)
        self.assertEqual(linear_search_list(self.test_values, 69420), True)
        self.assertEqual(linear_search_list(self.test_values, 1), True)
    def test_absent_values(self):
        self.assertEqual(linear_search_list(self.test_values, 1336), False)
        self.assertEqual(linear_search_list(self.test_values, 69421), False)
        self.assertEqual(linear_search_list(self.test_values, 0), False)


if __name__ == '__main__':
    unittest.main()
