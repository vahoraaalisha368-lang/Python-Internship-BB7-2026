# Initialize an empty list for the to-do list
todo_list = []

# Function to add a task
def add_task(task_name):
    todo_list.append(task_name)
    print(f"Task added: '{task_name}'")

# Function to remove a task by name
def remove_task(task_name):
    if task_name in todo_list:
        todo_list.remove(task_name)
        print(f"Task removed: '{task_name}'")
    else:
        print(f"Task '{task_name}' not found in the list.")

# Function to print all current tasks
def show_tasks():
    print("\n--- Current To-Do List ---")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    print("--------------------------\n")

# --- Testing the To-Do List Manager ---

# 1. Adding 5 tasks
print("--- Adding 5 Tasks ---")
add_task("Learn Python basics")
add_task("Complete internship assignment")
add_task("Go for a walk")
add_task("Read a book")
add_task("Buy groceries")

# Print current tasks after adding
show_tasks()

# 2. Removing 2 tasks by name
print("--- Removing 2 Tasks ---")
remove_task("Go for a walk")
remove_task("Read a book")

# Print final current tasks
show_tasks()