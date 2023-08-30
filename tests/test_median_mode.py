import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import median, mode


class MedianModeTests(unittest.TestCase):
    @weight(1.0)
    def test_median_1(self): self.assertEqual(median([1, 1, 1]), 1)
    @weight(1.0)
    def test_median_2(self): self.assertEqual(median([1, 2, 3]), 2)
    @weight(1.0)
    def test_median_3(self): self.assertEqual(median([1, 2, 2, 3]), 2)
    @weight(1.0)
    def test_median_4(self): self.assertEqual(median([1, 2, 3, 4]), 2.5)
    @weight(1.0)
    def test_median_5(self): self.assertEqual(median([1, 3, 2, 3, 1]), 2)
    @weight(1.0)
    def test_median_6(self): self.assertEqual(median([5, 5, 5, 25]), 5)
    @weight(1.0)
    def test_median_7(self): self.assertEqual(median([13, 6, 13, 3, 7, 29, 12, 1, 2, 14]), 9.5)

    @weight(1.0)
    def test_median_8(self):
        orig = [5, 5, 5, 25]
        xs = orig[:]
        ans = median(xs)
        self.assertEqual(orig, xs)
        self.assertEqual(ans, 5)

    # ---------------------------------------------------------------------

    @weight(1.0)
    def test_mode_1(self): self.assertEqual(mode([1, 1, 1]), [1])
    @weight(1.0)
    def test_mode_2(self): self.assertEqual(mode([1, 2, 3]), [1, 2, 3])
    @weight(1.0)
    def test_mode_3(self): self.assertEqual(mode([1, 2, 2, 3]), [2])
    @weight(1.0)
    def test_mode_4(self): self.assertEqual(mode([1, 2, 3, 4]), [1, 2, 3, 4])
    @weight(1.0)
    def test_mode_5(self): self.assertEqual(mode([1, 3, 2, 3, 1]), [1, 3])
    @weight(1.0)
    def test_mode_6(self): self.assertEqual(mode([5, 5, 5, 25]), [5])
    @weight(1.0)
    def test_mode_7(self): self.assertEqual(mode([13, 6, 13, 3, 7, 29, 12, 1, 2, 14]), [13])

    @weight(1.0)
    def test_mode_8(self):
        orig = [5, 5, 5, 25]
        xs = orig[:]
        ans = mode(xs)
        self.assertEqual(orig, xs)
        self.assertEqual(ans, [5])
