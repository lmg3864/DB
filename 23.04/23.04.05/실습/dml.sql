CREATE TABLE users (
  first_name TEXT NOT null,
  last_name TEXT NOT null,
  age INTEGER NOT null,
  country TEXT NOT null,
  phone TEXT NOT null,
  balance INTEGER NOT null
);

SELECT * FROM users;
-- 이름과 나이 컬럼만 조회하기
SELECT first_name, age FROM users;
-- rowid와 이름 컬럼 조회하기
SELECT rowid, first_name FROM users;
-- 이름과 나이를 나이가 어린 순서대로 조회
SELECT first_name, age FROM users ORDER BY age;
-- 이름, 나이, 잔고를 나이가 작은 순서로
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;

-- 조회 결과 중복 제거하는 방법 DISTINCT
SELECT DISTINCT country FROM users ORDER BY country;

-- 조회 컬럼이 2개 이상인 경우
SELECT DISTINCT first_name, country FROM users;

SELECT DISTINCT first_name, country
FROM users
ORDER BY country;

-- 특정한 조건을 만족하는 결과
-- WHERE 절 사용 (IF문)
SELECT first_name, age, balance
FROM users
WHERE age >= 30;

-- 조건이 여러개인 경우 or, and 사용
SELECT first_name, age, balance
FROM users
WHERE age >= 30 AND balance > 500000;

SELECT first_name, age, balance
FROM users
ORDER BY age
LIMIT 10 OFFSET 10;