-- LAB 3 - Day 3 - Adding, changing and deleting data

-- E1
INSERT INTO customers (
    customer_id,
    first_name,
    last_name,
    email,
    city,
    joined_date
)
VALUES (
    11,
    'Christian',
    'Norman',
    'cnorm@holdom.com',
    'Stockholm',
    CURRENT_DATE
);

-- E2
INSERT INTO products (product_id, name, category, price, stock)
VALUES
    (13, 'Scarf', 'Accessories', 229.0, 15),
    (14, 'Gloves', 'Accessories', 199.0, 20);

-- E3
-- First create order 16
INSERT INTO orders (order_id, customer_id, order_date, status)
VALUES (16, 7, CURRENT_DATE, 'new');

-- Then create its order item
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179);

-- E4
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (17, 10, 0, 179); -- NOT NULL check and ("quantity" > 0) causes an error: CHECK contraint

-- E5
UPDATE orders
SET status = 'shipped'
WHERE order_id = 12;

-- E6
UPDATE products
SET stock = 50
WHERE product_id = 5;

-- E7
UPDATE products
SET price = price * 1.10
WHERE category = 'Accessories';

-- E8
DELETE FROM order_items
WHERE order_id = 7;

DELETE FROM orders
WHERE order_id = 7;

-- E9 - Revert changes.
