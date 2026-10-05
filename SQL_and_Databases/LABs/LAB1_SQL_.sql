-- LAB 1 - SQL and Databases

-- 1.
SELECT first_name, email FROM customers;
-- 2.
SELECT * FROM products WHERE category = 'Shoes';
-- 3.
SELECT * FROM customers WHERE city = 'Uppsala';
-- 4.
SELECT * from products WHERE price = 199;
--  .
SELECT * FROM products ORDER BY name;
--  .
SELECT * FROM customers order by joined_date;
--  .
SELECT * from products WHERE stock < 1;

SELECT * FROM customers order by joined_date DESC LIMIT 3;
--  .
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');
--  .
SELECT name AS product_name, price AS price_sek FROM products;


-- Bonus questions
-- B1.
SELECT * FROM products WHERE category IN ('Shoes', 'Clothing') AND (price > 1000);
-- B2.
SELECT name, price, stock, (price * stock) AS stock_value from products WHERE stock > 0 ;
-- B3.
SELECT * FROM customers WHERE first_name LIKE '____';
-- B4.

-- B5.


