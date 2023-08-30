import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import is_prime


class IsPrimeTests(unittest.TestCase):
    @weight(1.0)
    def test_is_prime_01(self):
        self.assertFalse(is_prime(-5))

    @weight(1.0)
    def test_is_prime_02(self):
        self.assertFalse(is_prime(0))

    @weight(1.0)
    def test_is_prime_03(self):
        self.assertFalse(is_prime(1))

    @weight(1.0)
    def test_is_prime_04(self):
        self.assertTrue(is_prime(2))

    @weight(1.0)
    def test_is_prime_05(self):
        self.assertTrue(is_prime(3))

    @weight(1.0)
    def test_is_prime_06(self):
        self.assertFalse(is_prime(4))

    @weight(1.0)
    def test_is_prime_07(self):
        self.assertTrue(is_prime(5))

    @weight(1.0)
    def test_is_prime_08(self):
        self.assertTrue(is_prime(41))

    @weight(1.0)
    def test_is_prime_09(self):
        self.assertFalse(is_prime(117))

    @weight(1.0)
    def test_is_prime_10(self):
        self.assertTrue(is_prime(1117))

    @weight(1.0)
    def test_is_prime_11(self):
        self.assertTrue(is_prime(11117))

    @weight(1.0)
    def test_is_prime_12(self):
        self.assertTrue(is_prime(49999))

    @weight(1.0)
    def test_is_prime_13(self):
        self.assertFalse(is_prime(200000000))
