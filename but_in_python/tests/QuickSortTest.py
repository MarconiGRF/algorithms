import unittest

from but_in_python.sources.QuickSort import quick_sort


class QuickSortTest(unittest.TestCase):

    def test_quick_sort(self):
        array = [9,3,7,4,69,420,42]

        quick_sort(array)
        self.assertEqual(array, [3, 4, 7, 9, 42, 69, 420])

if __name__ == '__main__':
    unittest.main()