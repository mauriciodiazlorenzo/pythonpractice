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

print('hello'=="hello") # double and single quotes are equivalent
print("it's working") # single quote within double quote
print('my name is "Mauricio"')
x= """ multiline string 
with triple quotes"""
x='''multiline
string'''
print(x)

mystring="a string is a char array"
print(mystring[-1]) # print last char
mystring = "abcdef"
for x in mystring: # iterate through the chars in mystring
    print(x)
print(len(mystring)) # number of chars in string