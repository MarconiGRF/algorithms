import unittest

from but_in_python.sources.LeastRecentlyUsed import LRU


class LeastRecentlyUsedTest(unittest.TestCase):

    def test_lru(self):
        lru = LRU(3)
        self.assertEqual(lru.get("foo"), None)
        lru.update("foo", 69)
        self.assertEqual(lru.get("foo"), 69)

        lru.update("bar", 420)
        self.assertEqual(lru.get("bar"), 420)

        lru.update("baz", 1337)
        self.assertEqual(lru.get("baz"), 1337)

        lru.update("ball", 69420)
        self.assertEqual(lru.get("ball"), 69420)
        self.assertEqual(lru.get("foo"), None)
        self.assertEqual(lru.get("bar"), 420)
        lru.update("foo", 69)
        self.assertEqual(lru.get("bar"), 420)
        self.assertEqual(lru.get("foo"), 69)

        self.assertEqual(lru.get("baz"), None)
if __name__ == '__main__':
    unittest.main()
