class Staff:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Staff.id
        Staff.id += 1

    def __str__(self):
        s = '\nName: ' + self.name
        s += '\nID: ' + str(self.id)
        return s


staff_1 = Staff("John")
staff_2 = Staff("Sam")
print(staff_1)
print(staff_2)
print('------------------------')
print(f'ID of staff_1: {staff_1.id}')
print(f'ID of staff_2: {staff_2.id}')
print(f'ID of class Staff: {Staff.id}')
