CREATE TABLE SINH_VIEN
(
    ID integer primary key AUTOINCREMENT,
    ho_ten text not null,
    ngay_sinh text not null,
    gioi_tinh integer not null,
    diem_trung_binh real not null,
    ma_khoa text not null
)