from manipulate_staff import *


def menu():
    menu = ''' 0. Exit
    1. Show data department
    2. Show data staff in the department
    3. Add new department
    4. Add new staff
    5. Update data department
    6. Update data staff '''
    menu = ''.join(menu.split('   '))
    print(menu)


def choice_add_new_dept():
    name = input('Input dept name: ')
    work = input('Input dept work: ')
    add_new_Dep(name, work)
    print("Add new dept success")
    print('\n')


def choice_add_new_staff():
    name = input('Input staff name: ')
    dept_id = int(input('Input Dept ID: '))
    age = int(input('Input age: '))
    address = input('Input address: ')
    salary = float(input('Input salary: '))
    add_new_staff(name, age, address, salary, dept_id)
    print("Add new staff success")
    print('\n')


def choice_update_dept():
    dept_id = int(input('Input dept ID: '))
    work = input('Input new work: ')
    update_Dept(work, dept_id)
    print("Update success")


def choice_update_staff():
    id_staff = int(input('Input ID you want to update: '))
    age = input('Input new age: ')
    address = input('Input new address: ')
    salary = input('Input new salary: ')
    dept_ID = input('Input new dept ID: ')
    if age == '':
        age = None
    else:
        age = int(age)

    if address == '':
        address = None

    if salary == '':
        salary = None
    else:
        salary = int(salary)

    if dept_ID == '':
        dept_ID = None
    else:
        dept_ID = int(dept_ID)

    update_staff(id_staff, age, address, salary, dept_ID)

    print('Update success')
    print('\n')


def main():
    print('What do you want to do?')
    menu()
    choice = int(input('> '))

    while choice != 0:
        if choice == 1:
            print_title_Dep()
            read_Dept()

        elif choice == 2:
            read_Staff()

        elif choice == 3:
            choice_add_new_dept()

        elif choice == 4:
            choice_add_new_staff()

        elif choice == 5:
            choice_update_dept()

        elif choice == 6:
            choice_update_staff()

        else:
            print('No number in you choice!')
            break

        print('\n')
        print('Do you want to continue?')
        menu()
        choice = int(input('> '))


if __name__ == '__main__':
    main()
    conn.close()
