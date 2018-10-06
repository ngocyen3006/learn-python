import unittest
from rockPaperScissorsGame import rockPaperScissors


class TestRocKPaperScissors(unittest.TestCase):
    def test_player_one_win(self):
        self.assertEqual(rockPaperScissors("rock", "scissors"), "Player One win.")
        self.assertEqual(rockPaperScissors("scissors", "paper"), "Player One win.")
        self.assertEqual(rockPaperScissors("paper", "rock"), "Player One win.")

    def test_player_two_win(self):
        self.assertEqual(rockPaperScissors("scissors", "rock"), "Player Two win.")
        self.assertEqual(rockPaperScissors("paper", "scissors"), "Player Two win.")
        self.assertEqual(rockPaperScissors('rock', 'paper'), "Player Two win.")

    def test_draw(self):
        self.assertEqual(rockPaperScissors('rock', 'rock'), "Draw.")
        self.assertEqual(rockPaperScissors('paper', 'paper'), "Draw.")
        self.assertEqual(rockPaperScissors('scissors', 'scissors'), "Draw.")


if __name__ == '__main__':
    unittest.main()
