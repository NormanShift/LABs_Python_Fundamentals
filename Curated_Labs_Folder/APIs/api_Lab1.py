# API-exercises - HT 2026 (October 19)

import requests

from api_client import get_json

""" # General get JSON function from todays class:
def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("The request took too long")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")

    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")

    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")

    except requests.exceptions.RequestException as error:
        print(f"Something else went wrong: {type(error).__name__}")

    return None """


""" # t1:

url = "https://fakestoreapi.com/products"
products = get_json(url)

if products is not None:
    sorted_products = sorted(products, key=lambda product: product["price"])

    for product in sorted_products:
        print(f'${product["price"]:.2f} - {product["title"]}') """


""" # t2:

categories_url = "https://fakestoreapi.com/products/categories"
categories = get_json(categories_url)

if categories is not None:
    print("Available categories:")

    for category in categories:
        print(category)

    selected_category = input("\nChoose a category: ").strip()

    category_url = (
        f"https://fakestoreapi.com/products/category/{selected_category}"
    )
    category_products = get_json(category_url)

    if category_products:
        cheapest_product = min(
            category_products,
            key=lambda product: product["price"]
        )

        print(f"\nNumber of products: {len(category_products)}")
        print(
            f'Cheapest product: {cheapest_product["title"]} '
            f'(${cheapest_product["price"]:.2f})'
        )
    else:
        print("The category does not exist or contains no products.") """


# t3: See separate file api_client.py (also imported into this file)

""" # t4:

# Task 4: Create a new product

new_product = {
    "title": "Mechanical Keyboard",
    "price": 89.99,
    "description": "A mechanical keyboard with backlit keys",
    "image": "https://example.com/keyboard.jpg",
    "category": "electronics"
}

try:
    response = requests.post(
        "https://fakestoreapi.com/products",
        json=new_product,
        timeout=5
    )

    response.raise_for_status()

    print(f"POST status code: {response.status_code}")
    print("Created product:")
    print(response.json())

except requests.exceptions.RequestException as error:
    print(f"Could not create the product: {error}")



# Raise the price of an existing product (below)

updated_price = {
    "price": 79.99
}

try:
    response = requests.patch(
        "https://fakestoreapi.com/products/7",
        json=updated_price,
        timeout=5
    )

    response.raise_for_status()

    print(f"\nPATCH status code: {response.status_code}")
    print("Updated product:")
    print(response.json())

except requests.exceptions.RequestException as error:
    print(f"Could not update the product: {error}") """



# t5:

print("\n1. Testing a wrong URL:")
get_json("https://fakestoreapi.com/this-does-not-exist")

print("\n2. Testing an extremely short timeout:")
get_json(
    "https://fakestoreapi.com/products",
    timeout=0.001
)

print("\n3. Testing a made-up domain:")
get_json("https://this-domain-does-not-exist-12345.com")