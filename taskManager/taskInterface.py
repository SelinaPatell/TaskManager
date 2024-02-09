import tkinter as tk

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")

        self.tasks = []

        self.task_name_label = tk.Label(master, text="Task Name:")
        self.task_name_label.grid(row=0, column=0)

        self.task_name_entry = tk.Entry(master)
        self.task_name_entry.grid(row=0, column=1)

        self.task_description_label = tk.Label(master, text="Task Description:")
        self.task_description_label.grid(row=1, column=0)

        self.task_description_entry = tk.Entry(master)
        self.task_description_entry.grid(row=1, column=1)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.grid(row=3, column=0, columnspan=2)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=0, columnspan=2)

        self.update_task_listbox()

    def add_task(self):
        name = self.task_name_entry.get()
        description = self.task_description_entry.get()
        self.tasks.append((name, description))
        self.update_task_listbox()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            self.task_listbox.insert(tk.END, f"{idx}. {task[0]} - {task[1]}")

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()