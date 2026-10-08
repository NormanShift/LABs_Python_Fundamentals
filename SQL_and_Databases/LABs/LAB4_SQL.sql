

SELECT first_name, last_name, status
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;



SELECT customers.customer_id, first_name, last_name, status
FROM orders
JOIN customers
	ON orders.customer_id = customers.customer_id
WHERE orders.customer_id = 2;



SELECT first_name, last_name, order_date, city
FROM orders
JOIN customers
	ON orders.customer_id = customers.customer_id
WHERE customers.city = 'Göteborg' ORDER BY order_date DESC;



SELECT p.name, p.category
FROM order_items AS oi
JOIN products AS p 
	ON oi.product_id = p.product_id;



SELECT oi.order_id, p.name
FROM order_items AS oi
JOIN products AS p 
	ON oi.product_id = p.product_id
WHERE p.category = 'Shoes';

