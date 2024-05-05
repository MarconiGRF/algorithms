import unittest

from but_in_python.sources.ArrayList import ArrayList


class ArrayListTest(unittest.TestCase):

    def test_array_list(self):
        array_list = ArrayList()

        array_list.append(5)
        array_list.append(7)
        array_list.append(9)

        self.assertEqual(array_list.get(2), 9)
        self.assertEqual(array_list.remove_at(1), 7)
        self.assertEqual(len(array_list), 2)

        array_list.append(11)
        self.assertEqual(array_list.remove_at(1), 9)
        self.assertEqual(array_list.remove(9), None)
        self.assertEqual(array_list.remove_at(0), 5)
        self.assertEqual(array_list.remove_at(0), 11)
        self.assertEqual(len(array_list), 0)

        array_list.prepend(5)
        array_list.prepend(7)
        array_list.prepend(9)

        self.assertEqual(array_list.get(2), 5)
        self.assertEqual(array_list.get(0), 9)
        self.assertEqual(array_list.remove(9), 9)
        self.assertEqual(len(array_list), 2)
        self.assertEqual(array_list.get(0), 7)


if __name__ == '__main__':
    unittest.main()
