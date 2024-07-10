import json
import os

class ToDoApp:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task '{task}' added successfully.")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            self.save_tasks()
            print(f"Task {index} updated to '{new_task}'.")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print(f"Task {index} marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task '{task['task']}' deleted successfully.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def main():
    app = ToDoApp()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            app.add_task(task)
        elif choice == '2':
            index = int(input("Enter task index: "))
            new_task = input("Enter new task: ")
            app.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter task index: "))
            app.complete_task(index)
        elif choice == '4':
            index = int(input("Enter task index: "))
            app.delete_task(index)
        elif choice == '5':
            app.list_tasks()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
