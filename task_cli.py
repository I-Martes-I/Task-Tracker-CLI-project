import sys
import json
import datetime

def addTask(id = len(tasks), description = "Add your description here", status = "todo", createdAt = datetime.datetime.now(), updatedAt = datetime.datetime.now()):
    task = [{"id": id, "description": description, "status": status, "createdAt": createdAt, "updatedAt": updatedAt}]
    tasks.append(task)

try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []
except json.JSONDecodeError:
    tasks = []

args = sys.argv

if len(args) < 2:
    print("Enter your command: ")
    sys.exit(1)

command = args[1] 

if command == "add":
    if len(args) < 3:
        print(f"You need an argument after command '{command}'")
    else:
        description = args[2]
        addTask(, , )
        
        print(f"Task '{description}' added")
elif command == "list":
    pass
    print("List")
elif command == "delete":
    if len(args) < 3:
        print(f"You need an argument after command '{command}'")
    else:
        description = args[2]
        print(f"Delete task with ID {description}")
else:
    print(f"There is no such command as '{command}'")

    #task = [{"id": "", "description": "", "status": "", "createdAt": "", "updatedAt": ""}]
    #task = [{"id": len(tasks), "description": "Add your description here", "status": "todo", "createdAt": datetime.datetime.now(), "updatedAt": datetime.datetime.now()}]