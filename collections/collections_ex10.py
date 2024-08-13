# 10. Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl', 'Max', 'Nick', 'Victor' }

print(names)

# No. The elements are stored in set. Sets are by default unordered collections. 

# To print the names in an alphabetical order, the elements can be copied into a list or a tuple and can be sorted according to unicode characters

# launchschool solution
# This code probably won't print the names alphabetically. Sets, by definition, are unordered collections. Thus, the order in which members are shown when printing or iterating is arbitrary. Bob's code may print the names alphabetically on rare occasions, but it would do so only once every 5040 times.