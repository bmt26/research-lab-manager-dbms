-- 1. Show members currently using a given piece of equipment
--    and the projects they are working on.
SELECT
    lm.MID,
    lm.NAME AS member_name,
    e.E_NAME AS equipment_name,
    p.TITLE AS project_title,
    u.PURPOSE AS usage_purpose
FROM USES u
JOIN LAB_MEMBER lm ON u.MID = lm.MID
JOIN DEVICE d ON u.DID = d.DID AND u.EID = d.EID
JOIN EQUIPMENT e ON d.EID = e.EID
JOIN WORKS w ON lm.MID = w.MID
JOIN PROJECT p ON w.PID = p.PID
WHERE e.EID = 1
  AND u.E_DATE IS NULL;


-- 2. Top 5 projects by total grant funding in decreasing order.
SELECT
    p.PID,
    p.TITLE AS project_title,
    SUM(g.BUDGET) AS total_funding
FROM PROJECT p
JOIN `GRANT` g ON p.PID = g.PID
GROUP BY p.PID, p.TITLE
ORDER BY total_funding DESC
LIMIT 5;


-- 3. Mentor(s) whose mentees collectively produced the most publications.
WITH mentee_pub_counts AS (
    SELECT
        lm.MENTOR AS mentor_mid,
        COUNT(pub.PUBID) AS total_publications
    FROM LAB_MEMBER lm
    JOIN PUBLISHES pub ON lm.MID = pub.MID
    WHERE lm.MENTOR IS NOT NULL
    GROUP BY lm.MENTOR
)
SELECT
    mentor.MID,
    mentor.NAME AS mentor_name,
    mpc.total_publications
FROM mentee_pub_counts mpc
JOIN LAB_MEMBER mentor ON mpc.mentor_mid = mentor.MID
WHERE mpc.total_publications = (
    SELECT MAX(total_publications) FROM mentee_pub_counts
);


-- 4. Total student publications per major and per publication year.
SELECT
    s.MAJOR,
    YEAR(pub.DATE) AS publication_year,
    COUNT(DISTINCT pl.PUBID) AS total_publications
FROM STUDENT s
JOIN PUBLISHES pl ON s.MID = pl.MID
JOIN PUBLICATION pub ON pl.PUBID = pub.PUBID
GROUP BY s.MAJOR, YEAR(pub.DATE)
ORDER BY s.MAJOR, publication_year;


-- 5. Projects that ended before a given date and their grant counts.
SELECT
    p.PID,
    p.TITLE AS project_title,
    p.E_DATE AS end_date,
    COUNT(g.GID) AS grant_count
FROM PROJECT p
LEFT JOIN `GRANT` g ON p.PID = g.PID
WHERE p.E_DATE < '2023-01-01'
GROUP BY p.PID, p.TITLE, p.E_DATE
ORDER BY p.E_DATE;


-- 6. Three most productive years by student publications.
SELECT
    YEAR(pub.DATE) AS publication_year,
    COUNT(DISTINCT pl.PUBID) AS total_publications
FROM STUDENT s
JOIN PUBLISHES pl ON s.MID = pl.MID
JOIN PUBLICATION pub ON pl.PUBID = pub.PUBID
GROUP BY YEAR(pub.DATE)
ORDER BY total_publications DESC
LIMIT 3;