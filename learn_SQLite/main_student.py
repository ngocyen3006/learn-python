import sqlite3

conn = sqlite3.connect("student.db")

# lay cau truc bang de in k can lay vi tri
conn.row_factory = sqlite3.Row


def in_ds_hoc_sinh():
    sql = "select * from HOC_SINH"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    '''
    print(type(cur))
    # khi fetchall thi con tro ra ngoai cur,
    #  khong chay lap trong cur duoc
    rows = cur.fetchall()
    print(type(rows))
    print(rows)
    '''
    for row in rows:  # for row in cur (cu)
        print(f"ID: {row['id']}")
        print(f"Ma so: {row['ma_so']}")
        print(f"Ho ten: {row['ho_ten']}")
        print(f"Gioi tinh: {row['gioi_tinh']}")
        print("\n")


def doi_ten_hoa():
    sql = "select * from HOC_SINH"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        ten_hoa = row['ho_ten'].upper()
        id = row['id']
        sql = "update HOC_SINH set ho_ten = ? where id =?"
        conn.execute(sql, (ten_hoa, id))  # phai update theo ID
        conn.commit()


# in danh sach
in_ds_hoc_sinh()
print("------------------------------")

# doi gioi tinh la 1 cho ID=4
sql = "update HOC_SINH set gioi_tinh='1'where id=?"
conn.execute(sql, (4,))
conn.commit()

# doi ten thanh chu hoa
# cach 1
# sql = "update HOC_SINH set ho_ten = upper(ho_ten)"
# conn.execute(sql)
# conn.commit()

# cach 2
doi_ten_hoa()
in_ds_hoc_sinh()
print("----------------------------------------")

# delete danh sach hoc sinh
sql = "delete from HOC_SINH"
conn.execute(sql)
in_ds_hoc_sinh()
print("-----------------------")
print("--------rollback----------")
conn.rollback()
in_ds_hoc_sinh()
print("-----------------")

conn.close()
