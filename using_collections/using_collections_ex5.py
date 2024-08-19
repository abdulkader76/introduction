# 5. Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']  # NA
{'a': 1, 'b': 2} # NA
range(5)
{1, 4, 9, 16, 25} # NA
3
0.0
frozenset({1, 4, 9, 16, 25})

# dict keys must be hashable objects - immutable objects - strings, integers, floats, tuples and frozensets are immutable

# ls solution
# ['a', 'b']
# {'a': 1, 'b': 2}
# {1, 4, 9, 16, 25}


