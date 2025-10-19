#!/usr/bin/env python3
"""
Simple Task Manager App for Two Users
A command-line task management application that allows two users to manage their tasks.
"""

import datetime
from typing import Dict, List, Optional, Tuple


class Task:
    """Represents a single task with all its properties."""
    
    def __init__(self, title: str, description: str = "", priority: str = "medium", 
                 due_date: Optional[str] = None, user: str = ""):
        self.title = title
        self.description = description
        self.priority = priority  # "low", "medium", "high"
        self.due_date = due_date
        self.user = user
        self.completed = False
        self.created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def __str__(self) -> str:
        """String representation of the task for display."""
        status = "✓" if self.completed else "○"
        priority_symbol = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(self.priority, "🟡")
        due_info = f" (Due: {self.due_date})" if self.due_date else ""
        return f"{status} {priority_symbol} {self.title}{due_info}"


class TaskManager:
    """Main task manager class that handles all task operations."""
    
    def __init__(self):
        # Store tasks for each user separately
        self.users = {"user1": [], "user2": []}
        self.current_user = "user1"
    
    def add_task(self, title: str, description: str = "", priority: str = "medium", 
                 due_date: Optional[str] = None) -> bool:
        """Add a new task for the current user."""
        if not title.strip():
            print("Error: Task title cannot be empty.")
            return False
        
        # Validate priority
        if priority not in ["low", "medium", "high"]:
            print("Error: Priority must be 'low', 'medium', or 'high'.")
            return False
        
        # Validate due date format if provided
        if due_date:
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Due date must be in YYYY-MM-DD format.")
                return False
        
        task = Task(title, description, priority, due_date, self.current_user)
        self.users[self.current_user].append(task)
        print(f"Task '{title}' added successfully!")
        return True
    
    def edit_task(self, task_index: int, title: str = None, description: str = None, 
                  priority: str = None, due_date: str = None) -> bool:
        """Edit an existing task."""
        if not self._is_valid_task_index(task_index):
            return False
        
        task = self.users[self.current_user][task_index]
        
        if title is not None:
            if not title.strip():
                print("Error: Task title cannot be empty.")
                return False
            task.title = title
        
        if description is not None:
            task.description = description
        
        if priority is not None:
            if priority not in ["low", "medium", "high"]:
                print("Error: Priority must be 'low', 'medium', or 'high'.")
                return False
            task.priority = priority
        
        if due_date is not None:
            if due_date:
                try:
                    datetime.datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print("Error: Due date must be in YYYY-MM-DD format.")
                    return False
            task.due_date = due_date
        
        print(f"Task '{task.title}' updated successfully!")
        return True
    
    def delete_task(self, task_index: int) -> bool:
        """Delete a task."""
        if not self._is_valid_task_index(task_index):
            return False
        
        task = self.users[self.current_user].pop(task_index)
        print(f"Task '{task.title}' deleted successfully!")
        return True
    
    def mark_task_complete(self, task_index: int) -> bool:
        """Mark a task as complete or incomplete."""
        if not self._is_valid_task_index(task_index):
            return False
        
        task = self.users[self.current_user][task_index]
        task.completed = not task.completed
        status = "completed" if task.completed else "incomplete"
        print(f"Task '{task.title}' marked as {status}!")
        return True
    
    def list_tasks(self, show_completed: bool = True) -> None:
        """Display all tasks for the current user."""
        tasks = self.users[self.current_user]
        
        if not tasks:
            print(f"No tasks found for {self.current_user}.")
            return
        
        print(f"\n=== Tasks for {self.current_user.upper()} ===")
        for i, task in enumerate(tasks):
            if show_completed or not task.completed:
                print(f"{i + 1}. {task}")
                if task.description:
                    print(f"   Description: {task.description}")
                print(f"   Created: {task.created_date}")
                print()
    
    def switch_user(self, user: str) -> bool:
        """Switch between users."""
        if user not in self.users:
            print("Error: Invalid user. Use 'user1' or 'user2'.")
            return False
        
        self.current_user = user
        print(f"Switched to {user}.")
        return True
    
    def _is_valid_task_index(self, index: int) -> bool:
        """Check if the task index is valid."""
        if index < 1 or index > len(self.users[self.current_user]):
            print(f"Error: Invalid task number. Please enter a number between 1 and {len(self.users[self.current_user])}.")
            return False
        return True
    
    def get_task_stats(self) -> Dict[str, int]:
        """Get statistics for the current user's tasks."""
        tasks = self.users[self.current_user]
        total = len(tasks)
        completed = sum(1 for task in tasks if task.completed)
        pending = total - completed
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("           TASK MANAGER APP")
    print("="*50)
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Mark Task Complete/Incomplete")
    print("5. List All Tasks")
    print("6. List Pending Tasks Only")
    print("7. Switch User")
    print("8. Show Task Statistics")
    print("9. Exit")
    print("="*50)


