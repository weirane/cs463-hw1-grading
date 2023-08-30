import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import fib
import timeout_decorator


class FibTests(unittest.TestCase):
    @weight(1.0)
    def test_fib_1(self):
        self.assertEqual(fib(0), 0)

    @weight(1.0)
    def test_fib_2(self):
        self.assertEqual(fib(1), 1)

    @weight(1.0)
    def test_fib_3(self):
        self.assertEqual(fib(2), 1)

    @weight(1.0)
    def test_fib_4(self):
        self.assertEqual(fib(3), 2)

    @weight(1.0)
    def test_fib_5(self):
        self.assertEqual(fib(4), 3)

    @weight(1.0)
    def test_fib_6(self):
        self.assertEqual(fib(5), 5)

    @weight(1.0)
    def test_fib_7(self):
        self.assertEqual(fib(6), 8)

    @weight(1.0)
    @timeout_decorator.timeout(5)
    def test_fib_8(self):
        self.assertEqual(fib(7), 13)

    @weight(1.0)
    @timeout_decorator.timeout(5)
    def test_fib_9(self):
        self.assertEqual(fib(20), 6765)

    @weight(1.0)
    @timeout_decorator.timeout(5)
    def test_fib_10(self):
        self.assertEqual(fib(29), 514229)

    @weight(1.0)
    @timeout_decorator.timeout(5)
    def test_fib_11(self):
        self.assertEqual(fib(43), 433494437)

    @weight(1.0)
    @timeout_decorator.timeout(5)
    def test_fib_12(self):
        self.assertEqual(fib(55), 139583862445)
