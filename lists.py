#!/usr/bin/env python3


my_list = []

my_list[len(my_list):] = [10, 20, 30, 40]

print("Before append: ", my_list)

my_list.insert(1, 15)

print(f"inserted 15 at 2: ", my_list)
# Extend list
another_list = [50, 60, 70]

# Appending
my_list.extend(another_list)
print(my_list)

# removing last element
my_list.pop(-1)
print(my_list)

# Sort items
my_list.sort()
print(my_list)

# Find an item
print([x for x in my_list if x == 30])