CREATE TABLE PHONG_BAN
(
    ma_phong char(2) primary key,
    ten_phong text not null
);
CREATE TABLE NHAN_VIEN
(
    ma_so char(3) primary key,
    ho_ten text not null,
    ngay_sinh char(10),
    gioi_tinh char(1) default '1',
    luong integer,
    ma_phong char(2)
);