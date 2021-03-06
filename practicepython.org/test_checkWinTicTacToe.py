import unittest
from checkWinTicTacToe import checkWinGame


class TestCheckWinGame(unittest.TestCase):
    def test_winner_is_1(self):
        test_case = {
            "round1": [[1, 1, 0],
                       [1, 2, 0],
                       [1, 2, 2]],
            "round2": [[1, 2, 0],
                       [2, 1, 0],
                       [2, 1, 1]],
            "round3": [[0, 1, 0],
                       [2, 1, 0],
                       [2, 1, 1]]}
        for i in range(1, 4):
            arr_name = "round" + str(i)
            arr = test_case[arr_name]
            self.assertEqual(checkWinGame(arr), 1)

    def test_winner_is_2(self):
        test_case = {
            "round1": [[2, 2, 0],
                       [2, 1, 0],
                       [2, 1, 1]],
            "round2": [[2, 2, 2],
                       [1, 1, 0],
                       [1, 0, 1]],
            "round3": [[1, 1, 2],
                       [0, 0, 2],
                       [1, 1, 2]],
            "round4": [[0, 1, 2],
                       [1, 2, 1],
                       [2, 2, 0]]}
        for i in range(1, 5):
            arr_name = "round" + str(i)
            arr = test_case[arr_name]
            self.assertEqual(checkWinGame(arr), 2)

    def test_no_winner(self):
        test_case = {
            "round1": [[1, 2, 0],
                       [2, 1, 0],
                       [2, 1, 2]],
            "round2": [[1, 2, 0],
                       [2, 1, 0],
                       [2, 1, 0]]}
        for i in range(1, 3):
            arr_name = "round" + str(i)
            arr = test_case[arr_name]
            self.assertEqual(checkWinGame(arr), 0)


if __name__ == '__main__':
    unittest.main()
