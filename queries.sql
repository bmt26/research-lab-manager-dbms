SELECT * 
FROM lab_member 
NATURAL JOIN student;

SELECT * 
FROM lab_member 
NATURAL JOIN faculty;

SELECT * 
FROM lab_member 
NATURAL JOIN collaborator;

SELECT *
FROM project;

SELECT *
FROM works;

# Show all projects and their workers
SELECT f2.DEPARTMENT, TITLE, ROLE, COALESCE(MAJOR, f1.DEPARTMENT, AFFILIATION) AS AFFILIATION
FROM project
NATURAL LEFT JOIN works
NATURAL LEFT JOIN student AS s1
NATURAL LEFT JOIN faculty AS f1
NATURAL LEFT JOIN collaborator
LEFT JOIN faculty AS f2
ON project.LEADER = f2.MID;