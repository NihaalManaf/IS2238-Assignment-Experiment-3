#!/usr/bin/env python3
"""
Simple Task Manager App
A command-line task management application for two users with in-memory storage.
"""

import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    """Task priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    """Represents a single task"""
    title: str
    description: str
    due_date: str
    priority: Priority
    completed: bool = False
    created_date: str = None
    
    def __post_init__(self):
        """Set created date when task is initialized"""
        if self.created_date is None:
            self.created_date = datetime.date.today().isoformat()


class TaskManager:
    """Main task manager class handling all operations"""
    
    def __init__(self):
        """Initialize the task manager with empty data structures"""
        self.users: Dict[str, List[Task]] = {}
        self.current_user: Optional[str] = None
    
    def add_user(self, username: str) -> bool:
        """Add a new user to the system"""
        if username in self.users:
            return False
        self.users[username] = []
        return True
    
    def login_user(self, username: str) -> bool:
        """Login a user"""
        if username in self.users:
            self.current_user = username
            return True
        return False
    
    def logout_user(self) -> None:
        """Logout current user"""
        self.current_user = None
    
    def validate_date(self, date_str: str) -> bool:
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def validate_priority(self, priority_str: str) -> bool:
        """Validate priority level"""
        try:
            Priority(priority_str.lower())
            return True
        except ValueError:
            return False
    
    def is_duplicate_title(self, title: str) -> bool:
        """Check if task title already exists for current user"""
        if self.current_user is None:
            return False
        
        for task in self.users[self.current_user]:
            if task.title.lower() == title.lower():
                return True
        return False
    
    def add_task(self, title: str, description: str, due_date: str, priority: str) -> str:
        """Add a new task for the current user"""
        if self.current_user is None:
            return "Error: No user logged in"
        
        if not title.strip():
            return "Error: Task title cannot be empty"
        
        if self.is_duplicate_title(title):
            return "Error: Task title already exists"
        
        if not self.validate_date(due_date):
            return "Error: Invalid date format. Use YYYY-MM-DD"
        
        if not self.validate_priority(priority):
            return "Error: Invalid priority. Use 'low', 'medium', or 'high'"
        
        task = Task(
            title=title.strip(),
            description=description.strip(),
            due_date=due_date,
            priority=Priority(priority.lower())
        )
        
        self.users[self.current_user].append(task)
        return f"Task '{title}' added successfully"
    
    def edit_task(self, title: str, new_title: str = None, new_description: str = None, 
                  new_due_date: str = None, new_priority: str = None) -> str:
        """Edit an existing task"""
        if self.current_user is None:
            return "Error: No user logged in"
        
        task = self.get_task_by_title(title)
        if task is None:
            return "Error: Task not found"
        
        if new_title is not None:
            if not new_title.strip():
                return "Error: Task title cannot be empty"
            if new_title.strip().lower() != title.lower() and self.is_duplicate_title(new_title):
                return "Error: New task title already exists"
            task.title = new_title.strip()
        
        if new_description is not None:
            task.description = new_description.strip()
        
        if new_due_date is not None:
            if not self.validate_date(new_due_date):
                return "Error: Invalid date format. Use YYYY-MM-DD"
            task.due_date = new_due_date
        
        if new_priority is not None:
            if not self.validate_priority(new_priority):
                return "Error: Invalid priority. Use 'low', 'medium', or 'high'"
            task.priority = Priority(new_priority.lower())
        
        return f"Task '{title}' updated successfully"
    
    def delete_task(self, title: str) -> str:
        """Delete a task"""
        if self.current_user is None:
            return "Error: No user logged in"
        
        task = self.get_task_by_title(title)
        if task is None:
            return "Error: Task not found"
        
        self.users[self.current_user].remove(task)
        return f"Task '{title}' deleted successfully"
    
    def mark_task_complete(self, title: str) -> str:
        """Mark a task as complete"""
        if self.current_user is None:
            return "Error: No user logged in"
        
        task = self.get_task_by_title(title)
        if task is None:
            return "Error: Task not found"
        
        task.completed = True
        return f"Task '{title}' marked as complete"
    
    def get_task_by_title(self, title: str) -> Optional[Task]:
        """Get a task by its title for the current user"""
        if self.current_user is None:
            return None
        
        for task in self.users[self.current_user]:
            if task.title.lower() == title.lower():
                return task
        return None
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks for the current user"""
        if self.current_user is None:
            return []
        return self.users[self.current_user].copy()
    
    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """Get tasks filtered by priority"""
        if self.current_user is None:
            return []
        
        return [task for task in self.users[self.current_user] if task.priority == priority]
    
    def get_tasks_by_status(self, completed: bool) -> List[Task]:
        """Get tasks filtered by completion status"""
        if self.current_user is None:
            return []
        
        return [task for task in self.users[self.current_user] if task.completed == completed]


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("TASK MANAGER")
    print("="*50)
    print("1. Login")
    print("2. Add Task")
    print("3. View All Tasks")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Mark Task Complete")
    print("7. View Tasks by Priority")
    print("8. View Tasks by Status")
    print("9. Logout")
    print("0. Exit")
    print("-"*50)


