
/*Практическое задание по теме «Операторы, фильтрация, сортировка и ограничение»*/

# 1. Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
# Месяцы заданы в виде списка английских названий (may, august)

DROP DATABASE IF EXISTS shop_r;
CREATE DATABASE shop_r;
USE shop_r;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';

INSERT INTO users (name, birthday_at) VALUES
  ('Геннадий', '1990-10-05'),
  ('Наталья', '1984-11-12'),
  ('Александр', '1985-05-20'),
  ('Сергей', '1988-02-14'),
  ('Иван', '1998-01-12'),
  ('Мария', '1992-08-29');

SELECT * FROM users WHERE MONTHNAME(birthday_at) IN ('May','August');

# 2.Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN 1(5, 1, 2); 
# Отсортируйте записи в порядке, заданном в списке IN.

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название раздела',
  UNIQUE unique_name(name(10))
) COMMENT = 'Разделы интернет-магазина';

INSERT INTO catalogs VALUES
  (NULL, 'Процессоры'),
  (NULL, 'Материнские платы'),
  (NULL, 'Видеокарты'),
  (NULL, 'Жесткие диски'),
  (NULL, 'Оперативная память');

 SELECT * FROM catalogs WHERE id IN (5,1,2) ORDER BY find_in_set(id,'5,1,2');
 
/*Практическое задание теме «Агрегация данных»*/
# 1.Подсчитайте средний возраст пользователей в таблице users. shop

SELECT ROUND(AVG(ABS(TIMESTAMPDIFF(YEAR,NOW(),birthday_at))),2) AS average_age FROM users;

# 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
# Следует учесть, что необходимы дни недели текущего года, а не года рождения.

SELECT birthday_at FROM users;
SELECT DATE_ADD(birthday_at,INTERVAL ABS(TIMESTAMPDIFF(YEAR,NOW(),birthday_at)) YEAR) AS birthday_in_year FROM users;
SELECT COUNT(*) AS amount_of_birthdays,DAYNAME(DATE_ADD(birthday_at,INTERVAL ABS(TIMESTAMPDIFF(YEAR,NOW(),birthday_at)) YEAR)) AS day_of_week FROM users GROUP BY day_of_week;

# 3.Подсчитайте произведение в чисел столбце таблицы.

ALTER TABLE users ADD COLUMN value TINYINT;
INSERT INTO users(value) VALUES (1),(2),(3),(4),(5);
SELECT EXP(SUM(LN(value))) AS mul FROM users;
