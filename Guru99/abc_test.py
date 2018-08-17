alph = ['a', 'b', 'c', 'g']
ralph = list(reversed(alph))
print(ralph)

a = "String"
a = a.upper()
print(a)
a = a.lower()
print(a)

# Example file for working with classes


class myClass():
    def method1(self):
        print("Guru99")

    def method2(self, someString):
        print("Software Testing:" + someString)


def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2(" Testing is fun")


if __name__ == "__main__":
    main()
