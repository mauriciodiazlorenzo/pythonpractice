# built-in data types

# text type: str
x = 'this is a str'

# numeric types: int, float, complex
x=complex(5,6) # 5+6i
print(x)
x=5+6j # same as above, note usage of j rather than i

# sequence types: list, tuple, range
x=['apple', 5, 6, 7] # list
x = ('toronto', 'ontario') # tuple of two strings
x = range(10) # range
print(x)

# mapping type: dict
city_to_province = dict(city='toronto',province='ontario')
print(city_to_province)
city_to_province = {'toronto':'ontario'} # shorter form


# set types: set, frozenset
x = {'apple','banana','orange'} # set
x = frozenset({'apple','banana','orange'}) # frozenset

# boolean type
x = bool(1) # casts to true
print(x)
print(x==False)

# binary types: bytes, bytearray, memoryview
x=b'Hello' # bytes
print(x)
x=bytes(8) # bytes
print(x)

x=bytearray(5) # bytearray
print(x)

x=memoryview(bytes(5)) # memoryview
print(x)

# NoneType
x= None
print(x)