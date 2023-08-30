import unittest
from gradescope_utils.autograder_utils.decorators import weight

REQUIRED_DEFNS = [
    "fib", "reversed", "is_prime", "nub", "zip_with", "collatz", "median", "mode", "check_sudoku"
]


class TestAAAFunctions(unittest.TestCase):
    @weight(0)
    def test_functions(self):
        try:
            import submission
        except ImportError:
            print('autograder bug: submission.py not found. Notify the TA')

        defns = dir(submission)
        missing = [f for f in REQUIRED_DEFNS if f not in defns]
        if missing:
            self.fail(f'Functions {", ".join(missing)} not defined')
