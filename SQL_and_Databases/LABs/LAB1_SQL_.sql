-- LAB 1 - SQL and Databases

-- 1.
SELECT first_name, email FROM customers;
-- 2.
SELECT * FROM products WHERE category = 'Shoes';
-- 3.
SELECT * FROM customers WHERE city = 'Uppsala';
-- 4.
SELECT * from products WHERE price = 199;
-- 5.
SELECT * FROM products ORDER BY name;
-- 6.
SELECT * FROM customers order by joined_date;
-- 7.
SELECT * from products WHERE stock < 1;
-- 8.
SELECT * FROM customers order by joined_date DESC LIMIT 3;
-- 9.
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');
-- 10.
SELECT name AS product_name, price AS price_sek FROM products;


-- Bonus questions
-- B1.
SELECT * FROM products WHERE category IN ('Shoes', 'Clothing') AND (price > 1000);
-- B2.
SELECT name, price, stock, (price * stock) AS stock_value from products WHERE stock > 0 ;
-- B3.
SELECT * FROM customers WHERE first_name LIKE '____';
-- B4.
SELECT * FROM products ORDER BY price ASC LIMIT 5, 5;
-- B5.
SELECT * FROM customers WHERE joined_date < '2025-01-01' AND city != 'Uppsala' ORDER BY city, last_name;




SELECT * FROM products WHERE name LIKE '% %' AND stock > 0 AND category IS NOT 'Accessories' ORDER BY category ASC, price DESC;