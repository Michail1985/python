CREATE DATABASE example;
USE example;
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));
SELECT * FROM users;
insert users values (1, 'User1');
insert users values (2, 'User2');
SELECT * FROM users;