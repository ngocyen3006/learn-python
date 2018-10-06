# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


def rockPaperScissors(p1, p2):
    a = ["rock beats scissors",
         "scissors beats paper",
         "paper beats rock"]
    winner = 0
    if p1 == p2:
        winner = winner
    elif p1 + " beats " + p2 in a:
        winner = winner + 1
    else:
        winner = winner - 1

    if winner == 0:
        return "Draw."
    elif winner > 0:
        return "Player One win."
    else:
        return "Player Two win."
