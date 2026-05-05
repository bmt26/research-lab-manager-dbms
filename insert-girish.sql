USE ResearchLabManager;

-- LAB_MEMBER
INSERT INTO LAB_MEMBER (MID, NAME, JOIN_DATE, TYPE, MENTOR, M_SDATE, M_EDATE) VALUES
(1,  'Dr. Alice Chen',      '2018-01-15', 'Faculty',      NULL, NULL,       NULL),
(2,  'Dr. Robert Kim',      '2017-03-20', 'Faculty',      NULL, NULL,       NULL),
(3,  'Dr. Sarah Patel',     '2019-06-01', 'Faculty',      NULL, NULL,       NULL),
(4,  'James Wilson',        '2020-09-01', 'Student',      1,    '2020-09-01', '2023-05-15'),
(5,  'Emily Davis',         '2020-09-01', 'Student',      1,    '2020-09-01', '2024-05-20'),
(6,  'Michael Brown',       '2021-01-10', 'Student',      2,    '2021-01-10', NULL),
(7,  'Priya Sharma',        '2021-09-01', 'Student',      2,    '2021-09-01', NULL),
(8,  'Carlos Rivera',       '2022-01-15', 'Student',      3,    '2022-01-15', NULL),
(9,  'Aisha Johnson',       '2022-09-01', 'Student',      3,    '2022-09-01', NULL),
(10, 'David Lee',           '2023-01-10', 'Student',      1,    '2023-01-10', NULL),
(11, 'Dr. Mark Thompson',   '2020-06-01', 'Collaborator', NULL, NULL,       NULL),
(12, 'Dr. Lisa Wang',       '2021-03-15', 'Collaborator', NULL, NULL,       NULL);

-- STUDENT
INSERT INTO STUDENT (MID, SID, LEVEL, MAJOR) VALUES
(4,  20001, 'PhD',    'Computer Science'),
(5,  20002, 'PhD',    'Computer Science'),
(6,  20003, 'MS',     'Data Science'),
(7,  20004, 'PhD',    'Computer Science'),
(8,  20005, 'MS',     'Electrical Engineering'),
(9,  20006, 'PhD',    'Data Science'),
(10, 20007, 'MS',     'Computer Science');

-- FACULTY
INSERT INTO FACULTY (MID, DEPARTMENT) VALUES
(1, 'Computer Science'),
(2, 'Data Science'),
(3, 'Electrical Engineering');

-- COLLABORATOR
INSERT INTO COLLABORATOR (MID, AFFILIATION, CV) VALUES
(11, 'MIT Lincoln Laboratory',   'PhD Stanford, 10 years industry experience in ML'),
(12, 'Google Research',          'PhD CMU, 8 years research in distributed systems');

-- PROJECT
INSERT INTO PROJECT (PID, TITLE, S_DATE, E_DATE, E_DURATION, STATUS, LEADER) VALUES
(1, 'AI-Driven Drug Discovery',         '2021-01-01', '2023-06-30', 30, 'Completed', 1),
(2, 'Quantum Computing Algorithms',     '2021-06-01', '2023-12-31', 31, 'Completed', 2),
(3, 'Neural Network Optimization',      '2022-01-01', '2024-06-30', 30, 'Completed', 1),
(4, 'Smart Grid Energy Management',     '2022-06-01', '2024-12-31', 31, 'Completed', 3),
(5, 'Federated Learning Framework',     '2023-01-01', NULL,         24, 'Active',    2),
(6, 'Autonomous Robotics System',       '2023-06-01', NULL,         24, 'Active',    3),
(7, 'Blockchain Data Integrity',        '2020-01-01', '2022-06-30', 30, 'Completed', 1),
(8, 'Climate Prediction Model',         '2020-06-01', '2022-12-31', 31, 'Completed', 2);

-- GRANT
INSERT INTO `GRANT` (GID, P_DURATION, AGENCY, BUDGET, START_DATE, PID) VALUES
(1,  30, 'NIH',     850000.00, '2021-01-01', 1),
(2,  30, 'NSF',     620000.00, '2021-01-01', 1),
(3,  31, 'DARPA',   950000.00, '2021-06-01', 2),
(4,  31, 'NSF',     430000.00, '2021-06-01', 2),
(5,  30, 'NIH',     780000.00, '2022-01-01', 3),
(6,  30, 'DOE',     540000.00, '2022-01-01', 3),
(7,  31, 'NSF',     390000.00, '2022-01-01', 3),
(8,  31, 'DOE',     670000.00, '2022-06-01', 4),
(9,  24, 'DARPA',   920000.00, '2023-01-01', 5),
(10, 24, 'NSF',     410000.00, '2023-01-01', 5),
(11, 24, 'NIH',     360000.00, '2023-06-01', 6),
(12, 30, 'NSF',     500000.00, '2020-01-01', 7),
(13, 31, 'DARPA',   750000.00, '2020-06-01', 8);

