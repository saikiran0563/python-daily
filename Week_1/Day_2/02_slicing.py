# Indexing
# Access a single element using its index.

word = "Python"

# Positive Indexing
print(word[0])
print(word[1])
print(word[2])

# Negative Indexing
print(word[-1])
print(word[-2])
print(word[-3])


# String Slicing

word = "Python"

# start : stop

print(word[0:3])     # Pyt
print(word[2:6])     # thon
print(word[1:4])     # yth

# Missing start

print(word[:4])      # Pyth

# Missing stop

print(word[2:])      # thon

# Entire string

print(word[:])       # Python


# Step Slicing

word = "Python"

# Take every 2nd character
print(word[0:6:2])   # Pto

# Start at index 1, take every 2nd character
print(word[1:6:2])   # yhn

# Take every 2nd character from the whole string
print(word[::2])     # Pto

# Reverse the string
print(word[::-1])    # nohtyP


# List Slicing

numbers = [10, 20, 30, 40, 50, 60]

# Basic slicing
print(numbers[1:4])      # [20, 30, 40]

# From beginning
print(numbers[:3])       # [10, 20, 30]

# Till end
print(numbers[3:])       # [40, 50, 60]

# Every second element
print(numbers[::2])      # [10, 30, 50]

# Reverse the list
print(numbers[::-1])     # [60, 50, 40, 30, 20, 10]



# Tuple Slicing

numbers = (10, 20, 30, 40, 50, 60)

# Basic slicing
print(numbers[1:4])      # (20, 30, 40)

# From beginning
print(numbers[:3])       # (10, 20, 30)

# Till end
print(numbers[3:])       # (40, 50, 60)

# Every second element
print(numbers[::2])      # (10, 30, 50)

# Reverse the tuple
print(numbers[::-1])     # (60, 50, 40, 30, 20, 10)



