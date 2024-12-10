import datetime
import json

# Task class to hold task details
class Task:
    def __init__(self, task_id, description, due_date):
        self.id = task_id
        self.description = description
        self.is_completed = False
        self.due_date = due_date

    def __eq__(self, other):
        return self.id == other.id  # Compare tasks by their unique ID

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"ID: {self.id} | Description: {self.description} | Due Date: {self.due_date} | Status: {status}"

    def is_overdue(self):
        """Check if the task is overdue"""
        today = datetime.date.today()
        return not self.is_completed and datetime.datetime.strptime(self.due_date, '%Y-%m-%d').date() < today


# ToDoList class to manage tasks
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_count = 0

    def add_task(self, description, due_date):
        """Function to add a new task"""
        self.task_count += 1
        task = Task(self.task_count, description, due_date)
        self.tasks.append(task)

    def display_tasks(self):
        """Function to return a list of all tasks"""
        return [str(task) for task in self.tasks]

    def mark_as_completed(self, task_id):
        """Function to mark a task as completed"""
        task = self.find_task_by_id(task_id)
        if task:
            task.is_completed = True
            return True
        return False

    def undo_task_completion(self, task_id):
        """Function to undo task completion"""
        task = self.find_task_by_id(task_id)
        if task and task.is_completed:
            task.is_completed = False
            return True
        return False


    def remove_task(self, task_id):
        """Function to remove a task by ID"""
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print("Task removed successfully.")
            return "Task removed successfully."
        else:
            print("Task not found.")
            return "Task not found."

    def mark_as_completed(self, task_id):
        """Function to mark a task as completed"""
        task = self.find_task_by_id(task_id)
        if task:
            task.is_completed = True
            print("Task marked as completed.")
            return "Task marked as completed."
        else:
            print("Task not found.")
            return "Task not found."

    def update_task_description(self, task_id, new_description):
        """Function to update the description of a task"""
        task = self.find_task_by_id(task_id)
        if task:
            task.description = new_description
            print("Task description updated.")
            return "Task description updated."
        else:
            print("Task not found.")
            return "Task not found."

    def update_task_due_date(self, task_id, new_due_date):
        """Function to update the due date of a task"""
        task = self.find_task_by_id(task_id)
        if task:
            task.due_date = new_due_date
            print("Task due date updated.")
            return "Task due date updated."
        else:
            print("Task not found.")
            return "Task not found."

    def search_task_by_description(self, description):
        """Function to search for a task by description"""
        return [str(task) for task in self.tasks if description in task.description]

    def filter_tasks_by_status(self, is_completed):
        """Function to filter tasks by status (completed or pending)"""
        return [str(task) for task in self.tasks if task.is_completed == is_completed]

    def display_task_count(self):
        """Function to return the total task count"""
        return len(self.tasks)

    def clear_all_tasks(self):
        """Function to clear all tasks"""
        self.tasks.clear()

    def sort_tasks_by_due_date(self):
        """Sort tasks by due date"""
        self.tasks.sort(key=lambda task: datetime.datetime.strptime(task.due_date, '%Y-%m-%d'))

    def show_overdue_tasks(self):
        """Return tasks that are overdue"""
        overdue_tasks = [task for task in self.tasks if task.is_overdue()]
        return [str(task) for task in overdue_tasks]

    def find_task_by_id(self, task_id):
        """Helper function to find a task by ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def export_tasks_to_json(self, filename="tasks.json"):
        """Export tasks to a JSON file"""
        with open(filename, 'w') as file:
            tasks_data = [{
                'id': task.id,
                'description': task.description,
                'due_date': task.due_date,
                'is_completed': task.is_completed
            } for task in self.tasks]
            json.dump(tasks_data, file)
            return f"Tasks exported to {filename}"

    def import_tasks_from_json(self, filename="tasks.json"):
        """Import tasks from a JSON file"""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    self.add_task(task_data['description'], task_data['due_date'])
                    self.tasks[-1].is_completed = task_data['is_completed']
            return f"Tasks imported from {filename}"
        except FileNotFoundError:
            return f"File {filename} not found."


# Mock functions for input/output (for testing purposes)
def prompt_for_description(description: str):
    return description

def prompt_for_due_date(due_date: str):
    return due_date

def display_menu():
    return [
        "1. Add Task",
        "2. Display All Tasks",
        "3. Mark Task as Completed",
        "4. Undo Task Completion",
        "5. Remove Task",
        "6. Update Task Description",
        "7. Update Task Due Date",
        "8. Search Task by Description",
        "9. Filter Tasks by Status",
        "10. Display Total Tasks Count",
        "11. Clear All Tasks",
        "12. Sort Tasks by Due Date",
        "13. Show Overdue Tasks",
        "14. Export Tasks to JSON",
        "15. Import Tasks from JSON",
        "16. Exit"
    ]

def undo_task_completion(self, task_id):
    """Function to undo task completion"""
    task = self.find_task_by_id(task_id)
    if task and task.is_completed:
        task.is_completed = False
        print("Task completion undone.")
        return "Task completion undone."
    else:
        print("Task not found or not completed.")
        return "Task not found or not completed."

def export_tasks_to_json(self, filename="tasks.json"):
    """Export tasks to a JSON file"""
    with open(filename, 'w') as file:
        tasks_data = [{
            'id': task.id,
            'description': task.description,
            'due_date': task.due_date,
            'is_completed': task.is_completed
        } for task in self.tasks]
        json.dump(tasks_data, file)
        return f"Tasks exported to {filename}"

def import_tasks_from_json(self, filename="tasks.json"):
    """Import tasks from a JSON file"""
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                self.add_task(task_data['description'], task_data['due_date'])
                self.tasks[-1].is_completed = task_data['is_completed']
        return f"Tasks imported from {filename}"
    except FileNotFoundError:
        return f"File {filename} not found."

def remove_task(self, task_id):
    """Function to remove a task by ID"""
    task = self.find_task_by_id(task_id)
    if task:
        self.tasks.remove(task)
        print("Task removed successfully.")
        return "Task removed successfully."
    else:
        print("Task not found.")
        return "Task not found."

def sort_tasks_by_due_date(self):
    """Sort tasks by due date"""
    self.tasks.sort(key=lambda task: datetime.datetime.strptime(task.due_date, '%Y-%m-%d'))

def sort_tasks_by_due_date(self):
    """Sort tasks by due date"""
    self.tasks.sort(key=lambda task: datetime.datetime.strptime(task.due_date, '%Y-%m-%d'))

def show_overdue_tasks(self):
    """Return tasks that are overdue"""
    overdue_tasks = [task for task in self.tasks if task.is_overdue()]
    return [str(task) for task in overdue_tasks]

def search_task_by_description(self, description):
    """Function to search for a task by description"""
    return [str(task) for task in self.tasks if description in task.description]


def filter_tasks_by_status(self, is_completed):
    """Function to filter tasks by status (completed or pending)"""
    return [str(task) for task in self.tasks if task.is_completed == is_completed]

def display_task_count(self):
    """Function to return the total task count"""
    return len(self.tasks)


# Main Menu for the program

