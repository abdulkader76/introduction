# Short Circuits
# short circuit evaluation is a mechanism used by 'and' or 'or' operators

# e.g 
# is_red(item) and is_portable(item)

# expression will return True is item is red and portable. if either of them is False, then the program will terminate.

# so if the item is not red, Python will not need to evaluate the second result and will terminate the program by returning False.

# This is called short-circuiting



# is_green(item) or has_wheels(item)

# With the 'or' operator, if either one of these items is True, then the overall result will be True. 

# So if the item is green, then
