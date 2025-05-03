# bool values use capital
True
False


# numerical comparison
x = 10>9 # True
x = 10==9 # False
print(10!=9) #
# also >= <= !=

# identity operators for objects
x=5
y=10
x is y # checks if these are the same object
x is not y # true if they are different objects

# membership operators
# x in X
# x not in X

# most things cast to true
print(bool("hello"))
bool(5) # true
print(bool([1,2,3,5])) # true

# all false
bool(False)
bool(None)
bool(0)
bool(''), bool("")
bool(()) # empty tuple
bool([]) # empty list
bool({}) # empty map

# many functions return bools
print(isinstance(5, int)) # performs a type comparison

# standard operators + - * /
# % modulus, ** exponentiation, // floor division
print(8.5//2)
print(-8.5//2) # floor always rounds down
print(int(-8.5/2)) # int rounds to zero
# any of the previous operators can be combined with =
x=28
x //= 15
print(x)

# there are also bitwise operators
# & bitwise and
# | bitwise or
# ^ bitwise xor
# ~ bitwise complement
# << zero fill left shift e.g. x<<2 shifts all digits left by two and pads with two zeros
# >> signed right shift, pushes bits to the right and rightmost bits are dropped

# the bitwise operators can also be combined with assignment
x=4
x &= 5 # x = x&5
x ^= 15 # x = x xor 15
x = 120
x <<= 2 # essentially 4x 120
print(x) # 480
print(8|4|2|1) # 1000 or 0100 or 0010 or 0001 = 1111 = 15
print(6|4) # 110 or 010 = 110 = 6