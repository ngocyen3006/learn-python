CREATE TABLE HOC_SINH
(
    id integer primary key AUTOINCREMENT,
    ma_so char(3) not null unique,
    ho_ten text not null,
    ngay_sinh char(10),
    gioi_tinh char(1) default '1',
    hoc_bong real
);
INSERT INTO HOC_SINH(ma_so,ho_ten,ngay_sinh,gioi_tinh,hoc_bong)
VALUES 
    ("A01", "Lê Thị Bạch Cúc", "2000-03-25", "0", 200000.0),
    ("A02", "Hà Ngọc Trí", "2001-12-31", "1", 0.0),
    ("A03", "Trần Mạnh Phúc", "1989-07-10", "1", 200000.0),
    ("A04", "Nguyễn Ngọc Như Quỳnh", "1994-05-20", "0", 100000.0),
    ("A05", "Công Tằng Tôn Nữ Hà Thị Mai Trinh", "1992-02-28", "0", 200000.0);
