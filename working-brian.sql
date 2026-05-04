SELECT COLUMN_NAME
FROM (
    SELECT 
        COLUMN_NAME, 
        MIN(CASE WHEN TABLE_NAME = 'lab_member' THEN 1 ELSE 2 END) AS table_priority,
        MIN(ORDINAL_POSITION) AS position_priority
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME IN ('lab_member', 'student')
    GROUP BY COLUMN_NAME
) AS C
ORDER BY table_priority, position_priority;