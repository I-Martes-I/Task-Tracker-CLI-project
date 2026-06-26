import sys

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