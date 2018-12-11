CREATE TABLE STAFF
(
    ID_Staff integer primary key AUTOINCREMENT,
    Name text not null,
    Age integer not null,
    Address text not null,
    Salary real not null,
    Dep_ID integer not null,
    FOREIGN KEY(Dep_ID) REFERENCES DEPARTMENT(ID)
);
INSERT INTO STAFF(Name, Age, Address, Salary, Dep_ID)
values
    ('Tran Minh', 32, 'District 1', 8500000, 1)