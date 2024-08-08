# 6. Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(message):
    new_message = ''
    if (len(message) > 10):
        new_message = message.upper()
    else:
        new_message = message
    
    return new_message

print(all_caps('hello world'))
print(all_caps('goodbye!'))
print(all_caps('Sue Smith'))
print(all_caps('Sue Roberts'))
print(all_caps('Joe Shea'))
print(all_caps('Joe Stevens'))

# launchschool solution:

# def caps_long(string):
#     if len(string) > 10:
#         return string.upper()
#     else:
#         return string

# print(caps_long("Sue Smith"))     # Sue Smith
# print(caps_long("Sue Roberts"))   # SUE ROBERTS
# print(caps_long("Joe Shea"))      # Joe Shea
# print(caps_long("Joe Stevens"))   # JOE STEVENS