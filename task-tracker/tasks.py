import sys
import json
try:
    with open("tasks.json", "r") as file:
        task = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    task = []
if len(sys.argv) < 2:
    print("Enter a command: add, update, delete, mark-in-progress, mark-done, list")
elif sys.argv[1] == "add":
    if len(sys.argv) != 3:
        print("Enter in valid input format")
    else:
        task.append([len(task) + 1, sys.argv[2], "todo"])   # id, description, status
        print("Task added successfully (ID:", len(task), ")")
elif sys.argv[1] == "list":
    if len(sys.argv) == 2:
        for i in task:
            if i[0] != -1:
                print(i[0], "-", i[1], "-", i[2])        
    elif len(sys.argv) == 3 and sys.argv[2] in ("todo", "in-progress", "done"):
        for i in task:
            if i[2] == sys.argv[2] and i[0] != -1:
                print(i[0], "-", i[1], "-", i[2])
    else:
        print("Enter a valid input")
elif sys.argv[1] not in ("update", "mark-in-progress", "mark-done", "delete"):
    print("The input format is wrong")
elif len(sys.argv) != (4 if sys.argv[1] == "update" else 3):
    print("Enter in valid input format")
elif (not sys.argv[2].isdigit()
      or int(sys.argv[2]) <= 0
      or int(sys.argv[2]) > len(task)
      or task[int(sys.argv[2]) - 1][0] == -1):
    print("Enter valid ID")
elif sys.argv[1] == "update":
    task[int(sys.argv[2]) - 1][1] = sys.argv[3]
    print("Task updated")
elif sys.argv[1] == "mark-in-progress":
    task[int(sys.argv[2]) - 1][2] = "in-progress"
    print("Task marked in progress")
elif sys.argv[1] == "mark-done":
    task[int(sys.argv[2]) - 1][2] = "done"
    print("Task marked done")
elif sys.argv[1] == "delete":
    task[int(sys.argv[2]) - 1][0] = -1
    print("Task deleted")

with open("tasks.json", "w") as file:
    json.dump(task, file, indent=4)