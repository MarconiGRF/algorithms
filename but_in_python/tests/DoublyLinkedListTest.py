import unittest

from but_in_python.sources.DoublyLinkedList import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):

    def test_doubly_linked_list(self):
        dl_list = DoublyLinkedList()

        dl_list.append(5)
        dl_list.append(7)
        dl_list.append(9)

        self.assertEqual(dl_list.get(2), 9)
        self.assertEqual(dl_list.remove_at(1), 7)
        self.assertEqual(len(dl_list), 2)

        dl_list.append(11)
        self.assertEqual(dl_list.remove_at(1), 9)
        self.assertEqual(dl_list.remove(9), None)
        self.assertEqual(dl_list.remove_at(0), 5)
        self.assertEqual(dl_list.remove_at(0), 11)
        self.assertEqual(len(dl_list), 0)

        dl_list.prepend(5)
        dl_list.prepend(7)
        dl_list.prepend(9)

        self.assertEqual(dl_list.get(2), 5)
        self.assertEqual(dl_list.get(0), 9)
        self.assertEqual(dl_list.remove(9), 9)
        self.assertEqual(len(dl_list), 2)
        self.assertEqual(dl_list.get(0), 7)


if __name__ == '__main__':
    unittest.main()
