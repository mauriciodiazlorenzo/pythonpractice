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

x = "substring" in "text with a substring contained" # bool
print(x)
print("teststring" not in "some other string") # bool

# subset of the char array may be selected like any other array
x = "a short string of words"
print(x[2:7]) # index 2 to 6, "short"
print(x[:7]) # index 0 to 6, "a short"
print(x[8:])# index 8 to end

x="123456789"
print(x[-1]) # last char
print(x[-3:]) # last 3 chars
print(x[:-3]) # all except last three chars

x = "A Short String of Words"
# upper case
x=x.upper()
print(x)
x=x.lower()
print(x)

x="      trailing space         "
print(x.strip()) # "trailing space" trimmed on both sides
print(x.strip().replace("space","behind")) # "space" replaced by "behind" -> "trailing behind"

x="1,2,3,4,5,6,7"
print(x.split(',')) # turns into an array

x="hello " + "world" # string concatenation with plus operator
print(x)

# escape with backslash
x = 'it\'s a \'free\' world'
print(x)
# \\ backslash, \n newline, \r carriage return, \t tab, \b backspace, \f form feed, \xhh hex val

# there are many other string functions: https://www.w3schools.com/python/python_strings_methods.asp