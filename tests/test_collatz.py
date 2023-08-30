import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import collatz


class TestCollatz(unittest.TestCase):
    @weight(1.0)
    def test_collatz_1(self):
        self.assertEqual(collatz(1), [1])

    @weight(1.0)
    def test_collatz_2(self):
        self.assertEqual(collatz(3), [3, 10, 5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_3(self):
        self.assertEqual(collatz(4), [4, 2, 1])

    @weight(1.0)
    def test_collatz_4(self):
        self.assertEqual(collatz(5), [5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_5(self):
        self.assertEqual(collatz(10), [10, 5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_6(self):
        self.assertEqual(
            collatz(11), [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_7(self):
        self.assertEqual(
            collatz(17), [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_8(self):
        self.assertEqual(collatz(42), [42, 21, 64, 32, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_9(self):
        self.assertEqual(collatz(100), [
            100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_10(self):
        self.assertEqual(
            collatz(8192), [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_11(self):
        self.assertEqual(collatz(2), [2, 1])

    @weight(1.0)
    def test_collatz_12(self):
        self.assertEqual(collatz(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])

    @weight(1.0)
    def test_collatz_13(self):
        self.assertEqual(collatz(99), [
            99, 298, 149, 448, 224, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
