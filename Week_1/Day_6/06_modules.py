# Built-in Module

import math

print(math.sqrt(25))
print(math.factorial(5))


# Import Specific Function

from math import sqrt

print(sqrt(36))


# Import Using Alias

import math as m

print(m.sqrt(49))


# random Module

import random

print(random.randint(1, 10))

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(random.choice(fruits))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)


# datetime Module

from datetime import date
from datetime import datetime

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)

now = datetime.now()

print(now)


# User-Defined Module

import calculator

print("Addition:", calculator.add(20, 10))
print("Subtraction:", calculator.subtract(20, 10))
print("Multiplication:", calculator.multiply(20, 10))
print("Division:", calculator.divide(20, 10))
print("Division by Zero:", calculator.divide(20, 0))


# Student Module

import student

print(student.student_name("Kiran"))
print(student.student_branch("CSE"))
print(student.student_rollno(18))