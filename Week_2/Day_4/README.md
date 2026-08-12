# Week 2 Day 4 - Exception Handling

## What is an Exception?

An exception is an error that occurs during program execution and interrupts the normal flow of a program.

Example:

```python
print(10 / 0)
```

This raises a `ZeroDivisionError`.

---

## Syntax Error vs Exception

### Syntax Error

A syntax error occurs when the structure of the program is incorrect.

Example:

```python
if 10 > 5
    print("Yes")
```

### Exception

An exception occurs during execution even though the program structure is valid.

Example:

```python
print(10 / 0)
```

---

## try Block

The `try` block contains code that might cause an exception.

```python
try:
    result = 10 / 0
```

---

## except Block

The `except` block handles the exception and prevents the program from crashing.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

## Multiple except Blocks

We can use different `except` blocks to handle different types of exceptions.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## else Block

The `else` block executes only when no exception occurs in the `try` block.

```python
try:
    number = int("20")
    result = 100 / number

except ValueError:
    print("Invalid number")

else:
    print("Result:", result)
```

Output:

```text
Result: 5.0
```

---

## finally Block

The `finally` block executes whether an exception occurs or not.

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error")

finally:
    print("Done")
```

Output:

```text
Error
Done
```

---

## raise

The `raise` keyword is used to intentionally create an exception.

Example:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
```

Here, if the withdrawal amount is greater than the balance, a `ValueError` is raised.

---

## Exception Object using `as`

We can use `as` to store the exception object in a variable.

```python
try:
    result = 10 / 0

except ZeroDivisionError as e:
    print(type(e))
    print(e)
```

Here:

- `e` contains the exception object.
- `type(e)` gives the type of exception.
- `e` gives the exception message.

---

## Common Built-in Exceptions

| Exception | Meaning |
|---|---|
| `ValueError` | Invalid value |
| `TypeError` | Incompatible data types |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Invalid index |
| `KeyError` | Key does not exist in a dictionary |
| `NameError` | Variable does not exist |
| `FileNotFoundError` | File does not exist |

---

## Custom Exceptions

A custom exception is an exception created by the programmer.

We can create a custom exception by inheriting from the `Exception` class.

```python
class InvalidAgeError(Exception):
    pass
```

We can then raise our custom exception:

```python
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    return "Valid age"
```

And handle it using `except`:

```python
try:
    result = check_age(15)

except InvalidAgeError as e:
    print("Error:", e)
```

Output:

```text
Error: Age must be 18 or above
```

---

## Complete Example

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


try:
    result = divide(10, 2)
    print("Result:", result)

except ValueError as e:
    print("Error:", e)
```

Output:

```text
Result: 5.0
```

If we call:

```python
result = divide(10, 0)
```

the function raises a `ValueError`.

The `except` block catches it.

Output:

```text
Error: Cannot divide by zero
```

---

## Important Difference

### `animal.sound`

References the method.

```python
animal.sound
```

### `animal.sound()`

Calls or executes the method.

```python
animal.sound()
```

Parentheses `()` are required when we want to execute the method.

---

## Key Takeaways

- `try` → contains code that may cause an exception.
- `except` → handles the exception.
- `else` → executes when no exception occurs.
- `finally` → executes whether an exception occurs or not.
- `raise` → intentionally raises an exception.
- `as e` → stores the exception object.
- Custom exceptions → allow us to create our own application-specific errors.
- If an exception occurs and there is no matching `except` block, Python terminates the program and displays the exception.