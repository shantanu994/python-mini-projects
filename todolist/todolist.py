FILENAME = "todo.txt"

# Add a new task
def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(f"{task},Incomplete\n")
    print("Task added.")

# View all tasks
def view_tasks():
    print("\nTo-Do List:")
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No tasks found.")
            else:
                for idx, line in enumerate(lines, 1):
                    task, status = line.strip().split(",")
                    print(f"{idx}. {task} - {status}")
    except FileNotFoundError:
        print("No to-do file found. Start by adding tasks.")

# Mark a task complete
def complete_task(task_num):
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    if 0 < task_num <= len(tasks):
        tasks[task_num-1] = tasks[task_num-1].replace("Incomplete", "Complete")
        with open(FILENAME, "w") as file:
            file.writelines(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Main Menu
while True:
    print("\nTo-Do App")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Mark Task Complete")
    print("4.Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        num = int(input("Enter task number to mark complete: "))
        complete_task(num)
    elif choice == "4":
        print("Exiting To-Do App.")
        break
    else:
        print("Invalid choice.")
