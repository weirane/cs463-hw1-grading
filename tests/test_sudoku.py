import unittest
from gradescope_utils.autograder_utils.decorators import weight
from submission import check_sudoku


class SudokuTests(unittest.TestCase):
    @weight(2.0)
    def test_check_sudoku_1(self):
        # a pretty regular pattern of a correct sudoku.
        grid = [[1,2,3, 4,5,6, 7,8,9],
                [4,5,6, 7,8,9, 1,2,3],
                [7,8,9, 1,2,3, 4,5,6],

                [2,3,4, 5,6,7, 8,9,1],
                [5,6,7, 8,9,1, 2,3,4],
                [8,9,1, 2,3,4, 5,6,7],

                [3,4,5, 6,7,8, 9,1,2],
                [6,7,8, 9,1,2, 3,4,5],
                [9,1,2, 3,4,5, 6,7,8],
               ]
        self.assertTrue(check_sudoku(grid))

    @weight(2.0)
    def test_check_sudoku_2(self):
        # keeps repeating the top three rows. only columns are faulty.
        grid = [[1,2,3, 4,5,6, 7,8,9],
                [4,5,6, 7,8,9, 1,2,3],
                [7,8,9, 1,2,3, 4,5,6],

                [1,2,3, 4,5,6, 7,8,9],
                [4,5,6, 7,8,9, 1,2,3],
                [7,8,9, 1,2,3, 4,5,6],

                [1,2,3, 4,5,6, 7,8,9],
                [4,5,6, 7,8,9, 1,2,3],
                [7,8,9, 1,2,3, 4,5,6],
                ]
        self.assertFalse(check_sudoku(grid))

    @weight(2.0)
    def test_check_sudoku_3(self):
        # keeps repeating the left three 3x3 groups. only rows are faulty.
        grid = [[1,2,3, 1,2,3, 1,2,3],
                [4,5,6, 4,5,6, 4,5,6],
                [7,8,9, 7,8,9, 7,8,9],

                [2,3,4, 2,3,4, 2,3,4],
                [5,6,7, 5,6,7, 5,6,7],
                [8,9,1, 8,9,1, 8,9,1],

                [3,4,5, 3,4,5, 3,4,5],
                [6,7,8, 6,7,8, 6,7,8],
                [9,1,2, 9,1,2, 9,1,2],
               ]
        self.assertFalse(check_sudoku(grid))

    @weight(2.0)
    def test_check_sudoku_4(self):
        # rows are shuffled to have only 3x3 groups wrong.
        grid = [[1,2,3, 4,5,6, 7,8,9],
                [2,3,4, 5,6,7, 8,9,1],
                [3,4,5, 6,7,8, 9,1,2],
                [4,5,6, 7,8,9, 1,2,3],
                [5,6,7, 8,9,1, 2,3,4],
                [6,7,8, 9,1,2, 3,4,5],
                [7,8,9, 1,2,3, 4,5,6],
                [8,9,1, 2,3,4, 5,6,7],
                [9,1,2, 3,4,5, 6,7,8],
               ]
        self.assertFalse(check_sudoku(grid))

    @weight(1.0)
    def test_check_sudoku_5(self):
        # only the extra 5 in the dead center is a problem.
        grid = [[1,2,3, 4,5,6, 7,8,9],
                [4,5,6, 7,8,9, 1,2,3],
                [7,8,9, 1,2,3, 4,5,6],

                [2,3,4, 5,6,7, 8,9,1],
                [5,6,7, 8,5,1, 2,3,4],
                [8,9,1, 2,3,4, 5,6,7],

                [3,4,5, 6,7,8, 9,1,2],
                [6,7,8, 9,1,2, 3,4,5],
                [9,1,2, 3,4,5, 6,7,8],
               ]
        self.assertFalse(check_sudoku(grid))

    @weight(1.0)
    def test_check_sudoku_6(self):
        # way wrong...
        grid = [[1,1,1, 1,1,1, 1,1,1],
                [1,1,1, 1,1,1, 1,1,1],
                [1,1,1, 1,1,1, 1,1,1],

                [1,1,1, 1,2,3, 1,1,1],
                [1,1,1, 4,5,6, 1,1,1],
                [1,1,1, 7,8,9, 1,1,1],

                [1,1,1, 1,1,1, 1,1,1],
                [1,1,1, 1,1,1, 1,1,1],
                [1,1,1, 1,1,1, 1,1,1],
               ]
        self.assertFalse(check_sudoku(grid))

    @weight(1.0)
    def test_check_sudoku_7(self):
        # another correct grid.
        grid = [[2,7,8, 4,6,9, 1,5,3],
                [6,9,3, 1,2,5, 4,7,8],
                [4,5,1, 7,8,3, 2,6,9],

                [7,6,5, 8,9,4, 3,2,1],
                [3,4,2, 6,1,7, 9,8,5],
                [8,1,9, 3,5,2, 6,4,7],

                [9,8,4, 5,3,6, 7,1,2],
                [5,2,6, 9,7,1, 8,3,4],
                [1,3,7, 2,4,8, 5,9,6],
               ]
        self.assertTrue(check_sudoku(grid))

    @weight(1.0)
    def test_check_sudoku_8(self):
        # another correct grid.
        grid =([[7,8,6, 4,9,3, 2,5,1],
                [3,2,1, 8,7,5, 4,9,6],
                [9,4,5, 6,2,1, 8,7,3],

                [1,5,7, 9,3,8, 6,2,4],
                [2,9,8, 5,4,6, 3,1,7],
                [4,6,3, 7,1,2, 9,8,5],

                [8,1,2, 3,6,7, 5,4,9],
                [6,7,4, 2,5,9, 1,3,8],
                [5,3,9, 1,8,4, 7,6,2],
             ])
        self.assertTrue(check_sudoku(grid))

    @weight(1.0)
    def test_check_sudoku_9(self):
        orig = [[2,4,1,9,7,5,3,8,6],
                [9,5,6,3,8,4,1,7,2],
                [3,8,7,1,6,2,5,9,4],
                [8,9,2,5,4,1,6,3,7],
                [6,1,5,8,3,7,4,2,9],
                [4,7,3,2,9,6,8,5,1],
                [1,2,9,6,5,3,7,4,8],
                [5,6,4,7,2,8,9,1,3],
                [7,3,8,4,1,9,2,6,5]]
        grid = orig[:]
        self.assertTrue(check_sudoku(grid))
        self.assertEqual(orig,grid)
