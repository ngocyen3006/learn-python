import sqlite3

conn = sqlite3.connect(r"product.db")
conn.row_factory = sqlite3.Row

sql = "select * from product"


def read_data():
    try:
        cursor = conn.execute(sql)
        for row in cursor:
            print_data(str(row['id']), row['Name'], str(row['Price']), str(row['Amount']))

    except sqlite3.OperationalError:
        print("Non data")


def add_new_product(Name, Price, Amount):
    sql = "insert into product(Name, Price, Amount) values(?,?,?)"
    conn.execute(sql, (Name, Price, Amount))
    conn.commit()


def find_product(product_name):
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    for rs in rows:
        if product_name[0].upper() + product_name[1:].lower() in rs['Name'] or product_name.lower() in rs['Name']:
            print_data(str(rs['id']), rs['Name'], str(rs['Price']), str(rs['Amount']))


def delete_product(id):
    sql = 'delete from product where id= ?'
    conn.execute(sql, (id,))
    conn.commit()


def update(Price, Amount, id):
    conn.execute('update product set Price= ?, Amount= ? where id= ?', (Price, Amount, id))
    conn.commit()


def find_product_ID(ID):
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    for rs in rows:
        if ID == rs['id']:
            return True
    return False


def print_title():
    print('ID'.ljust(3) + '| ' + 'Name'.ljust(15) + '|' + 'Price'.center(12) + '| ' + 'Amount'.center(6))
    print('-' * 41)


def print_data(ID, Name, Price, Amount):
    print(ID.ljust(3) + '| ' + Name.ljust(15) + '|' + Price.rjust(12) + '| ' + Amount.rjust(6))
    print('-' * 41)
