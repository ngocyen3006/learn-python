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
    menu = '''  1. Just update Age
        2. Just update Address
        3. Just update Salary
        4. Just update Dept ID
        5. Update all '''
    menu = ''.join(menu.split('   '))
    print(menu)
    choice = int(input('> '))
    id_staff = int(input('Input ID you want to update: '))

    if choice == 1:
        age = int(input('Input new age: '))
        update_age_staff(age, id_staff)

    elif choice == 2:
        address = input('Input new address: ')
        update_address_staff(address, id_staff)

    elif choice == 3:
        salary = int(input('Input new salary: '))
        update_salary_staff(salary, id_staff)

    elif choice == 4:
        dept_ID = int(input('Input new dept ID: '))
        update_dept_ID_staff(dept_ID, id_staff)

    elif choice == 5:
        age = int(input('Input new age: '))
        address = input('Input new address: ')
        salary = int(input('Input new salary: '))
        dept_ID = int(input('Input new dept ID: '))
        update_staff(age, address, salary, dept_ID, id_staff)
    else:
        print('No number in you choice!')
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
