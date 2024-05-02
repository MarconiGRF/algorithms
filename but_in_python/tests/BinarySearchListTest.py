import unittest

from but_in_python.sources.BinarySearchList import bs_list


class BinarySearchListTest(unittest.TestCase):
    test_values = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

    def test_present_values(self):
        self.assertEqual(bs_list(self.test_values, 69), True)
        self.assertEqual(bs_list(self.test_values, 69420), True)
        self.assertEqual(bs_list(self.test_values, 1), True)
    def test_absent_values(self):
        self.assertEqual(bs_list(self.test_values, 1336), False)
        self.assertEqual(bs_list(self.test_values, 69421), False)
        self.assertEqual(bs_list(self.test_values, 0), False)


if __name__ == '__main__':
    unittest.main()
