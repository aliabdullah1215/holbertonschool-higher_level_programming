-- Task: list records with score greater or equal to 10
-- This query lists score and name from second_table where score >= 10 ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
