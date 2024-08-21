# 7. Write a find_integers function that returns a list of all the integers from my_tuple:

def find_integers(tuple_pm):
    new_list = list(tuple_pm)
    
    numbers = [ 
        number 
        for number in new_list 
        if type(number) is int
        ]
    
    return numbers

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)
print(integers)                    
# [1, 3, -4]


# ls solution
def find_integers(things):
    return [ element
             for element in things
             if type(element) is int ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                   
# [1, 3, -4]