def display_tasks(tasks: List[Task], title: str = "Tasks"):
    """Display a list of tasks in a formatted way"""
    print(f"\n{title}:")
    print("-" * 80)
    
    if not tasks:
        print("No tasks found.")
        return
    
    print(f"{'Title':<20} {'Description':<25} {'Due Date':<12} {'Priority':<8} {'Status':<10} {'Created':<12}")
    print("-" * 80)
    
    for task in tasks:
        status = "Complete" if task.completed else "Pending"
        print(f"{task.title:<20} {task.description[:24]:<25} {task.due_date:<12} "
              f"{task.priority.value:<8} {status:<10} {task.created_date:<12}")


def get_user_input(prompt: str) -> str:
    """Get user input with error handling"""
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)


def main():
    """Main application loop"""
    task_manager = TaskManager()
    
    # Initialize with two users
    task_manager.add_user("user1")
    task_manager.add_user("user2")
    
    print("Welcome to Task Manager!")
    print("Available users: user1, user2")
    
    while True:
        display_menu()
        
        if task_manager.current_user:
            print(f"Logged in as: {task_manager.current_user}")
        
        choice = get_user_input("Enter your choice: ")
        
        if choice == "0":
            print("Goodbye!")
            break
        
        elif choice == "1":
            username = get_user_input("Enter username: ")
            if task_manager.login_user(username):
                print(f"Successfully logged in as {username}")
            else:
                print("Error: Invalid username")
        
        elif choice == "2":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            title = get_user_input("Enter task title: ")
            description = get_user_input("Enter task description: ")
            due_date = get_user_input("Enter due date (YYYY-MM-DD): ")
            priority = get_user_input("Enter priority (low/medium/high): ")
            
            result = task_manager.add_task(title, description, due_date, priority)
            print(result)
        
        elif choice == "3":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            tasks = task_manager.get_all_tasks()
            display_tasks(tasks, f"All Tasks for {task_manager.current_user}")
        
        elif choice == "4":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            title = get_user_input("Enter task title to edit: ")
            
            print("Enter new values (press Enter to keep current value):")
            new_title = get_user_input(f"New title: ")
            new_description = get_user_input(f"New description: ")
            new_due_date = get_user_input(f"New due date (YYYY-MM-DD): ")
            new_priority = get_user_input(f"New priority (low/medium/high): ")
            
            # Convert empty strings to None
            new_title = new_title if new_title else None
            new_description = new_description if new_description else None
            new_due_date = new_due_date if new_due_date else None
            new_priority = new_priority if new_priority else None
            
            result = task_manager.edit_task(title, new_title, new_description, new_due_date, new_priority)
            print(result)
        
        elif choice == "5":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            title = get_user_input("Enter task title to delete: ")
            result = task_manager.delete_task(title)
            print(result)
        
        elif choice == "6":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            title = get_user_input("Enter task title to mark complete: ")
            result = task_manager.mark_task_complete(title)
            print(result)
        
        elif choice == "7":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            priority_input = get_user_input("Enter priority (low/medium/high): ")
            if task_manager.validate_priority(priority_input):
                priority = Priority(priority_input.lower())
                tasks = task_manager.get_tasks_by_priority(priority)
                display_tasks(tasks, f"{priority.value.title()} Priority Tasks")
            else:
                print("Error: Invalid priority")
        
        elif choice == "8":
            if task_manager.current_user is None:
                print("Error: Please login first")
                continue
            
            status_input = get_user_input("Enter status (completed/pending): ").lower()
            if status_input == "completed":
                tasks = task_manager.get_tasks_by_status(True)
                display_tasks(tasks, "Completed Tasks")
            elif status_input == "pending":
                tasks = task_manager.get_tasks_by_status(False)
                display_tasks(tasks, "Pending Tasks")
            else:
                print("Error: Invalid status. Use 'completed' or 'pending'")
        
        elif choice == "9":
            if task_manager.current_user:
                print(f"Successfully logged out from {task_manager.current_user}")
                task_manager.logout_user()
            else:
                print("Error: No user logged in")
        
        else:
            print("Error: Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
