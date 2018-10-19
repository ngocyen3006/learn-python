class Person:

    def __init__(self, name, age=1, gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender

    def showInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


aimee = Person("Aimee", 21, "Female")

aimee.showInfo()

print(" --------------- ")

alice = Person("Alice")

alice.showInfo()

print(" --------------- ")

tran = Person("Tran", 37)

tran.showInfo()
