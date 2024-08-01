# Coercion

# Strings to Numbers
# print(int('5'))               # 5
# print(float('3.141592'))      # 3.141592


# Numbers to Strings
# print(str(5))                 # '5'
# print(str(3.141592))          # '3.141592'

# Implicit Coercion

# (Unnecesasry) Explicit coercion

# print(str(3))                 # 3
# print(str(False))             # False
# print(str([1, 2, 3]))         # [1, 2, 3]
# print(str({4, 5, 6}))         # {4, 5, 6}

# Implicit coercion

# print(3)                      # 3
# print(False)                  # False
# print([1, 2, 3])              # [1, 2, 3]
# print({4, 5, 6})              # {4, 5, 6}

# Implicit coercion gotcha

# print(True + True + True)     # 3
# print(True + 1 + 1.0)         # 3.0
# print(False * 5000)           # 0              
