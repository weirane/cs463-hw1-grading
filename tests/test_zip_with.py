import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import zip_with


class ZipWithTests(unittest.TestCase):
    @weight(2.0)
    def test_zip_with_1(self):
        def add(x, y): return x + y
        self.assertEqual(zip_with(add, [1, 2, 3, 4], [10, 10, 10, 10]), [11, 12, 13, 14])

    @weight(2.0)
    def test_zip_with_2(self):
        def add(x, y): return x + y
        self.assertEqual(zip_with(add, [1, 2, 3, 4], [5, 6, 7, 8]), [6, 8, 10, 12])

    @weight(2.0)
    def test_zip_with_3(self):
        def mul(x, y): return x * y
        # first list has fewer elements.
        self.assertEqual(zip_with(mul, [2, 3, 4], [5, 5, 5, 5, 5]), [10, 15, 20])

    @weight(2.0)
    def test_zip_with_4(self):
        def mul(x, y): return x * y
        # second list has fewer elements.
        self.assertEqual(zip_with(mul, [2, 3, 4, 5, 6, 7, 8], [5, 5, 5]), [10, 15, 20])
        def mul(x, y): return x * y
        # first list has zero elements.
        self.assertEqual(zip_with(mul, [], [5, 5, 5, 5, 5]), [])

    @weight(2.0)
    def test_zip_with_5(self):
        def mul(x, y): return x * y
        # second list has zero elements.
        self.assertEqual(zip_with(mul, [2, 3, 4, 5, 6, 7, 8], []), [])

    @weight(2.0)
    def test_zip_with_6(self):
        def mul(x, y): return x * y
        # both lists have zero elements.
        self.assertEqual(zip_with(mul, [], []), [])
