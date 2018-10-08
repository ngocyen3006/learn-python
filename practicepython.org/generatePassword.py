# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random, string, re


def generatePassword():
    s = string.ascii_letters + string.digits + "!@#$&%"

    print("Size password is: ")
    size = random.randint(8, 12)
    print(size)

    p = r"[a-zA-z0-9!@#$%&]+[a-z]+[A-Z]+\d+[!@#$%&].+"
    while True:
        password = "".join(random.sample(s, size))
        if bool(re.match(p, password)):
            return password
        else:
            continue


print(generatePassword())
