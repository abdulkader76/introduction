# Controlling Loops

# continuing a loop with next iteration
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)
# ['CHRIS', 'KARIS', 'VICTOR']


# rewrite the names loop with a negated if 
names = ['Matthias', 'Noussair', 'Lenny', 'Joshua', 'Manuel']
upper_names = []

for name in names:
    if name != 'Manuel':
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names)
# ['MATTHIAS', 'NOUSSAIR', 'LENNY', 'JOSHUA']

# without continue, loops can get cluttered with nested logic
# for value in collection:
#     if some_condition():
#         # some code here
#         if some_condition():
#             # some code here

# use continue to rewrite above nested loop
# for value in collection:
#     if not some_condition():
#         continue

#     # some code here

#     if not another_condition():
#         continue

#    # some more code here


# Breaking Loops
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


# Emulating do/while loops

# dp/while loop prototype
# while some condition is truthy
#     do some work

# do some work at least once - even if condition is falsy
# do some work
# while some condition is truthy 

# do/while or do/until loop in other programming languages
# in Python - take a different approach
# do some work
#   if some condition is falsy
#       break

# usually in interactive programs where you need to 

# e.g
# keep_going = True
# while keep_going:
#     # main loop code here

#     answer = input('Play again? (y/n) ')
#     if answer == 'n':
#         keep_going = False

# above example is a little cluttered
# a slightly more shorter work around
while True:
    # main loop code is here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break
