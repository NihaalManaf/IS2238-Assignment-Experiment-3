#!/usr/bin/env python3
"""
Task Manager App - A simple command-line task management system for two users.

This application allows two users to manage their tasks with features including:
- Adding, editing, deleting, and marking tasks as complete
- Assigning due dates and priorities
- Viewing tasks separately for each user
- Data persistence using JSON file storage

Author: Senior Python Backend Engineer
Python Version: 3.11+
Dependencies: Standard library only
"""

import json
import os
import sys
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class Priority(Enum):
    """Task priority levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    """Represents a single task with all its properties."""
    id: int
    title: str
    description: str
    due_date: str
    priority: Priority
    completed: bool
    user: str
    created_at: str
    updated_at: str

    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority.value,
            'completed': self.completed,
            'user': self.user,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create Task instance from dictionary."""
        return cls(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            priority=Priority(data['priority']),
            completed=data['completed'],
            user=data['user'],
            created_at=data['created_at'],
            updated_at=data['updated_at']
        )


class TaskManager:
    """Main task management system."""
    
    def __init__(self, data_file: str = "tasks.json"):
        """Initialize the task manager with data file path."""
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.next_id = 1
        self.users = ["User1", "User2"]
        self.load_data()

    def load_data(self) -> None:
        """Load tasks from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
                    self.next_id = data.get('next_id', 1)
            else:
                self.tasks = []
                self.next_id = 1
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error loading data: {e}")
            print("Starting with empty task list.")
            self.tasks = []
            self.next_id = 1

    def save_data(self) -> None:
        """Save tasks to JSON file."""
        try:
            data = {
                'tasks': [task.to_dict() for task in self.tasks],
                'next_id': self.next_id
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except (OSError, IOError) as e:
            print(f"Error saving data: {e}")

    def add_task(self, title: str, description: str, due_date: str, 
                 priority: Priority, user: str) -> Task:
        """Add a new task."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        if not self._is_valid_date(due_date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        
        if user not in self.users:
            raise ValueError(f"Invalid user. Must be one of: {', '.join(self.users)}")

        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip(),
            due_date=due_date,
            priority=priority,
            completed=False,
            user=user,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        
        self.tasks.append(task)
        self.next_id += 1
        self.save_data()
        return task

    def edit_task(self, task_id: int, title: Optional[str] = None,
                  description: Optional[str] = None, due_date: Optional[str] = None,
                  priority: Optional[Priority] = None, user: Optional[str] = None) -> Task:
        """Edit an existing task."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        if due_date is not None:
            if not self._is_valid_date(due_date):
                raise ValueError("Invalid date format. Use YYYY-MM-DD")
            task.due_date = due_date

        if priority is not None:
            task.priority = priority

        if user is not None:
            if user not in self.users:
                raise ValueError(f"Invalid user. Must be one of: {', '.join(self.users)}")
            task.user = user

        task.updated_at = datetime.now().isoformat()
        self.save_data()
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        self.save_data()
        return True

    def mark_task_complete(self, task_id: int, completed: bool = True) -> Task:
        """Mark a task as complete or incomplete."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        
        task.completed = completed
        task.updated_at = datetime.now().isoformat()
        self.save_data()
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        return next((task for task in self.tasks if task.id == task_id), None)

    def get_tasks_by_user(self, user: str) -> List[Task]:
        """Get all tasks for a specific user."""
        return [task for task in self.tasks if task.user == user]

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self.tasks.copy()

    def _is_valid_date(self, date_string: str) -> bool:
        """Validate date format YYYY-MM-DD."""
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_task_statistics(self, user: str) -> Dict[str, int]:
        """Get task statistics for a user."""
        user_tasks = self.get_tasks_by_user(user)
        total = len(user_tasks)
        completed = sum(1 for task in user_tasks if task.completed)
        pending = total - completed
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending
        }


