CREATE TABLE DEPARTMENT
(
    ID integer primary key AUTOINCREMENT,
    Name text not null unique,
    Work text not null
);
INSERT INTO DEPARTMENT(Name, Work)
values
    ('Hanh chinh', 'Giai quyet cong viec hanh chinh cua cong ty'),
    ('Ky thuat', 'Thuc hien du an ky thuat cua cong ty')
