-- Task: list records with a name
-- This query lists score and name from second_table where name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
