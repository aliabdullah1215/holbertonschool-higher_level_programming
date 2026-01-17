-- Task: remove records with low score
-- This query deletes all records from second_table with score less than or equal to 5
DELETE FROM second_table
WHERE score <= 5;
