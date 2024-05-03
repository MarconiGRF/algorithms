import unittest

from but_in_python.sources.Stack import Stack


class StackTest(unittest.TestCase):

    def test_stack(self):
        stack = Stack()

        stack.push(5)
        stack.push(7)
        stack.push(9)

        self.assertEqual(stack.pop(), 9)
        self.assertEqual(stack.length, 2)
        self.assertEqual(len(stack), 2)

        stack.push(11)
        self.assertEqual(stack.pop(), 11)
        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), None)

        stack.push(69)
        self.assertEqual(stack.peek(), 69)
        self.assertEqual(stack.length, 1)
        self.assertEqual(len(stack), 1)


if __name__ == '__main__':
    unittest.main()
