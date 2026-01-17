-- Task: list all cities with their state names
-- This query lists cities with their corresponding states ordered by city id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
