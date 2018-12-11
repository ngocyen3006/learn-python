import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r"QLPhim.db")
    sql = "select * from PHIM"

    # Phim 1
    '''
    ten = "Brother Bear"
    nam_sx = "01/11/2003"
    the_loai = "Comedy-drama, cartoon"
    thoi_luong = 85
    nuoc_sx = "United States"
    them_phim_moi(ten, nam_sx, the_loai, thoi_luong, nuoc_sx)
    '''

    try:
        cursor = conn.execute(sql)
        for row in cursor:
            print(f"ID: {row[0]}")
            print(f"Ten: {row[1]}")
            print(f"Nam san xuat: {row[2]}")
            print(f"The loai: {row[3]}")
            print(f"Thoi luong: {row[4]}")
            print(f"Nuoc san xuat: {row[5]}")
            print('\n')
    except sqlite3.OperationalError:
        print("File null")

    conn.close()
