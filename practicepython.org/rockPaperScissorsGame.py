# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


def rockPaperScissors(p1, p2):
    a = ["rock beats scissors",
         "scissors beats paper",
         "paper beats rock"]

    if p1 not in ["rock", "scissors", "paper"]:
        return "Error!"
    if p2 not in ["rock", "scissors", "paper"]:
        return "Error!"
    elif p1 == p2:
        return "Draw."
    elif p1 + " beats " + p2 in a:
        return "Player One win."
    else:
        return "Player Two win."
