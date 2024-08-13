# 2. Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

# tuples are immutable; Python will raise an error when trying to change the values
stuff = ('hello', 'world', 'bye', 'now')

# Function that takes a tuple and adds the elements to a list
def change(stuff):
    empty_list = []
    # iterate over the tuple and add the items to the list unless the item is 'bye', the add 'goodbye
    for i in range(len(stuff)):
        if stuff[i] == 'bye':
            empty_list.append('goodbye')
        else:
            empty_list.append(stuff[i])
    
    # return a tuple of the new list
    return tuple(empty_list)


# assign the new tuple to stuff variables
stuff = change(stuff)
print(stuff)

# launchschool solution
# 1
# stuff = ('hello', 'world', 'goodbye', 'now')

# 2.
# stuff = stuff[0:2] + ('goodbye', stuff[3])

# 3
# stuff = list(stuff)
# stuff[2] = 'goodbye'
# stuff = tuple(stuff)
