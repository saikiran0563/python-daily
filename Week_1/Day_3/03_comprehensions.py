# List Comprehension

numbers = [1, 2, 3, 4, 5]

# Square of each number
squares = [num * num for num in numbers]

print("Squares:", squares)


# Conditional List Comprehension

numbers = [1, 2, 3, 4, 5, 6]

# Even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)

# Odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Odd Numbers:", odd_numbers)


# Dictionary Comprehension

numbers = [1, 2, 3, 4]

# Number -> Square
square_dict = {num: num * num for num in numbers}

print("Square Dictionary:", square_dict)

names = ["Kiran", "Sai", "Rahul"]

# Name -> Length
name_length = {name: len(name) for name in names}

print("Name Length:", name_length)


# Set Comprehension

numbers = [1, 2, 2, 3, 3, 4]

# Unique values
unique_numbers = {num for num in numbers}

print("Unique Numbers:", unique_numbers)

# Square values
square_set = {num * num for num in numbers}

print("Square Set:", square_set)


# Mini Project - Student Marks Filter

students = {
    "Kiran": 85,
    "Sai": 42,
    "Rahul": 91,
    "Anu": 38,
    "Priya": 76
}

# Students who passed
passed_students = {
    name: marks
    for name, marks in students.items()
    if marks >= 40
}

print("Passed Students:", passed_students)

# Student Grades
grades = [
    f"{name} - {'A' if marks >= 80 else 'B' if marks >= 60 else 'C'}"
    for name, marks in students.items()
]

print("Grades:", grades)

employees = {
    "Alice": 50000,
    "Bob": 35000,
    "Charlie": 70000,
    "David": 45000
}

emp ={name: salary for name,salary in employees.items() if salary >= 45000}
print(emp)

upper_emp = [name.upper() for name, salary in employees.items()]

print(upper_emp)