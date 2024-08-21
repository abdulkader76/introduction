# Comprehensions

# for & while loops - statements
# comprehensions - expressions

# e.g of comprehensions
# [print(foo) for foo in collection]

# use comprehensions as
# - right side of assignment
# - function argument
# - return value
# - any other place where you can use an expression that evaluates as a list, dict or set
# for loop is the preferred alternative


# list comprehensions
# [ expression for element in iterable if condition ]
# take iterable - create a new list

# [expression for element in iterable if condition]

# e.g list comprehension - transformation
squares = [number * number for number in range(5)]
print(squares)
# [0, 1, 4, 9, 16]


# square comprehension - with a for loop
squares = []

for number in range(5):
    square = number * number
    squares.append(square)

print(squares)
# [0, 1, 4, 9, 16]


# e.g list comprehension - selection
sixes = [number for number in range(100) if number % 6 == 0]
print(sixes)
# [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]

# e.g of selection
multiples_of_6 = [
    number for number in range(20) 
                  if number % 6 == 0
]
print(multiples_of_6)
# [0, 6, 12, 18]


# e.g combining transformation & selection
even_squares = [
                number * number 
                for number in range(10) 
                if number % 2 == 0
                ]
print(even_squares)


# create a list of uppercase names using a dictionary
cats_of_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',
}

uppercase_names = [
    name.upper() 
    for name in cats_of_colors
]
print(uppercase_names)
# ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']


# e.g list comprehension using cat names & color
cats_of_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',
}

uppercase_names = [
    f'{name.upper()}, {color.upper()}' 
    for (name, color) in 
    cats_of_colors.items()
]
print(uppercase_names)
# ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']


# limit the result of cats' names if the color is orange
cats_of_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',
}

names = [
    name.upper() 
    for name in cats_of_colors
    if cats_of_colors[name] == 'orange'
]

print(names)
# ['LEO', 'KAT']

# e.g using multiple selection criteria
cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',
}

names = [
    name.upper()
    for name in cats_colors
    if cats_colors[name] == 'orange'
    if name[0] == 'L'
]

print(names)
# ['LEO']

# e.g of compehension with multiple for loops
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9','10', 'Jack', 'Queen', 'King', 'Ace',
]

deck_of_cards = [
    f'{rank} of {suit}'
    for suit in suits
    for rank in ranks 
]

print(deck_of_cards)

# earlier example of nested loops with deck of cards
suits = [
    'Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)


# often mistaken for tuple expression
squares = ( 
    number * number 
    for number in range(1, 6)
    )

print(squares)
# <generator object <genexpr> at 0x10b713920>
# above mentioned example is a generator expression - tba

# how comprehensions work
# e.g list comprehension
# result = empty_collection     
# [], {}, set()
# for item in collection:
#     result.append(item)

# result starts with an empty collection
# with each iteration, item is added to result
# so in this sense, tuples and frozensets are immutable - Python can't have tuple comprehensions
# use tuple or str constuctors to convert a list comprehension's result 