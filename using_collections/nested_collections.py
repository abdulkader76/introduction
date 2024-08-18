# Nested Collections

# Collections can be nested in other collections
# e.g

nested_list = [
    { 'foo': 42, 'bar': [1, 2, 3], 'qux': None },
     {
         'Kim',
         ('Leslie', 'Les'),
         ('Pete', 'Peter'),
         ('Jonathan', 'Jon', 'Jack'),
     },
     (4, 5, (1, 2, 3), 6, 7),
     ['a', 'b', 'cde', -3.1415192],
]

# limitations
# add mutable collections in other non-mutable collections will raise an exception

# my_set = {1, 2, 3, [4, 5]}
# TypeError: unhashable type: 'list'

# my_set = {1, 2, 3, {4, 5},}
# TypeError: unhashable type: 'set'

# exceptions
# nest frozenset in a set
# my_set = { 1, 2, 3, frozenset([4, 5])}
# print(my_set)
# {frozenset({4, 5}), 1, 2, 3}

# nest mutable collections in a tuple
# my_tuple = (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'},)
# print(my_tuple)
# (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'})

# nested collection - structure & reason for nesting

deck = [
    {'suit': 'Clubs', 'value': '2'},
    {'suit': 'Clubs', 'value': '3'},
    {'suit': 'Clubs', 'value': '4'},
    {'suit': 'Clubs', 'value': '5'},
    {'suit': 'Clubs', 'value': '6'},
    {'suit': 'Clubs', 'value': '7'},
    {'suit': 'Clubs', 'value': '8'},
    {'suit': 'Clubs', 'value': '9'},
    {'suit': 'Clubs', 'value': '10'},
    {'suit': 'Clubs', 'value': 'Jack'},
    {'suit': 'Clubs', 'value': 'Queen'},
    {'suit': 'Clubs', 'value': 'King'},
    {'suit': 'Clubs', 'value': 'Ace'},
    {'suit': 'Hearts', 'value': '2'},
    {'suit': 'Hearts', 'value': '3'},
    {'suit': 'Hearts', 'value': '4'},
    {'suit': 'Hearts', 'value': '5'},
    {'suit': 'Hearts', 'value': '6'},
    {'suit': 'Hearts', 'value': '7'},
    {'suit': 'Hearts', 'value': '8'},
    {'suit': 'Hearts', 'value': '9'},
    {'suit': 'Hearts', 'value': '10'},
    {'suit': 'Hearts', 'value': 'Jack'},
    {'suit': 'Hearts', 'value': 'Queen'},
    {'suit': 'Hearts', 'value': 'King'},
    {'suit': 'Hearts', 'value': 'Ace'},
    {'suit': 'Diamonds', 'value': '2'},
    {'suit': 'Diamonds', 'value': '3'},
    {'suit': 'Diamonds', 'value': '4'},
    {'suit': 'Diamonds', 'value': '5'},
    {'suit': 'Diamonds', 'value': '6'},
    {'suit': 'Diamonds', 'value': '7'},
    {'suit': 'Diamonds', 'value': '8'},
    {'suit': 'Diamonds', 'value': '9'},
    {'suit': 'Diamonds', 'value': '10'},
    {'suit': 'Diamonds', 'value': 'Jack'},
    {'suit': 'Diamonds', 'value': 'Queen'},
    {'suit': 'Diamonds', 'value': 'King'},
    {'suit': 'Diamonds', 'value': 'Ace'},
    {'suit': 'Spades', 'value': '2'},
    {'suit': 'Spades', 'value': '3'},
    {'suit': 'Spades', 'value': '4'},
    {'suit': 'Spades', 'value': '5'},
    {'suit': 'Spades', 'value': '6'},
    {'suit': 'Spades', 'value': '7'},
    {'suit': 'Spades', 'value': '8'},
    {'suit': 'Spades', 'value': '9'},
    {'suit': 'Spades', 'value': '10'},
    {'suit': 'Spades', 'value': 'Jack'},
    {'suit': 'Spades', 'value': 'Queen'},
    {'suit': 'Spades', 'value': 'King'},
    {'suit': 'Spades', 'value': 'Ace'},
]

print(f"{deck[5]['value']} of {deck[5]['suit']}")
print(len(deck))

# several layers of nesting
# access each nested collection using '[]'

nested_seq = [
    [1, 2, [3, 4, (5, 6, 7, 8)]],
    [9, [10, (11,)]],
    [12, 13, [14, 15, (16, 17)]],
    [18, [19, 20, (21, 22)]],
]

print(nested_seq[1]) # [9, [10, (11,)]]
print(nested_seq[3][0]) # 18
print(nested_seq[0][2][2]) # (5, 6, 7, 8)
print(nested_seq[2][2][2][1]) # 17