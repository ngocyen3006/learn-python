import sqlite3

conn = sqlite3.connect(r"Staff.db")
conn.row_factory = sqlite3.Row

depts = "SELECT * from DEPARTMENT"
staffs = "SELECT * from STAFF"


def read_Dept():
    try:
        Dep = conn.execute(depts)
        for row in Dep:
            print_Dep_data(row['ID'], row['Name'], row['Work'])

    except sqlite3.OperationalError:
        print("Non data")


def read_Staff():
    try:
        Dept = conn.execute(depts)
        Dept = Dept.fetchall()
        staff = conn.execute(staffs)
        staff = staff.fetchall()

        for dept in Dept:
            print('\n')
            print(f"--------- {dept['ID']}: {dept['Name']} ---------")
            print_title_Staff()
            for st in staff:
                if st['Dep_ID'] == dept['ID']:
                    salary = f"{st['Salary']:,.0f}"
                    print_Staff_data(st['ID_Staff'], st['Name'], st['Age'], st['Address'], salary)

    except sqlite3.OperationalError:
        print("Non data")


def add_new_Dep(name, work):
    sql = "insert into DEPARTMENT(Name, Work) values(?,?)"
    conn.execute(sql, (name, work))
    conn.commit()


def add_new_staff(name, age, address, salary, dept_ID):
    sql = "insert into STAFF(Name, Age,Address,Salary,Dep_ID) values(?,?,?,?,?)"
    conn.execute(sql, (name, age, address, salary, dept_ID))
    conn.commit()


def update_Dept(work, id):
    conn.execute('update DEPARTMENT set Work= ? where ID= ?', (work, id))
    conn.commit()


def update_age_staff(age, id):
    conn.execute('update STAFF set Age= ? where ID_Staff= ?', (age, id))
    conn.commit()


def update_salary_staff(salary, id):
    conn.execute('update STAFF set Salary= ? where ID_Staff= ?', (salary, id))
    conn.commit()


def update_address_staff(address, id):
    conn.execute('update STAFF set Address= ? where ID_Staff= ?', (address, id))
    conn.commit()


def update_dept_ID_staff(dept_ID, id):
    conn.execute('update STAFF set Dep_ID= ? where ID_Staff= ?', (dept_ID, id))
    conn.commit()


def update_staff(age, address, salary, dept_ID, id):
    conn.execute('update STAFF set Age= ?, Address= ?, Salary=?, Dep_ID=?  where ID_Staff= ?',
                 (age, address, salary, dept_ID, id))
    conn.commit()


def print_title_Dep():
    print('\t--- List of Department ---')
    print("ID".ljust(4) + "| " + "Name".ljust(25) + "| " + "Work".ljust(60))
    print("-" * 104)


def print_title_Staff():
    print("ID".ljust(4) + "| " + "Name".ljust(20) + "| " + "Age".ljust(4), end="")
    print("| " + "Address".ljust(20) + "| " + "Salary".rjust(10))
    print("-" * 70)


def print_Dep_data(ID, name, work):
    print(str(ID).ljust(4) + "| " + name.ljust(25) + "| " + work.ljust(60))
    print("-" * 104)


def print_Staff_data(ID, name, age, address, salary):
    print(str(ID).ljust(4) + "| " + name.ljust(20) + "| " + str(age).ljust(4), end="")
    print("| " + address.ljust(20) + "| " + str(salary).rjust(10))
    print("-" * 70)
