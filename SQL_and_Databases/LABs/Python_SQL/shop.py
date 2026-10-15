import sqlite3


def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Invalid input. Price must be a number and stock must be a whole number.")
        return
    
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock(conn):
    product_id = int(input("Product ID: "))
    new_stock = int(input("Stock: "))
    
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, product_id)
    )
    conn.commit()
    print("Saved!")

def show_receipt(conn):
    order_id = int(input("Order ID: "))

    cursor = conn.execute("""
        SELECT products.name,
               order_items.quantity,
               order_items.unit_price
        FROM order_items
        JOIN products
            ON order_items.product_id = products.product_id
        WHERE order_items.order_id = ?
    """, (order_id,))

    rows = cursor.fetchall()

    if not rows:
        print("Order not found, or the order has no items.")
        return

    total = 0

    print(f"\nReceipt for order {order_id}")
    print("-" * 52)

    for name, quantity, unit_price in rows:
        line_total = quantity * unit_price
        total += line_total

        print(
            f"{name:<20} "
            f"{quantity:>3} x "
            f"{unit_price:>8.2f} kr = "
            f"{line_total:>8.2f} kr"
        )

    print("-" * 52)
    print(f"{'Total:':>41} {total:>8.2f} kr")

def list_top_3(conn):
    cursor = conn.execute("""
        SELECT products.name, SUM(order_items.quantity) AS total_sold
        FROM order_items
        JOIN products
            ON order_items.product_id = products.product_id
        GROUP BY products.product_id, products.name
        ORDER BY total_sold DESC
        LIMIT 3
    """)

    for name, total_sold in cursor.fetchall():
        print(f"{name:<20} {total_sold:>3} sold")



def main():
    conn = connect()
    while True:
        print("\n1) List products\n2) Search customers\n3) Add product\n4) Change stock\n5) Show orders receipt\n6) Top 3 best-selling products\n0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            list_top_3(conn)
        elif choice == "0":
            break
    conn.close()


main()
