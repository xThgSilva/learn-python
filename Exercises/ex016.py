"""
Mini Task List CRUD

You will create a simple task management system.

Rules:
You will start with an empty list:
- tasks = []

You must create functions for:

1️⃣ Create task
- Receives the list and a description
- Adds it to the list
- addTask(list, description)

2️⃣ List tasks
Show all tasks numbered.

Example:
1 - Study Python
2 - Train
3 - Read a book

- listTasks(list)

3️⃣ Delete task
- Receives the list and the task number
- Removes it from the list
- deleteTask(list, index)
"""
tasks = []

def add_task(lst, task):

    if task == "":
        print("[ERROR] Task title cannot be empty.")
    else:
        lst.append(task)
        print("Task added!")

def list_tasks(lst):

    if len(lst) == 0:
        print("There are no tasks.")
    else:
        for i, value in enumerate(lst):
            print(f"{i + 1}º task - {value}")

def delete_task(lst, index):

    correct_id = index - 1
    lst.pop(correct_id)
    print("Task deleted!")

is_active = True

while is_active:
    print("=== Task Manager ===\n")

    option = int(input(
        "Choose an option:\n"
        "[1] - Add task\n"
        "[2] - List tasks\n"
        "[3] - Delete task\n"
        "[0] - Exit\n"
    ))

    if option == 1:

        name = input("Enter the task name: ")
        add_task(tasks, name)

    elif option == 2:

        list_tasks(tasks)

    elif option == 3:

        list_tasks(tasks)
        index = int(input("Enter the task index: "))

        delete_task(tasks, index)

    else:

        is_active = False

print("Program finished...")
