Exercises "written anwers" 1, 2 and 14: Design, aggregation and safe code

e1 ("Design"):
I would reference the reviews in a separate collection because, although they belong to and are displayed with the book, the number of reviews can grow without limit.
I would also reference members in a separate collection because members are shared entities that can borrow many books, and their details should not be copied into every book or review.

e2 ("Copies or 'duplicated data'"):
One advantage of copying (or duplicating) the product name into each embedded item in the order’s items array, is that the order can be displayed without first looking up (making a query) every product in the products collection. It also preserves the product name that applied when the order was placed, even if the product is later renamed or removed. Effectively this also becomes a record or historical data (also becomes useful for receipts).
The disadvantage is that product.name is duplicated across potentially many orders, so a change in the products collection will not automatically update the copies in existing order documents. This can lead to inconsistent data if the product names are expected to remain synchronized.

e14: