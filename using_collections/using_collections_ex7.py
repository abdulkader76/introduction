# 7. Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# Try this problem using the methods you've learned about in this chapter. Once you have that working, use the Python documentation for the str type to find an alternative solution.

# from this chapter
info_list = info.split(':')
print(('+').join(info_list))

# from documentation
print(info.replace(':', "+"))

# ls solution
# from this chapter
info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'

# from documentation
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'