# Function Definition

def greet():
    print("Hello, World!")

greet()


def welcome():
    print("Welcome to Python")

welcome()


# Function with Parameters

def greet(name):
    print("Hello", name)

greet("Kiran")


def square(number):
    print(number * number)

square(5)


def add(a, b):
    print(a + b)

add(10, 20)


# Function with Return

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


def square(number):
    return number * number

print(square(5))


# Function with Default Parameters

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Kiran")


def power(number, exponent=2):
    return number ** exponent

print(power(5))
print(power(5, 3))


# Local Scope

def display_message():
    message = "Hello"
    print(message)

display_message()


# Global Scope

name = "Kiran"

def display_name():
    print(name)

display_name()

print(name)


# Variable Shadowing

name = "Kiran"

def greet():
    name = "Python"
    print(name)

greet()

print(name)


# Mini Project - Simple Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division by Zero:", divide(10, 0))




def maximum(a,b):
    if a> b:
        return a
    else:
        return b
print(maximum(20,35))
def minimum(a,b):
    if a< b:
        return a 
    else:
        return b

print(minimum(20,35))