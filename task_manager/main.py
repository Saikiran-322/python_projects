# main.py
from tasks import TaskManager

manager = TaskManager()

def menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        manager.add_task(title)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        try:
            tid = int(input("Enter task ID to complete: "))
            manager.complete_task(tid)
        except ValueError:
            print("Invalid input! Enter a number.")

    elif choice == "4":
        try:
            tid = int(input("Enter task ID to delete: "))
            manager.delete_task(tid)
        except ValueError:
            print("Invalid input! Enter a number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
