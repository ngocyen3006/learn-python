class Book:
    def __init__(self, code, name, date, price, quantity, publisher):
        self.code = code
        self.name = name
        self.date = date
        self.price = price
        self.quantity = quantity
        self.publisher = publisher

    def cost(self):
        return self.quantity * self.price

    def print_info(self):
        print(f'Cost: {self.cost():,.0f}')


class TextBook(Book):
    def __init__(self, code, name, date, price, quantity, publisher, status):
        Book.__init__(self, code, name, date, price, quantity, publisher)
        self.status = status

    def cost(self):
        if self.status:
            return Book.cost(self)
        return Book.cost(self) * 0.5

    def print_info(self):
        print(''.center(30, '-'))
        status = 'new'
        if self.status == 0:
            status = 'old'
        print(f'This is a {status} textbook')
        Book.print_info(self)


class ReferenceBook(Book):
    def __init__(self, code, name, date, price, quantity, publisher, tax):
        Book.__init__(self, code, name, date, price, quantity, publisher)
        self.tax = tax / 100

    def cost(self):
        return Book.cost(self) * (1 + self.tax)

    def print_info(self):
        print(''.center(30, '-'))
        print(f'This is a reference book')
        Book.print_info(self)


if __name__ == '__main__':
    cost_textbook = 0
    new_book = 0
    old_book = 0
    cost_refer = 0
    quan_refer = 0
    loop = 1
    while loop > 0:
        code = input('Input code: ')
        name = input('Input name: ')
        date = input('Input date: ')
        price = int(input('Input price: '))
        quan = int(input('Input quantity: '))
        publisher = input('Input publisher: ')
        type_book = int(input('Textbook or Reference book? 1: Textbook, 2: Refernce book: '))

        if type_book == 1:
            status = int(input('New or old? 1: new, 0: old: '))
            book = TextBook(code, name, date, price, quan, publisher, status)
            book.print_info()

            cost_textbook += book.cost()
            print(f'Total amount: {cost_textbook:,.0f}')

            if status:
                new_book += quan
            else:
                old_book += quan
            print(f'New book: {new_book:,.0f}; old book: {old_book:,.0f}')

        else:
            tax = int(input('Input tax(1% - 20%): '))
            book = ReferenceBook(code, name, date, price, quan, publisher, tax)
            book.print_info()

            cost_refer += book.cost()
            print(f'Total amount: {cost_refer:,.0f}')

            quan_refer += quan
            print(f'Book: {quan_refer:,.0f}')
        print(''.center(30, '-'))
        loop = int(input('Do you want to continue? 1: Yes, 0: No'))
