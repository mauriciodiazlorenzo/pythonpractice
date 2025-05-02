import sys
print(sys.version)

# comment with a hashtag

if 5>2:
    print("indentation is key")

if 5>2:
                    print('this also works') # single or double quote for string literal
    #print("this would not work due to mixed amount of indentation")

"""
extended multiline comment
is just a multiline string
"""

x=5 # variables are created at assignment
y = 'david'
print(x,y)

x=5
x='sally' # type can be changed on the fly
print(x)

# casting
x = str(3) # cast int to string
print(x*10) # string can be multiplied by int
x = int(3) # 3
x= float(3) # 3.0
print(int(5.8)) # truncated down to 5
print(str(5.8)) # '5.8'

# retrieve type with type(x)
print(type(5)) # class 'int'
print(type(5.0)) # class 'float'
print(type('5')) # class 'str'

# variables are case sensitive
x = 'hello'
X = 'world'
print(x,X) # hello world

# variable names must begin with letter or underscore
# only alpha-numeric characters and underscores are permitted
x=5
X=5
_x=5
_x5=5
# 5x = 5 #not permitted
# my-var = 5 #not permitted

myVariableName = 'camelCase'
MyVariableName = 'PascalCase'
my_variable_name = 'snake_case'

# multiple value assignment
x, y, z = "hello", 5, float(7.0)
print(x,y,z)

# single value assignment to multiple vars
x = y = z = 10
print(x,y,z)

# "unpacking" a collection
fruits = ["apple", 6, "banana", 15.5]
x,y,z,a = fruits
print(x,y,z,a)

# all previous variables are global variables, defined outside of a class and function
# they are available for use within a function

def myfunc():
    global y # global variables can also be declared within a function
    y='watermelon'
    print(x)
    locvar = 10 # this local variable only exists in the scope of the function
    z = 200 # defines local var z, distinct from global z

print(z) # prints banana, not 200

# the function ends when indenting returns to normal

#invoke the function
myfunc() # will print(x) i.e. apple

# check if we can access y
print(y) # watermelon, not y=6
# print(locvar) # undefined in this scope

# the plus operator concatenates strings
print('concatenated ' + 'sentence ' + 'of strings')