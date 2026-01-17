-- Task: create table force_name with non-null name
-- This query creates the table force_name with a NOT NULL name column
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
