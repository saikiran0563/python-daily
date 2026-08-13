# Week 2 Day 7 - CSV & JSON

## What I Learned

### CSV

- `csv.reader()` → reads CSV rows as lists.
- `csv.writer()` → writes rows to a CSV file.
- `writerow()` → writes one row.
- `writerows()` → writes multiple rows.
- `csv.DictReader()` → reads rows as dictionaries.
- `csv.DictWriter()` → writes dictionaries to CSV.

### JSON

- `json.load()` → JSON file → Python object.
- `json.loads()` → JSON string → Python object.
- `json.dump()` → Python object → JSON file.
- `json.dumps()` → Python object → JSON string.

## Practical Project

Converted CSV data into JSON using:

```python
import csv
import json

students = []

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved successfully")
```

## Key Difference

```text
CSV → tabular data
JSON → structured data
```

## Day 7 Completed ✅