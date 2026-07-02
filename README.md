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


```bash
  add <description>          - Add a new task
  update <id> <description>  - Update a task
  delete <id>                - Delete a task
  mark-in-progress <id>      - Mark a task as in progress
  mark-done <id>             - Mark a task as done
  mark-todo <id>             - Mark a task as todo
  list                       - List all tasks
  list todo                  - List all todo tasks
  list in-progress           - List all in-progress tasks
  list done                  - List all done tasks
  help                       - Show this help message
```