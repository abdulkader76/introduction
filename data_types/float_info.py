
# In theory, floats can represent any number, with or without a decimal point. In practice, there are limits that can be looked up in the sys.float_info module as follows:

import sys

# The maximum number of digits that can be accurately presented
print(sys.float_info.dig)   # Typically 15

# The largest possible float value
print(sys.float_info.max)   # About 1.8 * (10**308)

# The smallest non-zero positive float value
print(sys.float_info.min)   # About 2.2 * (10**-308)

# large and small floats are printed using scientific notation
print(3.14 * (10**20))      # 3.14e+20
print(3.14 * (10**-20))     # 3.14e-20

# using scientific notation when writing float literals
print(3.14e+20 / 2.72e-15)


# Integers don't the same issue as floating point numbers
print(3 * (10**20))     #300000000000000000000

# Use of scientific notation
print(int(3e+20))       #300000000000000000000