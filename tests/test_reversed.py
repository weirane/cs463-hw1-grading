import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import reversed


class ReversedTests(unittest.TestCase):
    @weight(1.0)
    def test_reversed_1(self):
        self.assertEqual(reversed([]), [])

    @weight(1.0)
    def test_reversed_2(self):
        self.assertEqual(reversed([5]), [5])

    @weight(1.0)
    def test_reversed_3(self):
        self.assertEqual(reversed([2, 4, 6, 8]), [8, 6, 4, 2])

    @weight(1.0)
    def test_reversed_4(self):
        self.assertEqual(reversed([True, 3, "hat"]), ["hat", 3, True])

    @weight(1.0)
    def test_reversed_5(self):
        self.assertEqual(reversed([1, 1, 1, 2, 1, 1]), [1, 1, 2, 1, 1, 1])

    @weight(1.0)
    def test_reversed_6(self):
        self.assertEqual(reversed([1, 3, 5, 2, 4, 6]), [6, 4, 2, 5, 3, 1])

    @weight(1.0)
    def test_reversed_7(self):
        self.assertEqual(reversed([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

    @weight(1.0)
    def test_reversed_8(self):
        self.assertEqual(reversed([1.1, 2.2, 3.3]), [3.3, 2.2, 1.1])

    @weight(1.0)
    def test_reversed_9(self):
        xs = [1, 2, 3, 4, 5, 6]
        _ = reversed(xs)
        # the original list shouldn't be modified.
        self.assertEqual([1, 2, 3, 4, 5, 6], xs)

    @weight(1.0)
    def test_reversed_10(self):
        # give test 9 more weighting.
        self.test_reversed_9()

    @weight(1.0)
    def test_reversed_11(self):
        xs = [1, 2, 3, 4, 5, 6]
        id1 = id(xs)  # memory location of the original list
        vs = reversed(xs)
        id2 = id(vs)  # memory location of the returned list
        # they shouldn't match.
        self.assertFalse(id1 == id2)

    @weight(1.0)
    def test_reversed_12(self):
        # give test 11 more weighting.
        self.test_reversed_11()

    @weight(1.0)
    def test_reversed_13(self):
        orig = [1, 2, 3, 4, 5]
        xs = orig[:]
        ans = reversed(xs)
        self.assertEqual(orig, xs)
        self.assertEqual(ans, [5, 4, 3, 2, 1])
