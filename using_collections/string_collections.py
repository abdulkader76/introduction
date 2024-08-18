# String Collections

# Letter Case

# str.capitalize() - returns uppercase of the first character in a string
# the return value is a copy, strings themselves are immutable

print("what's up?".capitalize())
print('456abc'.capitalize())

# str.title - returns copy of every word in string capitalized
print('four SCORE and sEvEn'.title())

# str.title - uses whitespace and punctuation as word boundaries - which leads to unexpected results
print("i can't believe it's already mid-july.".title())
# I Can't Believe It'S Already Mid-July

# use capwords - for only capitalizing words after whitespace
import string
print(string.capwords("i can't believe it's already mid-july."))

# str.startswith - returns True / Fase
'Four score and seven'.startswith('Four score') # True
'Four score and seven'.startswith('For score') # False
'Four score and seven'.startswith('score') # False


# str.startswith - argument can also be tuple of strings
'abc def'.startswith(('abc', 'xyz', 'stu')) # True
'def ghu'.startswith(('abc', 'xyz', 'stu'))
# False
'xyz uvw'.startswith(('abc', 'xyz', 'stu'))
# True
'stu vwx'.startswith(('abc', 'xyz', 'stu'))
# True

'abc def'.startswith('def', 4)  # True
'abc def ghi'.startswith('def', 4, 7) # True

# str.endswith - inverse of starts
'Four score and seven'.endswith('and seven') # True
'Four score and seven'.endswith('ad seven') # False
'Four score and seven'.endswith('score')
# False

# add tuple of strings as arguments
'abc def'.endswith(('abc', 'xyz', 'stu')) # False
'abc def'.endswith(('xyz', 'def'))
# True
'abc def'.endswith('def', 4) # True
'abc def ghi'.endswith('def', 4, 7) # True

# str.swapcase - returns upper to lower & lower to upper
print("What's up?".swapcase()) 
# wHAT'S UP?
print('456ABC'.swapcase())
# 456abc
print('455ABC'.swapcase().swapcase())
# 456ABC

print('Straße'.swapcase().swapcase())
# Strasse
# the german character eszet character represents a double lower case s (ss) does not have an uppercase counterpart.
# thus, the string 'Strasse' is returned


# Character Classification

# str.isalpha() - True if all characters are alphabets
'Hello'.isalpha()       # True
'Good-bye'.isalpha()    # False
'Four Score'.isalpha()  # False
''.isalpha()            # False

# str.isdigit() - True if all characters are digits
'12340'.isdigit()       # True
'123.4'.isdigit()      # False
'-1234'.isdigit()       # False
''.isdigit()            # False

# str.isalnum() - True is all characters are alphabets or digits

# str.islower() - True if all cased characters are lower case

# str.upper() - True if all characters are characters are upper case

# str.isspace() - True if all characters in str are whitespace
# False if string is empty
# whitespace ( ), ( \t), ( \n), ( \r), ( \v) ( \f)

# above methods are unicode aware
# to exclude non-ASCII characters
# text.isalpha() and text.isascii()


# Stripping Characters

# str.strip returns copy of string by removing leading and trailing white spaces

# text = input(prompt).strip()

# use repr to show explicit string representation

# text = ' \t   abc def   \n\r'
# print(repr(text))     # ' \t   abc def   \n\r'
# print(repr(text.strip())) # 'abc def'

# strip remove leading and trailing whitespace by default
# strip also removes strings when they are provided as string arguments

# text = ' \t  abc def   \n\r'
# print(repr(text.strip('abc')))
# ' \t  abc def   \n\r'

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))  # 'baacccabxyzabccb'
print(text.strip('ab')) # 'cccabxyzabcc'
print(text.strip('ba')) # 'cccabxyzabcc'
print(text.strip('abc')) # 'xyz'
print(text.strip('bc')) # 
# aaabaacccabxyzabccba

print(repr(text.strip('abcxyz'))) # ''

# str.lstrip() - removes whitspace on the left
# str.rstrip() - removes whitespace on the right

text = 'aaabaacccabxyzabccba'

print(text.lstrip('a'))
print(text.rstrip('a'))

print(text.lstrip('ab'))
print(text.rstrip('ab'))

print(text.lstrip('ba'))
print(text.rstrip('ba'))

print(text.lstrip('abc'))
print(text.rstrip('abc'))


# Splitting and Joining Strings
# str.split() - returns a list of words separated by one or more whitespace

text = ' Four   score and    seven years ago.'
print(text.split())
print('no-spaces'.split())

text = ',Four,score,and,,,seven,years,ago,'
print(text.split(','))


# delimiter argument splits the string at every occurence of the delimiter

text = '  Four    score and    seven years ago.'
print(text.split(' '))

# split recognizes multi-character delimiters
text = 'Four<>score<:>and<>seven<>years<>ago.'
print(text.split('<>'))

# Python doesn't split  a string into individual characters
# to split a string into individual characters - use list or tuple

text = 'abcde'
print(list(text))
print(tuple(text))

# iterate over each string character
text = 'abcde'
for char in text:
    print(char)


# str.splitlines - returns list of lines
text = '''
You were lucky to have a room. We used to have to
live in a corridor.
Oh we used to dream of livin' in a corridor!
Woulda' been a palace to us. We used to live in an
old water tank on a rubbish tip. We got woken up
every morning by having a load of rotting fish
dumped all over us.
'''

print(text.splitlines())
lines = text.splitlines()

for line in lines:
    print(line)


# str.join - concatenates strings in a iterable collection

words = ['You', 'were', 'lucky']
print(''.join(words))
print(' '.join(words))
print(','.join(words))
print('\n  '.join(words))


# Finding Substrings

# str.find & str.rfind - search through the first occurrence of the argument
# str.find - goes from left to right
# str.rfind - goes from right to left

school = 'launch school'
print(school.find(' ')) # 6
print(school.find('l')) # 0
print(school.find('h')) # 5
print(school.find('hoo')) # 9
print(school.find('x')) # -1
print(school.find('N')) # -1

print(school.rfind(' '))    # 6
print(school.rfind('l'))    # 12
print(school.rfind('h'))    # 9
print(school.rfind('hoo'))  # 9
print(school.rfind('oh'))   # -1
print(school.rfind('N'))    # -1


# add start & end arguments to the function call

text = 'abc abc def abc'

print(text.find(' ', 4))    # 7
print(text.find(' ', 8))    # 11

print(text.find('c', 0, 2))     # -1
print(text.find('c', 3, 10))    # 6

# using find / rfind to search slices
# using [start:stop] syntax does not yield the same results

# e.g.
text = 'abc abc def abc'
print(text[3:10].find('c'))     # 3
print(text.find('c', 3, 10))    # 6

# difference is - starting point of slices changes when using find on a sliced string
# 2nd difference - slice returns a new copy of a string 