# while statement - looking for item
numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index

    index += 1

print(found_item)
# even after the item is found, the loop continues iterating 


# Using break to stop the loop completely
numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break
    index += 1

print(found_item)

