# Git

## What is Git?

Git is a distributed version control system used to track changes in files and manage source code.

## Repository

A repository is a Git-tracked project folder.

## Working Directory

The place where we create and edit files.

## Staging Area

A temporary area where changes are added before committing.

## Commit

A snapshot of the project at a particular point in time.

## Git Commands

### git status

Shows the current status of the repository.

### git add .

Moves changes from the working directory to the staging area.

### git commit -m "message"

Creates a snapshot of the project.

### git log

Shows the history of commits.

### git diff

Shows changes before committing.

### git restore filename

Restores a file to its last committed version.

---

# GitHub

## What is GitHub?

GitHub is a cloud platform that stores Git repositories online.

## Local Repository

Repository stored on your computer.

## Remote Repository

Repository stored on GitHub.

## GitHub Commands

### git push

Uploads commits to GitHub.

### git pull

Downloads the latest commits from GitHub.

### git clone

Copies a remote repository to your local computer.

---

# pip

Python package manager.

## Commands

pip list

Lists installed packages.

pip install package_name

Installs a package.

pip install --upgrade package_name

Updates a package.

pip uninstall package_name

Removes a package.

pip show package_name

Displays package information.

---

# Virtual Environment

## Create

python -m venv .venv

## Activate (Windows)

.venv\Scripts\Activate

## Deactivate

deactivate

---

# requirements.txt

Generate:

pip freeze > requirements.txt

Install packages:

pip install -r requirements.txt