# cast between number types using int(), float(), complex()
# print(float(complex(5+6j))) # can't cast complex as int or float
print(complex(float(5.134526526))+15289.234325j) # can cast float as complex
print(int(6.9)) # truncates towards zero
print(int(-6.9)) # truncates towards zero
print(5.6E-5+2j) # can use E notation

#python has a built-in random module
import random
print(random.randrange(50,60))
print(random.random()) # 0 to 1 float
# numpy.random is much more rich
