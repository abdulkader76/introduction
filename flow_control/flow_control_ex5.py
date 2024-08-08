# 5. What does this code output and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# output: Empty
# the expression is_list_empty([]) is falsy. Empty collections are falsy so the output will print 'Empty'.