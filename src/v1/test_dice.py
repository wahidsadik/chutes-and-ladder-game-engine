import unittest
from v1.dice import Dice

ITERATIONS = 10000


class TestDice(unittest.TestCase):

    def test_roll(self):
        dice = Dice()

        for i in range(0, ITERATIONS):
            with self.subTest(i=i):
                roll = dice.roll()
                self.assertGreaterEqual(roll, 1)
                self.assertLessEqual(roll, 6)
