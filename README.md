# Task Tracker CLI

A simple command line interface app to track and manage your tasks. Built with Python using only the standard library — no external dependencies.

## Features

- Add, update, and delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- List all tasks or filter by status
- Tasks are stored locally in a `tasks.json` file

## Installation

Clone the repository:

```bash
git clone https://github.com/I-Martes-I/Task-Tracker-CLI-project.git
cd task-tracker
```

### Commands

#### Add a task
```bash
python task_cli.py add "Buy groceries"
# Output: New task 'Buy groceries' added!
```

#### Update a task
```bash
python task_cli.py update 1 "Cook dinner"
# Output: Task updated!
```

#### Delete a task
```bash
python task_cli.py delete 1
# Output: Task deleted!
```

#### Mark a task as in progress
```bash
python task_cli.py mark-in-progress 1
# Output: Status was changed!
```

#### Mark a task as done
```bash
python task_cli.py mark-done 1
# Output: Status was changed!
```

#### Mark a task as todo
```bash
python task_cli.py mark-todo 1
# Output: Status was changed!
```

#### List all tasks
```bash
python task_cli.py list
```

#### List tasks by status
```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

#### Show help
```bash
python task_cli.py help
```