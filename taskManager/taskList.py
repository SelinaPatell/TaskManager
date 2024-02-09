class Task:
    def __init__(self, name, description, status="Pending"):
        self.name = name
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task.name} - {task.description} - {task.status}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_manager.add_task(Task(name, description))
            print("Task added successfully.")
        elif userChoice == "2":
            name = input("Enter the name of the task to remove: ")
            if task_manager.remove_task(name):
                print("Task removed successfully.")
            else:
                print("Task not found.")
        elif userChoice == "3":
            task_manager.display_tasks()
        elif userChoice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from the following choices.")

if __name__ == "__main__":
    main()