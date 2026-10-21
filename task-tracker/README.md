# Python Task Tracker

A simple command-line task tracker built with Python. This project is part of my Python learning journey.

## Features

- Add tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in progress or done
- List all tasks or filter by status
- Store tasks in a JSON file

## Requirements

- Python 3

## Usage

Run commands from the project directory:

```bash
python3 py.py add "Buy groceries"
python3 py.py list
python3 py.py update 1 "Buy groceries and cook dinner"
python3 py.py mark-in-progress 1
python3 py.py mark-done 1
python3 py.py list done
python3 py.py delete 1
```

## What I Learned

- Command-line arguments using `sys.argv`
- Reading and writing JSON files
- Working with Python lists
- Conditional statements and loops
- Basic input validation
