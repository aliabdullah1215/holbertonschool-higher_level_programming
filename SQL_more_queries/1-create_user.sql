-- Task: create MySQL user user_0d_1 with full privileges
-- This query creates the user user_0d_1 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- This query grants all privileges to user_0d_1 on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- This query reloads the privilege tables
FLUSH PRIVILEGES;
