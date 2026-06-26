import json

try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []
except json.JSONDecodeError:
    tasks = []
    
task = [
    {"id": 1, "description": "Buy groceries", "status": "todo"}
]

tasks.append(task)

with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)

with open("tasks.json", "r") as f:
    data = json.load(f)

print(data)