import sys
import json
import datetime

'''def addTask(id = len(tasks), description = "Add your description here", status = "todo", createdAt = datetime.datetime.now(), updatedAt = datetime.datetime.now()):
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
    '''
    
    #task = [{
    #   "id": "", 
    #   "description": "", 
    #   "status": "", 
    #   "createdAt": "", 
    #   "updatedAt": ""
    #       }]

    


try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []
except json.JSONDecodeError:
    tasks = []

task = {
       "id": "", 
       "description": "", 
       "status": "", 
       "createdAt": "", 
       "updatedAt": ""
        }

args = sys.argv

if len(args) < 2:
    print("You need to enter your command! (Add, Delete, Update, List) ")
    sys.exit(1)

command = args[1] 

if command.lower() == "add":
    if len(args) == 2:
        print("Task description required!")
    else:
        tasks.append(task)
        newTask = tasks[len(tasks)-1]
        newTask.update({
            "id": len(tasks)-1, 
            "description": args[2], 
            "status": "todo", 
            "createdAt": datetime.datetime.now(), 
            "updatedAt": datetime.datetime.now()
        })
        print(f"New task ''{newTask["description"]}'' added!")
elif command.lower() == "delete":
    if len(args) == 2:
        print("Task ID required!")
    else:

        print("Task deleted!")
elif command.lower() == "update":
    if len(args) == 2:
        print("Task ID and description required!")
    elif len(args) < 4:
        print("Task description required!")
    else:
        print("Task updated!")
elif command.lower() == "list":
    if len(args) == 2:
        print("List of all of the tasks:")
    elif len(args) == 3:
        if args[2].lower() == "todo":
            print("List of all of the todo tasks:")
        elif args[2].lower() == "in-progress":
            print("List of all of the in-progress tasks:")
        elif args[2].lower() == "done":
            print("List of all of the done tasks:")
        else:
            print("Incorrect command")
else: 
    print("Incorrect command")