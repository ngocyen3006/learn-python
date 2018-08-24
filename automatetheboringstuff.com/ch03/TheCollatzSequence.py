# Practice projects "The Collatz Sequence" and "Input Validation"


def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


try:
    number = int(input())
    while (number > 1):
        print(int(collatz(number)))
        number = collatz(number)

except ValueError:
    print("Error: Invalid argument.")
