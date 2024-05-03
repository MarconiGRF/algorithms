import unittest

from but_in_python.sources.Queue import Queue


class QueueTest(unittest.TestCase):

    def test_queue(self):
        queue = Queue()

        queue.enqueue(5)
        queue.enqueue(7)
        queue.enqueue(9)

        self.assertEqual(queue.deque(), 5)
        self.assertEqual(queue.length, 2)
        self.assertEqual(len(queue), 2)

        queue.enqueue(11)
        self.assertEqual(queue.deque(), 7)
        self.assertEqual(queue.deque(), 9)
        self.assertEqual(queue.peek(), 11)
        self.assertEqual(queue.deque(), 11)
        self.assertEqual(queue.deque(), None)

        queue.enqueue(69)
        self.assertEqual(queue.peek(), 69)
        self.assertEqual(queue.length, 1)
        self.assertEqual(len(queue), 1)


if __name__ == '__main__':
    unittest.main()
