# 🐍 Python Daily — Python, APIs & SQL Practice

A structured learning repository documenting hands-on Python, REST API, file I/O, testing, logging, and SQL practice.

The repository is organized by **week and day** so the progression is easy to follow and review.

## 🎯 Purpose

This repository is a practical record of learning rather than a collection of copied snippets. Each section contains exercises, experiments, and small implementations used to strengthen programming and interview fundamentals.

## 📚 Learning Areas

- Python fundamentals and intermediate programming
- Data types, slicing, comprehensions, functions, modules, and arguments
- File handling and JSON/CSV processing
- REST API consumption with `requests`
- Error handling and logging
- CLI-style Python applications
- Automated testing fundamentals
- SQL query practice and interview-oriented problems
- Git and GitHub workflow

## 🗂️ Structure

```text
python-daily/
├── Week_1/
│   ├── Day_1/
│   ├── Day_2/
│   ├── Day_3/
│   └── ...
├── Week_2/
│   ├── Day_1/
│   ├── Day_2/
│   ├── ...
│   ├── weather_cli.py
│   └── test_weather_cli.py
├── Week_3/
│   └── Day_1/
└── README.md
```

## 🌦️ Practical API Project

`Week_2/weather_cli.py` is a command-line weather client that demonstrates:

- HTTP requests with `requests`
- JSON response parsing
- Query parameters
- Request timeouts
- HTTP error handling
- Structured return values
- Python logging

The accompanying `test_weather_cli.py` contains tests for the weather CLI work.

## 🗃️ SQL Practice

Week 3 contains SQL exercises focused on practical querying and interview preparation, including joins, aggregation, grouping, filtering, and ordering.

## ▶️ Running Python Examples

Create a virtual environment from the repository root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies for API examples when required:

```bash
pip install requests
```

Then run an individual exercise, for example:

```bash
python Week_2/weather_cli.py
```

## 🧪 Learning Workflow

The repository follows a simple cycle:

1. Learn a concept.
2. Implement it in Python or SQL.
3. Test the implementation where applicable.
4. Document the result.
5. Commit the work to GitHub.

## 🔒 Repository Hygiene

Generated logs, virtual environments, bytecode, and editor files should remain untracked. Do not commit API keys, passwords, access tokens, or personal data.

## 👤 Author

**Sai Kiran**

GitHub: https://github.com/saikiran0563
