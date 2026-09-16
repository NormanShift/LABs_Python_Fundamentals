# LAB 6

# Part A - List comprehensions

# A:1

squared_list = [] # First, we initialize an empty list.

for n in range(1, 21):
    squared_list.append(n ** 2) # Then we populate the list

print(squared_list)

# Same but with list comprehension:

squared_list = [n ** 2 for n in range(1, 21)] # Basically we define the operation and the loop inside the list.

print(squared_list)

#--------------------------
# A:2

even_numbers = [n for n in range(1, 21) if n % 2 == 0]

print(even_numbers)

#--------------------------
# A:3

names_list = ["  jimmey  ","  ryu   ","  charlie    "," williams      "]

# for name in names_list:
#     names = name.strip().title()
#     print(names)

# Or:
clean_names = []

for name in names_list:
    clean_names.append(name.strip().title())

print(clean_names)

# Or:
clean_names = [name.strip().title() for name in names_list]

print(clean_names)


# A:4

