CREATE TABLE product
(
    id integer primary key AUTOINCREMENT,
    Name text not null,
    Price real not null,
    Amount integer not null
);
INSERT INTO product(Name, Price, Amount)