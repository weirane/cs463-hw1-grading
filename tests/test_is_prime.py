import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import is_prime


class IsPrimeTests(unittest.TestCase):
    def prime_case(self, n):
        if not is_prime(n):
            self.fail(f'{n} should be a prime number')

    def not_prime_case(self, n):
        if is_prime(n):
            self.fail(f'{n} should not be a prime number')

    @weight(1.0)
    def test_is_prime_01(self):
        self.not_prime_case(-5)

    @weight(1.0)
    def test_is_prime_02(self):
        self.not_prime_case(0)

    @weight(1.0)
    def test_is_prime_03(self):
        self.not_prime_case(1)

    @ weight(1.0)
    def test_is_prime_04(self):
        self.prime_case(2)

    @ weight(1.0)
    def test_is_prime_05(self):
        self.prime_case(3)

    @ weight(1.0)
    def test_is_prime_06(self):
        self.not_prime_case(4)

    @ weight(1.0)
    def test_is_prime_07(self):
        self.prime_case(5)

    @ weight(1.0)
    def test_is_prime_08(self):
        self.prime_case(41)

    @ weight(1.0)
    def test_is_prime_09(self):
        self.not_prime_case(117)

    @ weight(1.0)
    def test_is_prime_10(self):
        self.prime_case(1117)

    @ weight(1.0)
    def test_is_prime_11(self):
        self.prime_case(11117)

    @ weight(1.0)
    def test_is_prime_12(self):
        self.prime_case(49999)

    @ weight(1.0)
    def test_is_prime_13(self):
        self.not_prime_case(200000000)
