import sqlite3


def them_sach_moi(ten, nam, dongia):
    sql = "insert into SACH(TEN,NAM,DONGIA) values(?,?,?)"  # play holder
    conn.execute(sql, (ten, nam, dongia))  # tuple
    conn.commit()


def xoa_sach(id):
    sql = "delete from SACH where ID=?"
    # tuple 1 phtu truyen bien vao phai co dau phay sau bien
    conn.execute(sql, (id,))
    conn.commit()


conn = sqlite3.connect("QLSach.db")

# them sach
# sql = "insert into SACH(TEN,NAM,DONGIA) values('Harry Potter 2','1989',120000)"
# conn.execute(sql)
# conn.commit()

# cach them 2
# sql = "insert into SACH(TEN,NAM,DONGIA) values(?,?,?)"  # play holder
# conn.execute(sql, ('Hon ma tro ve', 2018, 53000))  # tuple
# conn.commit()

# them_sach_moi('Nguoi dep ngu trong rung', 1999, 43000)

xoa_sach(1)

# doc bang SACH
sql = "select * from SACH order by DONGIA desc"
cursor = conn.execute(sql)
for row in cursor:
    print("ID:", row[0])
    print("Ten:", row[1])
    print("Nam xuat ban:", row[2])
    print(f"Don gia: {row[3]:,.0f}")
    print('\n')
conn.close()
