# 8. Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# the first line returns a new string from the slice method which creates a copy of the substring - the result is the indexing changes in the string

# the second line uses the find method to search through the original string

