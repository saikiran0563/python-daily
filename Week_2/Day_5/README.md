# Week 2 Day 5 - Context Managers

## What is a Context Manager?

A context manager is an object that manages the setup and cleanup of a resource.

It is commonly used for resources such as:

- Files
- Database connections
- Network connections
- Locks

Context managers make sure that resources are properly cleaned up, even if an exception occurs.

---

## Why Do We Need Context Managers?

Without a context manager, we may need to manually clean up a resource.

Example:

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

If an exception occurs before `file.close()`, the file may remain open.

A context manager handles the cleanup automatically.

---

## The `with` Statement

The `with` statement is used to work with a context manager.

Example:

```python
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
```

The file is automatically closed when the `with` block ends.

Even if an exception occurs inside the block, the cleanup is performed.

---

## Understanding `with open()`

Consider:

```python
with open("data.txt", "r") as file:
    print(file.read())
```

Here:

- `with` starts the context.
- `open("data.txt", "r")` opens the file in read mode and returns a file object.
- `as file` stores the returned file object in the variable `file`.
- When the `with` block ends, the file is automatically closed.

---

## `__enter__()` and `__exit__()`

A class can be used as a context manager by defining two special methods:

```python
__enter__()
__exit__()
```

Example:

```python
class MyContext:
    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")


with MyContext():
    print("Inside context")
```

Output:

```text
Entering Context
Inside context
Exiting Context
```

### `__enter__()`

`__enter__()` runs when entering the `with` block.

It is generally used for setup or acquiring a resource.

### `__exit__()`

`__exit__()` runs when leaving the `with` block.

It is generally used for cleanup or releasing a resource.

---

## Context Manager Execution Flow

```text
with MyContext()
        ↓
    __enter__()
        ↓
   with block
        ↓
    __exit__()
```

---

## What Happens When an Exception Occurs?

`__exit__()` is still called when an exception occurs inside the `with` block.

Example:

```python
class MyContext:
    def __enter__(self):
        print("Entering Context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")


with MyContext():
    print("Inside context")
    x = 10 / 0
```

Output:

```text
Entering Context
Inside context
Exiting Context
Traceback ...
ZeroDivisionError: division by zero
```

The `ZeroDivisionError` continues because `__exit__()` does not return `True`.

The important point is:

> Cleanup happens even when an exception occurs.

---

## `__exit__()` Parameters

The `__exit__()` method can receive three important parameters:

```python
def __exit__(self, exc_type, exc_value, traceback):
```

### `exc_type`

Contains the type of the exception.

Example:

```text
ZeroDivisionError
```

### `exc_value`

Contains the exception object/value.

Example:

```text
division by zero
```

### `traceback`

Contains information about where the exception occurred and the call stack.

If no exception occurs, all three values are:

```python
None
```

So:

```text
exc_type    → None
exc_value   → None
traceback   → None
```

---

## Exception Suppression

Normally, if `__exit__()` returns `None` or `False`, the exception continues.

Example:

```python
class MyContext:
    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup")


with MyContext():
    x = 10 / 0
```

The exception continues after `__exit__()`.

However, if `__exit__()` returns `True`, the exception is suppressed.

Example:

```python
class MyContext:
    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup")
        return True


with MyContext():
    x = 10 / 0

print("Program continues")
```

Output:

```text
Start
Cleanup
Program continues
```

Because `__exit__()` returned `True`, the `ZeroDivisionError` was suppressed.

---

## Creating a Custom Context Manager

We can create our own context manager using a class.

Example:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")


with FileManager("data.txt", "w") as file:
    file.write("Hello Python")
```

### Execution Flow

```text
FileManager("data.txt", "w")
        ↓
__init__()
        ↓
Stores filename and mode
        ↓
__enter__()
        ↓
Opens the file
        ↓
Returns the file object
        ↓
as file
        ↓
file.write()
        ↓
__exit__()
        ↓
Closes the file
```

---

## `@contextmanager`

Python provides the `contextlib` module to create context managers more easily.

Example:

```python
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Start")
    yield
    print("End")


with my_context():
    print("Inside")
```

Output:

```text
Start
Inside
End
```

---

## What Does `yield` Do in a Context Manager?

When using `@contextmanager`, `yield` gives control to the code inside the `with` block.

Example:

```python
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Start")
    yield
    print("End")
```

The execution is:

```text
Before yield → Setup
      ↓
    yield
      ↓
With block runs
      ↓
After yield → Cleanup
```

So:

```python
print("Start")
```

is the setup.

```python
yield
```

gives control to the `with` block.

```python
print("End")
```

is the cleanup.

---

## Context Manager with an Exception

Example:

```python
from contextlib import contextmanager


@contextmanager
def test():
    print("Start")
    yield
    print("Cleanup")


with test():
    print("Before")
    raise ValueError("Something went wrong")
    print("After")
```

Output:

```text
Start
Before
Cleanup
Traceback ...
ValueError: Something went wrong
```

`"After"` is not printed because the exception occurs before that statement.

`"Cleanup"` is printed because the code after `yield` is executed during the context manager's exit process.

The `ValueError` continues because the context manager does not suppress it.

---

## Context Managers and Exception Handling

The general flow is:

```text
Enter context
      ↓
Run with block
      ↓
Exception occurs?
      ↓
Yes
      ↓
__exit__()
      ↓
Exception suppressed?
   ↙          ↘
 Yes           No
  ↓             ↓
Continue     Exception
             propagates
```

---

## Practice Code

```python
class MyContext:
    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")


with MyContext():
    print("Inside context")
```

Output:

```text
Entering Context
Inside context
Exiting Context
```

---

## Key Takeaways

- A context manager manages the setup and cleanup of a resource.
- The `with` statement is used to work with context managers.
- Context managers handle setup and cleanup automatically.
- `__enter__()` is called when entering the context.
- `__exit__()` is called when leaving the context.
- `__exit__()` runs even when an exception occurs.
- Exceptions normally continue unless `__exit__()` returns `True`.
- `exc_type` contains the exception type.
- `exc_value` contains the exception object/value.
- `traceback` contains information about where the exception occurred.
- If there is no exception, `exc_type`, `exc_value`, and `traceback` are `None`.
- `@contextmanager` provides a simpler way to create context managers.
- `yield` gives control to the `with` block.
- Context managers are useful for files, database connections, network connections, and locks.

---

## What I Learned Today

- What context managers are
- Why context managers are useful
- How the `with` statement works
- How `__enter__()` works
- How `__exit__()` works
- How exceptions interact with context managers
- What `exc_type`, `exc_value`, and `traceback` represent
- How to create a custom context manager using a class
- How to use `@contextmanager`
- How `yield` works inside a context manager
- How context managers guarantee cleanup
```