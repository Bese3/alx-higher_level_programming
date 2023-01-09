-- creates a user and grants specific permission to them
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
