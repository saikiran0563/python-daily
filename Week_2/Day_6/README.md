# Week 2 Day 6 - File I/O

## What I Learned

- File I/O means reading and writing files using Python.
- `open()` is used to open files.
- File modes:
  - `r` → Read
  - `w` → Write/overwrite
  - `a` → Append
  - `x` → Create
- `read()` → reads the entire file.
- `readline()` → reads one line.
- `readlines()` → reads all lines as a list.
- `strip()` → removes newline and extra whitespace.
- `tell()` → returns the current file position.
- `seek()` → changes the file position.
- `with open()` → automatically closes the file.
- `FileNotFoundError` → occurs when a file does not exist.
- `FileExistsError` → occurs when creating a file that already exists.

## Example

```python
with open("student.txt", "w") as file:
    file.write("Kiran\nRahul\nArjun\nPriya")

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## Key Difference

```text
w → overwrites existing content
a → adds content to the end
```

## Day 6 Completed ✅