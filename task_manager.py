#!/usr/bin/env python3
"""
Task Manager App for Two Users

A command-line task management application that allows two users to:
- Add, edit, delete, and mark tasks as complete
- Assign due dates and priorities
- View all tasks by user

Author: AI Assistant
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class Task:
    """Represents a single task with all its properties."""
    
    def __init__(self, title: str, description: str = "", priority: str = "Medium", 
                 due_date: Optional[str] = None, completed: bool = False):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed,
            'created_date': self.created_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = cls(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'Medium'),
            due_date=data.get('due_date'),
            completed=data.get('completed', False)
        )
        task.created_date = data.get('created_date', datetime.now().strftime("%Y-%m-%d %H:%M"))
        return task
    
    def __str__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        priority_symbol = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(self.priority, "🟡")
        due_info = f" (Due: {self.due_date})" if self.due_date else ""
        return f"{status} {priority_symbol} {self.title}{due_info}"


class TaskManager:
    """Main task manager class that handles all operations."""
    
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.users = ["User1", "User2"]
        self.current_user = None
        self.tasks = {user: [] for user in self.users}
        self.load_data()
    
    def load_data(self) -> None:
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for user in self.users:
                        self.tasks[user] = [Task.from_dict(task_data) for task_data in data.get(user, [])]
            except (json.JSONDecodeError, KeyError):
                print("Warning: Could not load existing data. Starting fresh.")
    
    def save_data(self) -> None:
        """Save tasks to JSON file."""
        data = {}
        for user in self.users:
            data[user] = [task.to_dict() for task in self.tasks[user]]
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def login(self) -> None:
        """Handle user login."""
        print("\n" + "="*50)
        print("TASK MANAGER LOGIN")
        print("="*50)
        
        for i, user in enumerate(self.users, 1):
            print(f"{i}. {user}")
        
        while True:
            try:
                choice = input(f"\nSelect user (1-{len(self.users)}): ").strip()
                user_index = int(choice) - 1
                if 0 <= user_index < len(self.users):
                    self.current_user = self.users[user_index]
                    print(f"\nWelcome, {self.current_user}!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def display_main_menu(self) -> None:
        """Display the main menu options."""
        print(f"\n{'='*50}")
        print(f"TASK MANAGER - {self.current_user}")
        print(f"{'='*50}")
        print("1. View My Tasks")
        print("2. Add New Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. View All Users' Tasks")
        print("7. Switch User")
        print("8. Exit")
        print(f"{'='*50}")
    
    def view_my_tasks(self) -> None:
        """Display current user's tasks."""
        user_tasks = self.tasks[self.current_user]
        
        if not user_tasks:
            print(f"\n{self.current_user} has no tasks yet.")
            return
        
        print(f"\n{self.current_user}'s Tasks:")
        print("-" * 60)
        
        # Sort tasks by priority and completion status
        sorted_tasks = sorted(user_tasks, key=lambda t: (t.completed, {"High": 0, "Medium": 1, "Low": 2}.get(t.priority, 1)))
        
        for i, task in enumerate(sorted_tasks, 1):
            print(f"{i:2d}. {task}")
            if task.description:
                print(f"     Description: {task.description}")
            print(f"     Created: {task.created_date}")
            print()
    
    def add_task(self) -> None:
        """Add a new task."""
        print("\nAdd New Task")
        print("-" * 30)
        
        title = input("Task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return
        
        description = input("Task description (optional): ").strip()
        
        print("\nPriority levels:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        
        priority_choice = input("Select priority (1-3, default: Medium): ").strip()
        priority_map = {"1": "High", "2": "Medium", "3": "Low"}
        priority = priority_map.get(priority_choice, "Medium")
        
        due_date = input("Due date (YYYY-MM-DD format, optional): ").strip()
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Task added without due date.")
                due_date = None
        
        task = Task(title, description, priority, due_date)
        self.tasks[self.current_user].append(task)
        self.save_data()
        
        print(f"\nTask '{title}' added successfully!")
    
    def edit_task(self) -> None:
        """Edit an existing task."""
        user_tasks = self.tasks[self.current_user]
        
        if not user_tasks:
            print(f"\n{self.current_user} has no tasks to edit.")
            return
        
        self.view_my_tasks()
        
        try:
            task_num = int(input(f"\nEnter task number to edit (1-{len(user_tasks)}): ")) - 1
            if 0 <= task_num < len(user_tasks):
                task = user_tasks[task_num]
                self._edit_task_details(task)
                self.save_data()
                print("\nTask updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def _edit_task_details(self, task: Task) -> None:
        """Edit specific task details."""
        print(f"\nEditing task: {task.title}")
        print("-" * 40)
        
        new_title = input(f"New title (current: {task.title}): ").strip()
        if new_title:
            task.title = new_title
        
        new_description = input(f"New description (current: {task.description}): ").strip()
        task.description = new_description
        
        print(f"\nCurrent priority: {task.priority}")
        print("1. High")
        print("2. Medium") 
        print("3. Low")
        
        priority_choice = input("New priority (1-3, or press Enter to keep current): ").strip()
        priority_map = {"1": "High", "2": "Medium", "3": "Low"}
        if priority_choice in priority_map:
            task.priority = priority_map[priority_choice]
        
        new_due_date = input(f"New due date (current: {task.due_date or 'None'}, YYYY-MM-DD): ").strip()
        if new_due_date:
            try:
                datetime.strptime(new_due_date, "%Y-%m-%d")
                task.due_date = new_due_date
            except ValueError:
                print("Invalid date format. Due date not updated.")
        elif new_due_date == "":
            task.due_date = None
    
    def delete_task(self) -> None:
        """Delete a task."""
        user_tasks = self.tasks[self.current_user]
        
        if not user_tasks:
            print(f"\n{self.current_user} has no tasks to delete.")
            return
        
        self.view_my_tasks()
        
        try:
            task_num = int(input(f"\nEnter task number to delete (1-{len(user_tasks)}): ")) - 1
            if 0 <= task_num < len(user_tasks):
                task = user_tasks[task_num]
                confirm = input(f"\nAre you sure you want to delete '{task.title}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    del user_tasks[task_num]
                    self.save_data()
                    print("Task deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def toggle_task_completion(self) -> None:
        """Toggle task completion status."""
        user_tasks = self.tasks[self.current_user]
        
        if not user_tasks:
            print(f"\n{self.current_user} has no tasks.")
            return
        
        self.view_my_tasks()
        
        try:
            task_num = int(input(f"\nEnter task number to toggle completion (1-{len(user_tasks)}): ")) - 1
            if 0 <= task_num < len(user_tasks):
                task = user_tasks[task_num]
                task.completed = not task.completed
                status = "completed" if task.completed else "marked as incomplete"
                self.save_data()
                print(f"\nTask '{task.title}' {status}!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def view_all_users_tasks(self) -> None:
        """Display tasks for all users."""
        print("\nAll Users' Tasks")
        print("=" * 60)
        
        for user in self.users:
            user_tasks = self.tasks[user]
            print(f"\n{user} ({len(user_tasks)} tasks):")
            print("-" * 40)
            
            if not user_tasks:
                print("No tasks.")
                continue
            
            sorted_tasks = sorted(user_tasks, key=lambda t: (t.completed, {"High": 0, "Medium": 1, "Low": 2}.get(t.priority, 1)))
            
            for task in sorted_tasks:
                print(f"  {task}")
        
        print("\n" + "=" * 60)
    
    def run(self) -> None:
        """Main application loop."""
        print("Welcome to Task Manager!")
        
        # Initial login
        self.login()
        
        while True:
            self.display_main_menu()
            
            try:
                choice = input("Enter your choice (1-8): ").strip()
                
                if choice == "1":
                    self.view_my_tasks()
                elif choice == "2":
                    self.add_task()
                elif choice == "3":
                    self.edit_task()
                elif choice == "4":
                    self.delete_task()
                elif choice == "5":
                    self.toggle_task_completion()
                elif choice == "6":
                    self.view_all_users_tasks()
                elif choice == "7":
                    self.login()
                elif choice == "8":
                    print("\nThank you for using Task Manager. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")


def main():
    """Entry point of the application."""
    try:
        task_manager = TaskManager()
        task_manager.run()
    except Exception as e:
        print(f"Application error: {e}")
        print("Please try running the application again.")


if __name__ == "__main__":
    main()
