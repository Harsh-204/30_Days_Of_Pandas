1# Write your MySQL query statement below
2SELECT  teacher_id, COUNT(DISTINCT subject_id) AS cnt FROM Teacher
3GROUP BY teacher_id