text="To Do Application"
spaces = (150 - len(text)) // 2
print(' ' * spaces + text)
print("\n")

tasks = []

def add_task():
    task =  input(f"Enter task to add : ") 
    tasks.append({'task': task, 'done': False})
    print(f"Task '{task}' added.")

def delete_task():
    print_tasks()  
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)  
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def print_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

def mark_done():
    print_tasks()  
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['done'] = True  
            print(f"Task '{tasks[task_number - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Print Tasks")
    print("4. Mark Task as Done")
    print("5. Exit")


switch_dict = {
    1: add_task,
    2: delete_task,
    3: print_tasks,
    4: mark_done
}


while True:
    show_menu()
    try:
        choice = int(input("Choose an option: "))
        if choice == 5:
            print("Exiting To-Do List.")
            break
        elif choice in switch_dict:
            switch_dict[choice]()  
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")


