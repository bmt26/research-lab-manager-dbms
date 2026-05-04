# LAB MEMBER INSERTS
# Each valid mentorship type between students, collaborators, and faculty, and one mentorship chain
INSERT INTO lab_member (MID, NAME, JOIN_DATE, TYPE, MENTOR, M_SDATE, M_EDATE)
VALUES
(253, 'Jeves Stobs', '1976-04-01', 'Collaborator', null, null, null),
(364, 'Gill Bates', '1975-04-04', 'Student', null, null, null),
(648, 'Thomas Johnson', '2004-12-07', 'Faculty', null, null, null),
(715, 'Henry Leeson', '2005-11-03', 'Faculty', 253, '2005-11-10', null),
(984, 'Jacob Sandry', '2015-12-25', 'Student', 253, '2015-12-30', null),
(743, 'Byron Henderson', '2010-06-17', 'Collaborator', 364, '2010-06-20', null),
(518, 'Luke Ford', '2023-02-18', 'Faculty', 648, '2023-02-18', '2024-02-18'),
(627, 'Jessica Park', '2021-10-05', 'Student', 364, '2021-10-05', null),
(846, 'Sarah Stevens', '2018-04-10', 'Collaborator', 253, '2018-04-10', null),
(374, 'Tom Sayer', '2013-09-02', 'Student', 648, '2013-09-02', '2020-10-12'),
(567, 'Lisa Stansa', '2020-07-22', 'Collaborator', 648, '2020-07-22', null),
(843, 'Mary Pauls', '2008-01-29', 'Faculty', 518, '2024-02-20', null);

INSERT INTO student (MID, SID, LEVEL, MAJOR)
VALUES
(364, 813, 'Senior', 'Computer Science'),
(984, 496, 'Senior', 'Chemistry'),
(627, 483, 'Sophmore', 'Computer Science'),
(374, 177, 'Freshman', 'Chemistry');

INSERT INTO faculty (MID, DEPARTMENT)
VALUES
(648, 'Computer Science'),
(715, 'Chemistry'),
(518, 'Computer Science'),
(843, 'Chemistry');

INSERT INTO collaborator (MID, AFFILIATION, CV)
VALUES
(253, 'Computer Science', 'Hi I am Jeves Stobs.'),
(743, 'Chemistry', 'Hi I am Lisa Stansa.'),
(846, 'Computer Science', 'Hi I am Byron Henderson.'),
(567, 'Chemistry', 'Hi I am Sarah Stevens.');

# PROJECT INSERTS
INSERT INTO project (PID, TITLE, S_DATE, E_DATE, E_DURATION, LEADER)
VALUES
(762, 'Solving NP-Hard Froblems', '2024-01-01', '2025-02-12', 366, 518),
(477, 'Predicting Portein Folds', '2026-02-10', null, 74, 715),
(236, 'Halting Problem Solved', '2026-03-15', null, 480, 518),
(769, 'Room-Temperature Superconductors', '2026-04-11', null, 100, 843);

# WORKS INSERTS
INSERT INTO works (PID, MID, ROLE, HOURS)
VALUES
(762, 253, 'Programmer', 14),
(769, 253, 'Simulator', 19),
(236, 364, 'Programmer', 12),
(236, 648, 'Programmer', 20),
(477, 715, 'Leader', 36),
(762, 984, 'Writer', 24),
(769, 984, 'Chemist', 16),
(236, 743, 'Writer', 26),
(236, 518, 'Leader', 42),
(762, 518, 'Leader', 45),
(477, 627, 'Simulator', 28),
(762, 846, 'Programmer', 32),
(236, 846, 'Programmer', 16),
(762, 374, 'Writer', 18),
(477, 567, 'Chemist', 26),
(769, 843, 'Leader', 38);