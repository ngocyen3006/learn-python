from manipulation_product import *


def choice_add_new_product():
    Name = input('Input product name: ')
    Price = f"{int(input('Input price: ')):,.0f}"
    Amount = f"{int(input('Input amount: ')):,.0f}"

    add_new_product(Name, Price, Amount)
    print("Add new product success")
    print('\t---------------------')


def choice_find_product():
    pr_name = input("Input name: ")
    print_title()
    find_product(pr_name)


def choice_update_product():
    id = int(input('Please specify the ID of product to be updated: '))
    if find_product_ID(id):
        Price = f"{int(input('Input new price: ')):,.0f}"
        Amount = f"{int(input('Input new amount: ')):,.0f}"

        update(Price, Amount, id)
        print('Update success')
    else:
        print(f"ID {id} not found")
        print('Update failure')
    print('\t---------------------')


def choice_del_product():
    id = input('Please specify the ID of product to be deleted: ')
    confirm = int(input('Are you sure? 1: Yes, 0: No    '))
    if confirm == 1:
        delete_product(id)
        print('Delete success')
        print('\t---------------------')


def main():
    loop = 1
    while loop == 1:
        print('What do you want to do?')
        baseMenu = '''
            0: Exit
            1: Show data
            2: Add new product
            3: Find product with name
            4: Update product
            5: Delete product
            > '''
        menu = "\n".join(baseMenu.split('\n            '))
        choice = int(input(menu))
        if choice == 0:
            break
        elif choice == 1:
            print_title()
            read_data()
        elif choice == 2:
            choice_add_new_product()
        elif choice == 3:
            choice_find_product()
        elif choice == 4:
            choice_update_product()
        elif choice == 5:
            choice_del_product()
        else:
            print('No number in you choice!')
            break

        loop = int(input("Do you want to continue? 1: Yes, 0: No    "))


if __name__ == '__main__':
    main()
    conn.close()
