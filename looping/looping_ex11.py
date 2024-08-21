# 11. Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    index_2 = 0
    while index_2 < len(my_list[index]):
        number = my_list[index][index_2]
        if number % 2 == 0:
            print(number)
        index_2 += 1
    index += 1


# ls solution
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1