def get_user_input(prompt: str, input_type: str = "string") -> str:
    """Get user input with basic validation."""
    while True:
        try:
            value = input(prompt).strip()
            if input_type == "string" and not value:
                print("This field cannot be empty. Please try again.")
                continue
            return value
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)


def get_task_details() -> Tuple[str, str, str, Optional[str]]:
    """Get task details from user input."""
    title = get_user_input("Enter task title: ")
    description = get_user_input("Enter task description (optional): ")
    
    print("Priority options: low, medium, high")
    priority = get_user_input("Enter priority (default: medium): ")
    if not priority:
        priority = "medium"
    
    due_date = get_user_input("Enter due date in YYYY-MM-DD format (optional): ")
    if not due_date:
        due_date = None
    
    return title, description, priority, due_date


def main():
    """Main application loop."""
    print("Welcome to the Task Manager App!")
    print("This app supports two users: 'user1' and 'user2'")
    
    task_manager = TaskManager()
    
    while True:
        display_menu()
        choice = get_user_input(f"\nCurrent user: {task_manager.current_user}\nEnter your choice (1-9): ")
        
        if choice == "1":
            # Add Task
            print("\n--- ADD NEW TASK ---")
            title, description, priority, due_date = get_task_details()
            task_manager.add_task(title, description, priority, due_date)
        
        elif choice == "2":
            # Edit Task
            print("\n--- EDIT TASK ---")
            task_manager.list_tasks()
            if task_manager.users[task_manager.current_user]:
                try:
                    task_num = int(get_user_input("Enter task number to edit: "))
                    print("\nLeave fields empty to keep current values:")
                    title = get_user_input("Enter new title (optional): ")
                    description = get_user_input("Enter new description (optional): ")
                    priority = get_user_input("Enter new priority (optional): ")
                    due_date = get_user_input("Enter new due date (optional): ")
                    
                    task_manager.edit_task(task_num, 
                                         title if title else None,
                                         description if description else None,
                                         priority if priority else None,
                                         due_date if due_date else None)
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        elif choice == "3":
            # Delete Task
            print("\n--- DELETE TASK ---")
            task_manager.list_tasks()
            if task_manager.users[task_manager.current_user]:
                try:
                    task_num = int(get_user_input("Enter task number to delete: "))
                    confirm = get_user_input("Are you sure? (yes/no): ").lower()
                    if confirm in ["yes", "y"]:
                        task_manager.delete_task(task_num)
                    else:
                        print("Deletion cancelled.")
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        elif choice == "4":
            # Mark Task Complete/Incomplete
            print("\n--- MARK TASK COMPLETE/INCOMPLETE ---")
            task_manager.list_tasks()
            if task_manager.users[task_manager.current_user]:
                try:
                    task_num = int(get_user_input("Enter task number to toggle: "))
                    task_manager.mark_task_complete(task_num)
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        elif choice == "5":
            # List All Tasks
            print("\n--- ALL TASKS ---")
            task_manager.list_tasks(show_completed=True)
        
        elif choice == "6":
            # List Pending Tasks Only
            print("\n--- PENDING TASKS ---")
            task_manager.list_tasks(show_completed=False)
        
        elif choice == "7":
            # Switch User
            print("\n--- SWITCH USER ---")
            print("Available users: user1, user2")
            new_user = get_user_input("Enter user name: ")
            task_manager.switch_user(new_user)
        
        elif choice == "8":
            # Show Task Statistics
            print("\n--- TASK STATISTICS ---")
            stats = task_manager.get_task_stats()
            print(f"Total tasks: {stats['total']}")
            print(f"Completed: {stats['completed']}")
            print(f"Pending: {stats['pending']}")
            if stats['total'] > 0:
                completion_rate = (stats['completed'] / stats['total']) * 100
                print(f"Completion rate: {completion_rate:.1f}%")
        
        elif choice == "9":
            # Exit
            print("\nThank you for using the Task Manager App!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