-- WORKS
INSERT INTO WORKS (PID, MID, ROLE, HOURS) VALUES
(1, 1,  'Principal Investigator', 400),
(1, 4,  'Research Assistant',     600),
(1, 5,  'Research Assistant',     580),
(1, 11, 'Collaborator',           200),
(2, 2,  'Principal Investigator', 420),
(2, 6,  'Research Assistant',     550),
(2, 7,  'Research Assistant',     530),
(3, 1,  'Principal Investigator', 380),
(3, 4,  'Research Assistant',     500),
(3, 5,  'Research Assistant',     510),
(3, 10, 'Research Assistant',     460),
(4, 3,  'Principal Investigator', 400),
(4, 8,  'Research Assistant',     540),
(4, 9,  'Research Assistant',     520),
(5, 2,  'Principal Investigator', 300),
(5, 6,  'Research Assistant',     400),
(5, 7,  'Research Assistant',     380),
(5, 12, 'Collaborator',           150),
(6, 3,  'Principal Investigator', 280),
(6, 8,  'Research Assistant',     350),
(6, 9,  'Research Assistant',     340),
(7, 1,  'Principal Investigator', 350),
(7, 4,  'Research Assistant',     480),
(8, 2,  'Principal Investigator', 360),
(8, 6,  'Research Assistant',     490);

-- EQUIPMENT
INSERT INTO EQUIPMENT (EID, E_TYPE, E_NAME, MANUAL) VALUES
(1, 'Computing',    'GPU Cluster Node',         'NVIDIA DGX A100 Operations Manual v2.1'),
(2, 'Computing',    'High Performance Server',  'Dell PowerEdge R750 Setup Guide'),
(3, 'Measurement',  'Oscilloscope',             'Tektronix TDS2024C User Manual'),
(4, 'Imaging',      '3D Scanner',               'Artec Eva 3D Scanner Manual'),
(5, 'Networking',   'Network Switch',           'Cisco Catalyst 9300 Config Guide');

-- DEVICE
INSERT INTO DEVICE (DID, EID, STATUS, P_DATE) VALUES
(1, 1, 'In Use',             '2021-03-15'),
(2, 1, 'In Use',             '2021-03-15'),
(3, 2, 'Available',          '2020-08-10'),
(4, 3, 'In Use',             '2022-01-20'),
(5, 4, 'Under Maintenance',  '2021-11-05'),
(6, 5, 'Available',          '2023-02-28');

-- USES
INSERT INTO USES (MID, DID, EID, S_DATE, E_DATE, PURPOSE) VALUES
(4,  1, 1, '2021-03-20', '2023-06-30', 'Drug discovery model training'),
(5,  1, 1, '2021-04-01', '2024-05-20', 'Neural network experiments'),
(6,  2, 1, '2021-09-01', NULL,         'Quantum simulation runs'),
(7,  2, 1, '2022-01-15', NULL,         'Federated learning experiments'),
(8,  4, 3, '2022-06-15', NULL,         'Signal analysis for smart grid'),
(9,  4, 3, '2022-09-01', '2024-12-31', 'Energy sensor calibration'),
(10, 3, 2, '2023-02-01', '2023-08-30', 'Data preprocessing pipeline');

-- PUBLICATION
INSERT INTO PUBLICATION (PUBID, TITLE, VENUE, DATE, DOI) VALUES
(1,  'Deep Learning for Molecular Property Prediction',         'Nature Machine Intelligence',  '2022-03-15', '10.1038/s42256-022-001'),
(2,  'Quantum Gate Optimization via Reinforcement Learning',    'Physical Review Letters',      '2022-07-20', '10.1103/PhysRevLett.001'),
(3,  'Federated Learning with Differential Privacy',           'NeurIPS 2022',                 '2022-11-30', '10.5555/neurips2022-001'),
(4,  'Energy-Efficient Neural Architecture Search',            'ICML 2022',                    '2022-06-18', '10.5555/icml2022-001'),
(5,  'Gradient Compression for Distributed Training',          'ICLR 2023',                    '2023-05-01', '10.5555/iclr2023-001'),
(6,  'Sparse Quantum Circuit Compilation',                     'Quantum Science and Tech',     '2023-02-14', '10.1088/2058-9565-001'),
(7,  'Smart Grid Anomaly Detection with GNNs',                 'IEEE Transactions',            '2023-08-10', '10.1109/TSG.2023.001'),
(8,  'Privacy-Preserving Multi-Party Computation',             'CCS 2023',                     '2023-11-20', '10.1145/ccs2023-001'),
(9,  'Robust Optimization for Neural Networks',                'NeurIPS 2023',                 '2023-12-05', '10.5555/neurips2023-001'),
(10, 'Transfer Learning in Low-Resource Settings',             'ACL 2024',                     '2024-08-15', '10.5555/acl2024-001'),
(11, 'Autonomous Robot Path Planning with RL',                 'ICRA 2024',                    '2024-05-20', '10.1109/ICRA.2024.001'),
(12, 'Blockchain Consensus for IoT Networks',                  'IEEE IoT Journal',             '2021-09-30', '10.1109/JIOT.2021.001'),
(13, 'Climate Prediction via Ensemble Methods',                'Nature Climate Change',        '2021-12-10', '10.1038/s41558-021-001'),
(14, 'Multi-Agent Reinforcement Learning Survey',              'JMLR 2024',                    '2024-03-01', '10.5555/jmlr2024-001');

-- PUBLISHES
INSERT INTO PUBLISHES (MID, PUBID) VALUES
(4,  1),
(4,  4),
(4,  12),
(5,  1),
(5,  3),
(5,  9),
(6,  2),
(6,  5),
(6,  6),
(7,  3),
(7,  5),
(7,  8),
(8,  7),
(8,  11),
(9,  7),
(9,  13),
(10, 9),
(10, 10),
(10, 14),
(1,  1),
(2,  2),
(3,  7),
(11, 3),
(12, 8);

