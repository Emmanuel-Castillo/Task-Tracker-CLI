# This application simulates a command line interface using Python
# Users will be able to input commands and arguments that will then execute actions performed from
# a traditional Task Tracker.
# These actions involve:
#   - Add, Update, Delete tasks
#   - Mark a task as in progress or done
#   - List all tasks
#   - List all tasks that are done
#   - List all tasks that are not done
#   - List all tasks that are in progress

from datetime import datetime
import json
import os
JSON_FILE_PATH = "Task-Tracker-CLI.json"

class Task:
    def __init__(self, id, description):
        current_time = datetime.now()

        self.data = {
            "id" : id,
            "description" : description,
            "status" : "todo",
            "createdAt" : current_time.strftime('%H:%M %d %B %Y'),
            "updatedAt" : current_time.strftime('%H:%M %d %B %Y'),
        }

    
    
def add(task_description):
    print("Task desciption", task_description)
     # Create task
    # Should have the following properties
    #   - id
    #   - description
    #   - status
    #   - createdAt
    #   - updatedAt

    # Check to see if JSON file exists or empty
    # If so, read the file and determine id for new task
    # Else, provide task with id of 1

    # Default values in case file doesn't exist or is empty
    data = []
    newTaskId = 1

    # Create file if it doesn't exist
    if not os.path.exists(JSON_FILE_PATH):
        open(JSON_FILE_PATH, "w")

    # Open JSON file to read data
    with open(JSON_FILE_PATH, 'r') as file:
        # Check to see if file is not empty
        file_size = os.path.getsize(JSON_FILE_PATH)
        if file_size > 0:
            # Acquire data from JSON file to determine new id value
            data = json.load(file)
            newTaskId = data[-1]["id"] + 1

    # Create task w/ id of 1
    newTask = Task(newTaskId, task_description)
    data.append(newTask.data)

    # Write data to JSON file
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file)

def update(id, new_task_description):
    # Update task given id
    # Check to see if file exists. If not, return
    if not os.path.exists(JSON_FILE_PATH):
        print("File doesn't exist")
        return
    
    else:
        # Open file to read data
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)

        # Find task in data using id
        for task in data:

            # CHECK LATER: if id given in user input is a number
            if task["id"] == int(id):
                task["description"] = new_task_description
                task["updatedAt"] = datetime.now().strftime('%H:%M %d %B %Y')
                
                # Write back data in file
                with open(JSON_FILE_PATH, 'w') as file:
                    json.dump(data, file)

                print("Task updated successfully")

def delete(id):
    print(id)
    # Delete task given id
    # Check to see if file exists. If not, return
    if not os.path.exists(JSON_FILE_PATH):
        print("File doesn't exist")
        return

    else:
        # Open file to read data
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)

        # Removing dictionary from list using list comprehension
        newData = [task for task in data if not (task['id'] == int(id))]
        print("newData: " , newData)
        
        # Write back data to file
        with open(JSON_FILE_PATH, 'w') as file:
            json.dump(newData, file)

        print("Task deleted successfully")

def mark(id, mark):
    # Marking task in-progress given id
    # Check to see if file exists. If not, return
    if not os.path.exists(JSON_FILE_PATH):
        print("File doesn't exist")
        return

    else:
            # Open file to read data
            with open(JSON_FILE_PATH, 'r') as file:
                data = json.load(file)

            current_time = datetime.now()

            # Update task in data list
            for task in data:
                if task['id'] == int(id):
                    task['status'] = mark
                    task['updatedAt'] = current_time.strftime('%H:%M %d %B %Y')

            # Write back data to file
            with open(JSON_FILE_PATH, 'w') as file:
                json.dump(data, file)

            print("Task updated successfully")

def list(filter):
    # Listing all tasks
    # Check to see if file exists. If not, return
    if not os.path.exists(JSON_FILE_PATH):
        print("File doesn't exist")
        return

    else:
            # Open file to read data
            with open(JSON_FILE_PATH, 'r') as file:
                data = json.load(file)

            if filter:
                data = [task for task in data if task['status'] == filter]

            if not data:
                print("No tasks found")
            else:
                for task in data:
                    print(task)

def main():
    try:
        while(1):
            # Acquire user input
            user_input = input()

            # Parse user input
            input_parsed = user_input.split()

            # Check if first input is 'task-cli' command
            if input_parsed[0] != "task-cli":
                print("First input is not 'task-cli'")

            else:
                # Call functions depending on first positional argument
                match input_parsed[1]:
                    case "add":
                        task_description = " ".join(input_parsed[2:])
                        add(task_description)
                    case "update":
                        task_id = input_parsed[2]
                        task_description = " ".join(input_parsed[3:])
                        update(task_id, task_description)
                    case "delete":
                        task_id = input_parsed[2]
                        delete(task_id)
                    case "mark-in-progress":
                        task_id = input_parsed[2]
                        mark(task_id, "in-progress")
                    case "mark-done":
                        task_id = input_parsed[2]
                        mark(task_id, "done")
                    case "list":
                        list(input_parsed[2] if len(input_parsed) == 3 else None)
    except KeyboardInterrupt:
        print("Program ending...")

if __name__ == "__main__":
    main()
