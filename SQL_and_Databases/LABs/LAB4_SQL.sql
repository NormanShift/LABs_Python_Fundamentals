-- Day 4 - LAB 4 - Joining tables

-- E1
SELECT first_name, last_name, status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;


-- E2
SELECT customers.customer_id, first_name, last_name, status
FROM orders
JOIN customers
	ON orders.customer_id = customers.customer_id
WHERE orders.customer_id = 2;


-- E3
SELECT first_name, last_name, order_date, city
FROM orders
JOIN customers
	ON orders.customer_id = customers.customer_id
WHERE customers.city = 'Göteborg' ORDER BY order_date DESC;


-- E4
SELECT p.name, p.category
FROM order_items AS oi
JOIN products AS p 
	ON oi.product_id = p.product_id;


-- E5
SELECT oi.order_id, p.name
FROM order_items AS oi
JOIN products AS p 
	ON oi.product_id = p.product_id
WHERE p.category = 'Shoes';


-- E6
SELECT
	p.name,
	oi.quantity,
	oi.unit_price,
	oi.quantity * oi.unit_price AS line_total
FROM order_items AS oi
JOIN products AS p ON oi.product_id = p.product_id
WHERE oi.order_id = 10;


-- E7
SELECT
	c.first_name,
	o.order_date
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
JOIN order_items AS oi
    ON o.order_id = oi.order_id
JOIN products AS p
    ON oi.product_id = p.product_id
WHERE p.name = 'Hoodie Black';


-- E8
SELECT
	c.first_name,
	c.last_name,
	o.order_id
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id;



