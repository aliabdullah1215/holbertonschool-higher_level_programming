-- Task: create database hbtn_0d_2 and read-only user user_0d_2
-- This query creates the database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- This query creates the user user_0d_2 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- This query grants SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- This query reloads the privilege tables
FLUSH PRIVILEGES;
