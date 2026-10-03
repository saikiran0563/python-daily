# 🐍 Python Daily — Python, APIs & SQL Practice

A structured learning repository documenting hands-on Python, REST API, file I/O, testing, logging, and SQL practice.

The repository is organized by **week and day** so the progression is easy to follow and review.

## 🎯 Purpose

This repository is a practical record of learning rather than a collection of copied snippets. Each section contains exercises, experiments, and small implementations used to strengthen programming and interview fundamentals.

## 📚 Learning Areas

- Python fundamentals and intermediate programming
- Data types, slicing, comprehensions, functions, modules, and arguments
- File handling and JSON/CSV processing
- REST API consumption with requests
- Error handling and logging
- CLI-style Python applications
- Automated testing fundamentals
- SQL query practice and interview-oriented problems
- Git and GitHub workflow

## 🗂️ Current Structure

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
│   ├── Day_1/
│   ├── Day_2/
│   └── Day_3/
├── .github/
├── .gitignore
└── README.md
```

## 📈 Current Progress

**Week 3 — SQL interview preparation**

- **Day 1:** Tables, constraints, CRUD operations
- **Day 2:** SQL query practice
- **Day 3:** JOINs and subqueries

Week 3 Day 3 is the latest completed section currently committed in this repository.

## 🌦️ Practical API Project

Week_2/weather_cli.py is a command-line weather client that demonstrates:

- HTTP requests with requests
- JSON response parsing
- Query parameters
- Request timeouts
- HTTP error handling
- Structured return values
- Python logging

The accompanying test_weather_cli.py contains tests for the weather CLI work, including a mocked API response and a request-failure case.

## 🗃️ SQL Practice

Week 3 focuses on interview-oriented SQL. Current practice covers:

- Table creation and constraints
- INSERT, UPDATE, DELETE
- Filtering and sorting
- Aggregation and grouping
- JOINs
- Subqueries

Each day contains a focused SQL file and a short README describing what was practiced.

## 🧪 Automated Checks

GitHub Actions runs on pushes and pull requests to main.

Current checks include:

- Python syntax compilation
- pytest execution for the weather CLI tests
- Repository dependency installation required by the tests

## ▶️ Running Examples Locally

Create a virtual environment from the repository root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies used by the API example and tests:

```bash
pip install requests pytest
```

Run the weather CLI:

```bash
python Week_2/weather_cli.py
```

Run its tests:

```bash
pytest -q Week_2/test_weather_cli.py
```

## 🧭 Learning Workflow

The repository follows a repeatable cycle:

1. Learn a concept.
2. Implement it in Python or SQL.
3. Test the implementation where applicable.
4. Document the result.
5. Commit the work to GitHub.

## 🔒 Repository Hygiene

Generated logs, virtual environments, bytecode, editor files, environment files, and personal/sample data should remain out of the repository.

Do not commit:

- API keys
- passwords
- access tokens
- real personal information
- local .env files

## 👤 Author

**Sai Kiran**

GitHub: https://github.com/saikiran0563

LinkedIn: https://www.linkedin.com/in/sai-kiran-buska-127866403