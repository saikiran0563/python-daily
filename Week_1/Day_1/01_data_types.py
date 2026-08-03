# Integer
# Stores whole numbers.

age = 21

print(age)
print(type(age))


# Float
# Stores decimal numbers.

price = 99.99

print(price)
print(type(price))


# Complex
# Stores real and imaginary numbers.

number = 5 + 2j

print(number)
print(type(number))

print(number.real)
print(number.imag)

# String
# Stores text.

name = "Kiran"

print(name)
print(type(name))
print(len(name))


# Different Ways to Create Strings

city = 'Hyderabad'

message = """Welcome
to
Python"""

print(city)
print(message)


# Empty String

text = ""

print(text)
print(type(text))
print(len(text))

# List
# Stores multiple values.
# Lists are mutable.

numbers = [10, 20, 30]

print(numbers)
print(type(numbers))
print(len(numbers))


# List with different data types

data = [21, 99.99, "Kiran", True]

print(data)
print(type(data))


# Empty List

empty_list = []

print(empty_list)
print(type(empty_list))


# Lists are mutable

numbers[0] = 100

print(numbers)

# Tuple
# Stores multiple values.
# Tuples are immutable.

numbers = (10, 20, 30)

print(numbers)
print(type(numbers))
print(len(numbers))


# Tuple with different data types

student = ("Kiran", 21, 95.5, True)

print(student)
print(type(student))


# Empty Tuple

empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

# Range
# Generates a sequence of numbers.

# Starts from 0 and stops before 5
r1 = range(5)

print(r1)
print(type(r1))
print(list(r1))


# Starts from 2 and stops before 8
r2 = range(2, 8)

print(r2)
print(type(r2))
print(list(r2))


# Starts from 2, stops before 12, increments by 2
r3 = range(2, 12, 2)

print(r3)
print(type(r3))
print(list(r3))


# Counts backwards by 2
r4 = range(10, 0, -2)

print(r4)
print(type(r4))
print(list(r4))

# Dictionary
# Stores data in key-value pairs.
# Dictionaries are mutable.

student = {
    "name": "Kiran",
    "age": 21,
    "marks": 95.5,
}

print(student)
print(type(student))
print(len(student))

# Accessing values using keys

print(student["name"])
print(student["age"])

# Dictionary with different data types

data = {
    "name": "Kiran",
    "age": 21,
    "marks": 95.5,
    "is_student": True,
}

print(data)

# Empty Dictionary

empty_dict = {}

print(empty_dict)
print(type(empty_dict))

# Dictionaries are mutable

student["age"] = 22

print(student)


# Set
# Stores unique values.
# Sets are mutable.

numbers = {10, 20, 30}

print(numbers)
print(type(numbers))


# Duplicate values are removed automatically

numbers = {10, 20, 20, 30, 10}

print(numbers)


# Set with different data types

data = {10, "Kiran", True, 99.99}

print(data)


# Empty Set

empty_set = set()

print(empty_set)
print(type(empty_set))

# Frozenset
# Stores unique values.
# Frozensets are immutable.

numbers = frozenset([10, 20, 30])

print(numbers)
print(type(numbers))


# Duplicate values are removed automatically

numbers = frozenset([10, 20, 20, 30, 10])

print(numbers)

# Boolean
# Stores only True or False.

is_student = True
is_logged_in = False

print(is_student)
print(type(is_student))

print(is_logged_in)
print(type(is_logged_in))

# Bytes
# Stores binary data.
# Bytes are immutable.

data = bytes([65, 66, 67])

print(data)
print(type(data))


# Bytearray
# Stores binary data.
# Bytearrays are mutable.

data = bytearray([65, 66, 67])

print(data)
print(type(data))


# Memoryview
# Provides a view of binary data.

data = bytes([65, 66, 67])

view = memoryview(data)

print(view)
print(type(view))

# None
# Represents no value.

value = None

print(value)
print(type(value))