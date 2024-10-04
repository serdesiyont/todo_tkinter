import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "✔️" if self.completed else "❌"
        return f"{self.description} [{status}]"

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def view_tasks(self):
        return self.tasks

    def remove_task(self, index):
        try:
            self.tasks.pop(index)
            self.save_tasks()
        except IndexError:
            messagebox.showerror("Error", "Invalid task number.")

    def mark_completed(self, index):
        try:
            self.tasks[index].completed = True
            self.save_tasks()
        except IndexError:
            messagebox.showerror("Error", "Invalid task number.")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                tasks = json.load(f)
                self.tasks = [Task(**task) for task in tasks]

class ToDoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list
        self.title("To-Do List Application")
        self.attributes('-fullscreen', False)
        self.configure(bg='lightblue', width=100, height=30)

        self.create_widgets()
        self.refresh_tasks()

    def create_widgets(self):
        self.frame = tk.Frame(self, bg='lightblue')
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.listbox = tk.Listbox(self.frame, font=("Helvetica", 18), bg='white', fg='black')
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg='#4CAF50', fg='white', font=("Helvetica", 16))
        self.add_button.pack(fill=tk.X, pady=5)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task, bg='#F44336', fg='white', font=("Helvetica", 16))
        self.remove_button.pack(fill=tk.X, pady=5)

        self.mark_button = tk.Button(self.frame, text="Mark Completed", command=self.mark_task, bg='#FFEB3B', fg='black', font=("Helvetica", 16))
        self.mark_button.pack(fill=tk.X, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.quit, bg='#9E9E9E', fg='white', font=("Helvetica", 16))
        self.exit_button.pack(fill=tk.X, pady=5)

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list.view_tasks():
            self.listbox.insert(tk.END, task)

    def add_task(self):
        description = simpledialog.askstring("Task", "Enter the task description:")
        if description:
            self.todo_list.add_task(description)
            self.refresh_tasks()

    def remove_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.todo_list.remove_task(index)
            self.refresh_tasks()
        except IndexError:
            messagebox.showerror("Error", "Select a task to remove.")

    def mark_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.todo_list.mark_completed(index)
            self.refresh_tasks()
        except IndexError:
            messagebox.showerror("Error", "Select a task to mark as completed.")

if __name__ == "__main__":
    todo_list = ToDoList()
    app = ToDoApp(todo_list)
    app.mainloop()