# CLI Task Tracker

A simple command-line interface (CLI) application for tracking tasks. You can add, update, delete, and list tasks, as well as mark them as in progress or done.

## Challenge

This is a challenge from https://roadmap.sh/projects/task-tracker

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as in progress
- Mark a task as done
- List all tasks
- List tasks by status (done, not done, in progress)

## Requirements

- Python 3.x

**Clone the Repository**

```sh
https://github.com/Emmanuel-Castillo/Task-Tracker-CLI.git
```

## Usage

Run the script with the desired action and arguments.

### Add a New Task

```sh
task-cli add "task description"
```

### Update an existing Task

```sh
task-cli update task_id "task description"
```

### Delete a Task
```sh
task-cli delete task_id
```

### Mark a Task as In Progress
```sh
task-cli mark-in-progress task_id
```

### Mark a Task as Done

```sh
task-cli mark-done task_id
```

### List All Tasks

```sh
task-cli list
```

### List Done Tasks

```sh
task-cli list done
```

### List Tasks In Progress

```sh
task-cli list in-progress
```
