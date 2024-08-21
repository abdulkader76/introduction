# 3. Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

# use while loop to print the numbers in my_list
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1

# use for loop to print all numbers in my_list 

for number in my_list:
    print(number)


# ls solution
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1

my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    print(number)