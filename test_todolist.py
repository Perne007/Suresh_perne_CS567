import unittest
from datetime import datetime
from unittest.mock import patch, mock_open
import json
from todolist import Task, ToDoList  # Import from your main todolist.py file

class TestToDoList(unittest.TestCase):

    def setUp(self):
        """Set up the initial conditions for tests"""
        self.todo_list = ToDoList()
        self.todo_list.add_task("Test Task 1", "2024-12-31")
        self.todo_list.add_task("Test Task 2", "2025-01-01")
        self.todo_list.add_task("Test Task 3", "2023-12-31")

    def test_add_task(self):
        """Test adding tasks to the list"""
        self.assertEqual(len(self.todo_list.tasks), 3)
        self.todo_list.add_task("New Task", "2025-02-01")
        self.assertEqual(len(self.todo_list.tasks), 4)
        self.assertEqual(self.todo_list.tasks[-1].description, "New Task")
        self.assertEqual(self.todo_list.tasks[-1].due_date, "2025-02-01")

    def test_mark_task_as_completed(self):
        """Test marking a task as completed"""
        task_id = self.todo_list.tasks[0].id
        self.todo_list.mark_as_completed(task_id)
        self.assertTrue(self.todo_list.tasks[0].is_completed)

    def test_undo_task_completion(self):
        """Test undoing task completion"""
        task_id = self.todo_list.tasks[0].id
        self.todo_list.mark_as_completed(task_id)  # Mark as completed first
        self.assertTrue(self.todo_list.tasks[0].is_completed)
        self.todo_list.mark_as_completed(task_id)  # Try marking again (edge case)
        self.assertTrue(self.todo_list.tasks[0].is_completed)

    def test_remove_task(self):
        """Test removing a task from the list"""
        task_id = self.todo_list.tasks[0].id
        self.todo_list.remove_task(task_id)
        self.assertEqual(len(self.todo_list.tasks), 2)
        self.assertIsNone(self.todo_list.find_task_by_id(task_id))

    def test_update_task_description(self):
        """Test updating the task description"""
        task_id = self.todo_list.tasks[0].id
        new_description = "Updated Task Description"
        self.todo_list.update_task_description(task_id, new_description)
        self.assertEqual(self.todo_list.tasks[0].description, new_description)

    def test_update_task_due_date(self):
        """Test updating the task due date"""
        task_id = self.todo_list.tasks[0].id
        new_due_date = "2024-11-11"
        self.todo_list.update_task_due_date(task_id, new_due_date)
        self.assertEqual(self.todo_list.tasks[0].due_date, new_due_date)

    def test_search_task_by_description(self):
        """Test searching tasks by description"""
        tasks = self.todo_list.search_task_by_description("Test Task 1")
        self.assertEqual(len(tasks), 1)
        self.assertIn("Test Task 1", tasks[0])

    def test_filter_tasks_by_status(self):
        """Test filtering tasks by completion status"""
        self.todo_list.mark_as_completed(1)
        completed_tasks = self.todo_list.filter_tasks_by_status(True)
        pending_tasks = self.todo_list.filter_tasks_by_status(False)
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(len(pending_tasks), 2)

    def test_show_overdue_tasks(self):
        """Test showing overdue tasks"""
        overdue_tasks = self.todo_list.show_overdue_tasks()
        # Assuming today's date is 2024-01-01, only "Test Task 3" should be overdue
        self.assertEqual(len(overdue_tasks), 1)
        self.assertIn("Test Task 3", overdue_tasks[0])

    def test_export_tasks_to_json(self):
        """Test exporting tasks to JSON"""
        mock_file = mock_open()
        
        with patch("builtins.open", mock_file):
            result = self.todo_list.export_tasks_to_json("tasks.json")
            self.assertIn("Tasks exported to tasks.json", result)
            mock_file.assert_called_with("tasks.json", "w")

    def test_import_tasks_from_json(self):
        """Test importing tasks from JSON"""
        test_json_data = [
            {"id": 4, "description": "Imported Task", "due_date": "2025-03-01", "is_completed": False}
        ]
        mock_file = mock_open(read_data=json.dumps(test_json_data))
        
        with patch("builtins.open", mock_file):
            result = self.todo_list.import_tasks_from_json("tasks.json")
            self.assertIn("Tasks imported from tasks.json", result)
            self.assertEqual(len(self.todo_list.tasks), 4)
            self.assertEqual(self.todo_list.tasks[-1].description, "Imported Task")
            mock_file.assert_called_with("tasks.json", "r")

    def test_task_is_overdue(self):
        """Test if a task is overdue"""
        overdue_task = Task(1, "Overdue Task", "2020-12-31")
        self.assertTrue(overdue_task.is_overdue())

    def test_task_is_not_overdue(self):
        """Test if a task is not overdue"""
        non_overdue_task = Task(2, "Non-overdue Task", "2025-01-01")
        self.assertFalse(non_overdue_task.is_overdue())

    def test_task_is_completed(self):
        """Test if the task is marked as completed"""
        task = self.todo_list.tasks[0]
        task.is_completed = True
        self.assertTrue(task.is_completed)

    def test_clear_all_tasks(self):
        """Test clearing all tasks"""
        self.todo_list.clear_all_tasks()
        self.assertEqual(len(self.todo_list.tasks), 0)

    def test_sort_tasks_by_due_date(self):
        """Test sorting tasks by due date"""
        self.todo_list.sort_tasks_by_due_date()
        self.assertEqual(self.todo_list.tasks[0].due_date, "2023-12-31")  # Earliest due date

    def test_display_task_count(self):
        """Test displaying task count"""
        self.assertEqual(self.todo_list.display_task_count(), 3)

    def test_remove_task_not_found(self):
        """Test removing a task that doesn't exist"""
        result = self.todo_list.remove_task(999)  # Non-existing task ID
        self.assertIn("Task not found", result)

    def test_mark_task_as_completed_not_found(self):
        """Test marking a non-existing task as completed"""
        result = self.todo_list.mark_as_completed(999)  # Non-existing task ID
        self.assertIn("Task not found", result)

    def test_update_task_description_not_found(self):
        """Test updating a description of a non-existing task"""
        result = self.todo_list.update_task_description(999, "New Description")
        self.assertIn("Task not found", result)

    def test_update_task_due_date_not_found(self):
        """Test updating due date of a non-existing task"""
        result = self.todo_list.update_task_due_date(999, "2025-01-01")
        self.assertIn("Task not found", result)

    def test_display_menu(self):

        self.todo_list.display_tasks()


    


if __name__ == '__main__':
    unittest.main()
