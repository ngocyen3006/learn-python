CREATE TABLE TU_DIEN
(
    tu text not null unique,
    nghia text not null
);
INSERT INTO TU_DIEN VALUES
('teacher','Thầy giáo, giáo viên'),
('people','Con người'),
('pilot','Phi công'),
('ghost','Oan hồn, hồn ma');
