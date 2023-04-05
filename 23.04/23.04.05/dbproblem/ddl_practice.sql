CREATE TABLE users (
  name TEXT NOT null,
  phoneNumber TEXT NOT NULL,
  balance TEXT NOT NULL,
  age INTEGER,
  gender TEXT
);

SELECT name, age, balance FROM users
ORDER BY age, balance DESC;