class TaskManagerCLI:
    """Command-line interface for the Task Manager."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.task_manager = TaskManager()
        self.current_user = None

    def run(self) -> None:
        """Main application loop."""
        print("=" * 60)
        print("           TASK MANAGER APP")
        print("=" * 60)
        
        while True:
            try:
                if self.current_user is None:
                    self._show_user_selection()
                else:
                    self._show_main_menu()
            except KeyboardInterrupt:
                print("\n\nExiting Task Manager. Goodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
                print("Please try again.")

    def _show_user_selection(self) -> None:
        """Show user selection menu."""
        print("\nSelect User:")
        for i, user in enumerate(self.task_manager.users, 1):
            stats = self.task_manager.get_task_statistics(user)
            print(f"{i}. {user} (Tasks: {stats['total']}, Completed: {stats['completed']}, Pending: {stats['pending']})")
        print("0. Exit")
        
        choice = self._get_user_input("Enter your choice: ")
        
        if choice == "0":
            print("Goodbye!")
            sys.exit(0)
        elif choice in ["1", "2"]:
            self.current_user = self.task_manager.users[int(choice) - 1]
            print(f"\nWelcome, {self.current_user}!")
        else:
            print("Invalid choice. Please try again.")

    def _show_main_menu(self) -> None:
        """Show main menu for the current user."""
        print(f"\n{'='*50}")
        print(f"TASK MANAGER - {self.current_user}")
        print(f"{'='*50}")
        
        stats = self.task_manager.get_task_statistics(self.current_user)
        print(f"Tasks: {stats['total']} | Completed: {stats['completed']} | Pending: {stats['pending']}")
        
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Switch User")
        print("0. Exit")
        
        choice = self._get_user_input("Enter your choice: ")
        
        if choice == "1":
            self._view_tasks()
        elif choice == "2":
            self._add_task()
        elif choice == "3":
            self._edit_task()
        elif choice == "4":
            self._delete_task()
        elif choice == "5":
            self._toggle_task_completion()
        elif choice == "6":
            self.current_user = None
        elif choice == "0":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

    def _view_tasks(self) -> None:
        """Display tasks for the current user."""
        tasks = self.task_manager.get_tasks_by_user(self.current_user)
        
        if not tasks:
            print(f"\nNo tasks found for {self.current_user}.")
            return
        
        print(f"\n{'='*80}")
        print(f"TASKS FOR {self.current_user}")
        print(f"{'='*80}")
        
        # Sort tasks by due date and priority
        tasks.sort(key=lambda t: (t.due_date, t.priority.value))
        
        for task in tasks:
            status = "✓ COMPLETED" if task.completed else "○ PENDING"
            priority_color = self._get_priority_display(task.priority)
            
            print(f"\nID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print(f"Priority: {priority_color}")
            print(f"Status: {status}")
            print(f"Created: {task.created_at[:10]}")
            print("-" * 40)

    def _add_task(self) -> None:
        """Add a new task."""
        print(f"\n{'='*50}")
        print("ADD NEW TASK")
        print(f"{'='*50}")
        
        try:
            title = self._get_user_input("Enter task title: ")
            description = self._get_user_input("Enter task description: ")
            due_date = self._get_user_input("Enter due date (YYYY-MM-DD): ")
            
            print("\nPriority levels:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            
            priority_choice = self._get_user_input("Select priority (1-3): ")
            priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH}
            
            if priority_choice not in priority_map:
                print("Invalid priority choice.")
                return
            
            priority = priority_map[priority_choice]
            
            task = self.task_manager.add_task(title, description, due_date, priority, self.current_user)
            print(f"\nTask added successfully! Task ID: {task.id}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _edit_task(self) -> None:
        """Edit an existing task."""
        tasks = self.task_manager.get_tasks_by_user(self.current_user)
        
        if not tasks:
            print(f"\nNo tasks found for {self.current_user}.")
            return
        
        print(f"\n{'='*50}")
        print("EDIT TASK")
        print(f"{'='*50}")
        
        try:
            task_id = int(self._get_user_input("Enter task ID to edit: "))
            task = self.task_manager.get_task_by_id(task_id)
            
            if not task or task.user != self.current_user:
                print("Task not found or doesn't belong to you.")
                return
            
            print(f"\nCurrent task details:")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print(f"Priority: {task.priority.value}")
            
            print("\nEnter new values (press Enter to keep current value):")
            
            new_title = self._get_user_input(f"New title [{task.title}]: ")
            new_description = self._get_user_input(f"New description [{task.description}]: ")
            new_due_date = self._get_user_input(f"New due date [{task.due_date}]: ")
            
            print("\nPriority levels:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            priority_choice = self._get_user_input(f"New priority (1-3) [{task.priority.value}]: ")
            
            # Prepare edit parameters
            edit_params = {}
            
            if new_title.strip():
                edit_params['title'] = new_title
            if new_description.strip():
                edit_params['description'] = new_description
            if new_due_date.strip():
                edit_params['due_date'] = new_due_date
            if priority_choice.strip() and priority_choice in ["1", "2", "3"]:
                priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH}
                edit_params['priority'] = priority_map[priority_choice]
            
            if edit_params:
                self.task_manager.edit_task(task_id, **edit_params)
                print("Task updated successfully!")
            else:
                print("No changes made.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _delete_task(self) -> None:
        """Delete a task."""
        tasks = self.task_manager.get_tasks_by_user(self.current_user)
        
        if not tasks:
            print(f"\nNo tasks found for {self.current_user}.")
            return
        
        print(f"\n{'='*50}")
        print("DELETE TASK")
        print(f"{'='*50}")
        
        try:
            task_id = int(self._get_user_input("Enter task ID to delete: "))
            task = self.task_manager.get_task_by_id(task_id)
            
            if not task or task.user != self.current_user:
                print("Task not found or doesn't belong to you.")
                return
            
            print(f"\nTask to delete:")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            
            confirm = self._get_user_input("Are you sure you want to delete this task? (y/N): ")
            
            if confirm.lower() in ['y', 'yes']:
                if self.task_manager.delete_task(task_id):
                    print("Task deleted successfully!")
                else:
                    print("Failed to delete task.")
            else:
                print("Deletion cancelled.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _toggle_task_completion(self) -> None:
        """Toggle task completion status."""
        tasks = self.task_manager.get_tasks_by_user(self.current_user)
        
        if not tasks:
            print(f"\nNo tasks found for {self.current_user}.")
            return
        
        print(f"\n{'='*50}")
        print("TOGGLE TASK COMPLETION")
        print(f"{'='*50}")
        
        try:
            task_id = int(self._get_user_input("Enter task ID: "))
            task = self.task_manager.get_task_by_id(task_id)
            
            if not task or task.user != self.current_user:
                print("Task not found or doesn't belong to you.")
                return
            
            new_status = not task.completed
            self.task_manager.mark_task_complete(task_id, new_status)
            
            status_text = "completed" if new_status else "marked as pending"
            print(f"Task '{task.title}' has been {status_text}!")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _get_user_input(self, prompt: str) -> str:
        """Get user input with proper handling."""
        try:
            return input(prompt).strip()
        except EOFError:
            print("\nExiting...")
            sys.exit(0)

    def _get_priority_display(self, priority: Priority) -> str:
        """Get formatted priority display."""
        priority_colors = {
            Priority.LOW: "🟢 LOW",
            Priority.MEDIUM: "🟡 MEDIUM", 
            Priority.HIGH: "🔴 HIGH"
        }
        return priority_colors.get(priority, priority.value.upper())


def main():
    """Main entry point for the application."""
    try:
        app = TaskManagerCLI()
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
