# 15. Without running the following code, what values will be printed by line 10?

pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# dict_keys(['Cat', 'Bird', 'Snake'])

# ls solution
# dict_keys(['Cat', 'Bird', 'Snake'])

# Since dict.keys returns a dictionary view object, any changes made to the dictionary after you call the keys method will be reflected in dictionary view referenced by keys immediately.