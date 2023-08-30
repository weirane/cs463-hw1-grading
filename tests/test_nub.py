import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import nub


class NubTests(unittest.TestCase):
    @weight(1.0)
    def test_nub_01(self):
        self.assertEqual(nub([]), [])

    @weight(1.0)
    def test_nub_02(self):
        self.assertEqual(nub([5]), [5])

    @weight(1.0)
    def test_nub_03(self):
        self.assertEqual(nub([13, 13, 13]), [13])

    @weight(1.0)
    def test_nub_04(self):
        self.assertEqual(nub([1, 2, 3, 1, 2, 3, 1, 2, 3]), [1, 2, 3])

    @weight(1.0)
    def test_nub_05(self):
        self.assertEqual(nub([1, 1, 3, 2, 2, 5, 5, 5, 5, 4]), [1, 3, 2, 5, 4])

    @weight(1.0)
    def test_nub_06(self):
        self.assertEqual(
            nub([1, 4, 2, 5, 3, 1, 2, 3, 4, 5, 6, 1, 3, 2]), [1, 4, 2, 5, 3, 6])

    @weight(1.0)
    def test_nub_07(self):
        self.assertEqual(nub([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    @weight(1.0)
    def test_nub_08(self):
        self.assertEqual(
            nub([-3, -1, 1, 3, 2, 4, -2, -4]), [-3, -1, 1, 3, 2, 4, -2, -4])

    @weight(1.0)
    def test_nub_09(self):
        self.assertEqual(nub([1, 1, 5, 1, 10, 1, 1, 15, 1, 1]), [1, 5, 10, 15])

    @weight(1.0)
    def test_nub_10(self):
        self.assertEqual(nub([1, 2, 3, 2]), [1, 2, 3])

    @weight(1.0)
    def test_nub_11(self):
        self.assertEqual(nub([1, 2, 3, 3]), [1, 2, 3])

    @weight(1.0)
    def test_nub_12(self):
        self.assertEqual(nub([1, 2, 3, 1]), [1, 2, 3])

    @weight(1.0)
    def test_nub_13(self):
        orig = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        xs = orig[:]
        ans = nub(xs)
        self.assertEqual(orig, xs)
        self.assertEqual(ans, [1, 2, 3])
