  # Basic try and except
try:
    number = int("abc")
except ValueError:
    print("Invalid number")


# Multiple exceptions
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# else
try:
    number = int("20")
    result = 100 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)


# finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program finished")


# raise
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount


try:
    print(withdraw(10000, 12000))
except ValueError as e:
    print("Error:", e)


# Exception object using as e
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(type(e))
    print(e)


# Custom exception
class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    return "Valid age"


try:
    result = check_age(20)
except InvalidAgeError as e:
    print("Error:", e)
else:
    print(result)
finally:
    print("Age verification completed")


# Practical divide function
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


try:
    result = divide(10, 2)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)