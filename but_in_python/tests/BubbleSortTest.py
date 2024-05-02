import unittest

from but_in_python.sources.BubbleSort import bubble_sort


class BubbleSortTest(unittest.TestCase):
    test_values = [9, 3, 7, 4, 69, 420, 42]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.test_values), [3, 4, 7, 9, 42, 69, 420])


if __name__ == '__main__':
    unittest.main()
