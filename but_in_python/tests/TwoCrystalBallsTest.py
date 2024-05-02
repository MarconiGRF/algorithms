import random
import math
import unittest

from but_in_python.sources.TwoCrystalBalls import two_crystal_balls


class TwoCrystalBallsTest(unittest.TestCase):

    @staticmethod
    def data_setup():
        data_limit = 10000
        index = math.floor(random.random() * data_limit)
        data = [False for _ in range(data_limit)]

        i = index
        while i < data_limit:
            data[i] = True
            i += 1
        return data, index

    def test_all_breaks(self):
        self.assertEqual(two_crystal_balls([False for _ in range(821)]), -1)

    def test_breakable(self):
        data, index = self.data_setup()
        self.assertEqual(two_crystal_balls(data), index)


if __name__ == '__main__':
    unittest.main()
