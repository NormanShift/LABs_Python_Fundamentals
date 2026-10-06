-- LAB2 - SQL and Databases - Day 2 Exercises

-- E1.
CREATE TABLE books(
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT NOT NULL,
	year INTEGER
)

-- E2.
DROP TABLE books

CREATE TABLE books(
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT NOT NULL,
	year INTEGER CHECK (year > 1400)
)

-- E3.
ALTER TABLE books ADD isbn TEXT

-- E4.
DROP TABLE books

-- E5.
CREATE table reviews(
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER NOT NULL,
	rating INTEGER CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	FOREIGN KEY (product_id) REFERENCES products(product_id)
)

-- E6.
INSERT INTO reviews VALUES (1, 12, 5, 'Great!!!');

-- E7.
