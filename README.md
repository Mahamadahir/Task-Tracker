# Task Tracker CLI

A Python CLI app to track and manage your to-do list. App stores tasks in a Json file.
Roadmap : https://roadmap.sh/projects/task-tracker
## Features

- Add, update, and delete tasks
- Mark a task as `todo`, `in-progress`, or `done`
- List all tasks
- Filter tasks by status

## Requirements

- Python 3 

## How to run

Clone the repository, then go into the project folder:
'''bash
cd Task-Tracker
python3 task-cli.py --help
'''
## Commands

### Add a task

```bash
python3 task-cli.py add "Buy milk"
```

### List all tasks

```bash
python3 task-cli.py list
```

### List tasks by status

```bash
python3 task-cli.py list todo
python3 task-cli.py list in-progress
python3 task-cli.py list done
```

### Update a task

```bash
python3 task-cli.py update 1 "Buy oat milk"
```

### Mark a task

```bash
python3 task-cli.py mark 1 todo
python3 task-cli.py mark 1 in-progress
python3 task-cli.py mark 1 done
```

### Delete a task

```bash
python3 task-cli.py delete 1
```

### Show help

```bash
python3 task-cli.py --help
python3 task-cli.py add --help
python3 task-cli.py update --help
python3 task-cli.py delete --help
python3 task-cli.py mark --help
python3 task-cli.py list --help
```



## Project Structure

Task-Tracker/
├── task-cli.py
├── task_manager.py
├── storage.py
├── models.py
├── errors.py
├── tasks.json
└── README.md

