-- Task: list cities of California using a subquery
-- This query lists all cities of California ordered by city id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
