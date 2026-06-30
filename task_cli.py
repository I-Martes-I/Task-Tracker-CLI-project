import sys
import json
import datetime

try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []
except json.JSONDecodeError:
    tasks = []

args = sys.argv

if len(args) < 2:
    print("You need to enter your command! (Add, Delete, Update, List) ")
    sys.exit(1)

command = args[1] 

if command.lower() == "add":
    if len(args) == 2:
        print("Task description required!")
    else:
        if tasks:
            new_id = max(task["id"] for task in tasks) + 1
        else:
            new_id = 1
        new_task = {
            "id": new_id,
            "description": args[2],
            "status": "todo",
            "createdAt": datetime.datetime.now().isoformat(),
            "updatedAt": datetime.datetime.now().isoformat()
        }
        tasks.append(new_task)
        print(f"New task '{new_task['description']}' added!")

elif command.lower() == "delete":
    if len(args) == 2:
        print("Task ID required!")
    else:
        if any(int(args[2]) in task.values() for task in tasks):
            tasks = [task for task in tasks if task.get("id") != int(args[2])]
            print("Task deleted!")
        else:
            print(f"Task with ID {args[2]} was NOT fount")

elif command.lower() == "update":
    if len(args) == 2:
        print("Task ID and description required!")
    elif len(args) < 4:
        print("Task description required!")
    else:
        if any(int(args[2]) in task.values() for task in tasks):
            tasks[int(args[2])]["description"] = args[3]
            tasks[int(args[2])]["updatedAt"] = datetime.datetime.now().isoformat()
            print("Task updated!")
        else:
            print(f"Task with ID {args[2]} was NOT fount")

elif command.lower() == "list":
    if len(args) == 2:
        print("List of all of the tasks:")
        for task in tasks:
            print(task)
    elif len(args) == 3:
        if args[2].lower() == "todo":
            print("List of all of the todo tasks:")
            for task in tasks:
                if task["status"] == "todo":
                    print(task)
        elif args[2].lower() == "in-progress":
            print("List of all of the in-progress tasks:")
            for task in tasks:
                if task["status"] == "in-progress":
                    print(task)
        elif args[2].lower() == "done":
            print("List of all of the done tasks:")
            for task in tasks:
                if task["status"] == "done":
                    print(task)
        else:
            print("Incorrect command")

elif command.lower() == "mark-in-progress":
    if len(args) == 2:
        print("Task ID required!")
    else:
        if any(int(args[2]) in task.values() for task in tasks):
            tasks[int(args[2])]["status"] = "in-progress"
            print("Status was changed!")
        else:
            print(f"Task with ID {args[2]} was NOT found!")
elif command.lower() == "mark-done":
    if len(args) == 2:
        print("Task ID required!")
    else:
        if any(int(args[2]) in task.values() for task in tasks):
            tasks[int(args[2])]["status"] = "done"
            print("Status was changed!")
        else:
            print(f"Task with ID {args[2]} was NOT found!")
elif command.lower() == "mark-todo":
    if len(args) == 2:
        print("Task ID required!")
    else:
        if any(int(args[2]) in task.values() for task in tasks):
            tasks[int(args[2])]["status"] = "todo"
            print("Status was changed!")
        else:
            print(f"Task with ID {args[2]} was NOT found!")

else: 
    print("Incorrect command")

with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)

with open("tasks.json", "r") as f:
    data = json.load(f)