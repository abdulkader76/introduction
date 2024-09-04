# Method Chaining

# e.g
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper()

tv_show = tv_show.split()
print(tv_show)

# e.g method chaining
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()
print(tv_show)

# e.g method chaining multiline
letters = 'abcdefghijklmnopqrstuvwxyz'

consonants = (letters.replace('a', '').
                      replace('e', '').
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))

print(consonants)
# bcdfghjklmnpqrstvwxyz

