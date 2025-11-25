# tasks.py
from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return

        for task in self.tasks:
            status = "✔️" if task["completed"] else "❌"
            print(f"{task['id']}. {task['title']} - {status}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(self.tasks)
                print("Task completed!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        new_list = [t for t in self.tasks if t["id"] != task_id]
        if len(new_list) == len(self.tasks):
            print("Task not found!")
            return

        self.tasks = new_list
        save_tasks(self.tasks)
        print("Task deleted!")
