#!/usr/bin/env python3
"""
Task Manager App - A command-line task management system for two users

This application provides a comprehensive task management system with the following features:
- Add, edit, delete tasks
- Mark tasks as complete/incomplete
- Assign due dates (YYYY-MM-DD format)
- Set task priorities (High, Medium, Low)
- View tasks per user
- Data persistence using JSON file storage

Author: Senior Python Backend Engineer
Version: 1.0
Python Version: 3.11+
Dependencies: Standard library only
"""

import json
import os
import sys
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple
from enum import Enum
import uuid


class Priority(Enum):
    """Task priority levels"""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class TaskStatus(Enum):
    """Task completion status"""
    PENDING = "Pending"
    COMPLETED = "Completed"


class Task:
    """
    Represents a single task in the task management system.
    
    Attributes:
        id (str): Unique identifier for the task
        title (str): Task title/description
        description (str): Detailed task description
        priority (Priority): Task priority level
        due_date (date): Task due date
        status (TaskStatus): Task completion status
        created_at (datetime): Task creation timestamp
        updated_at (datetime): Last modification timestamp
        user_id (str): ID of the user who owns this task
    """
    
    def __init__(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM,
                 due_date: Optional[date] = None, user_id: str = ""):
        """
        Initialize a new task.
        
        Args:
            title: Task title
            description: Task description
            priority: Task priority level
            due_date: Task due date
            user_id: ID of the user who owns this task
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.user_id = user_id
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'user_id': self.user_id
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary (JSON deserialization)"""
        task = cls(
            title=data['title'],
            description=data.get('description', ''),
            priority=Priority(data['priority']),
            due_date=datetime.fromisoformat(data['due_date']).date() if data.get('due_date') else None,
            user_id=data['user_id']
        )
        task.id = data['id']
        task.status = TaskStatus(data['status'])
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.updated_at = datetime.fromisoformat(data['updated_at'])
        return task
    
    def update(self, title: str = None, description: str = None, priority: Priority = None,
               due_date: Optional[date] = None, status: TaskStatus = None):
        """
        Update task attributes.
        
        Args:
            title: New task title
            description: New task description
            priority: New task priority
            due_date: New task due date
            status: New task status
        """
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status
        
        self.updated_at = datetime.now()
    
    def mark_complete(self):
        """Mark task as completed"""
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()
    
    def mark_pending(self):
        """Mark task as pending"""
        self.status = TaskStatus.PENDING
        self.updated_at = datetime.now()
    
    def is_overdue(self) -> bool:
        """Check if task is overdue"""
        if not self.due_date or self.status == TaskStatus.COMPLETED:
            return False
        return self.due_date < date.today()
    
    def __str__(self) -> str:
        """String representation of the task"""
        status_icon = "✓" if self.status == TaskStatus.COMPLETED else "○"
        priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}[self.priority.value]
        overdue_indicator = " ⚠️ OVERDUE" if self.is_overdue() else ""
        
        due_date_str = f"Due: {self.due_date}" if self.due_date else "No due date"
        
        return (f"{status_icon} [{self.id[:8]}] {self.title} "
                f"{priority_icon} {due_date_str}{overdue_indicator}")


class User:
    """
    Represents a user in the task management system.
    
    Attributes:
        id (str): Unique user identifier
        name (str): User's display name
        email (str): User's email address
        created_at (datetime): User creation timestamp
    """
    
    def __init__(self, name: str, email: str):
        """
        Initialize a new user.
        
        Args:
            name: User's display name
            email: User's email address
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert user to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create user from dictionary (JSON deserialization)"""
        user = cls(data['name'], data['email'])
        user.id = data['id']
        user.created_at = datetime.fromisoformat(data['created_at'])
        return user
    
    def __str__(self) -> str:
        """String representation of the user"""
        return f"{self.name} ({self.email})"


class TaskManager:
    """
    Main task management system that handles all task operations.
    
    This class manages users, tasks, and provides methods for CRUD operations.
    It also handles data persistence using JSON file storage.
    """
    
    def __init__(self, data_file: str = "task_manager_data.json"):
        """
        Initialize the task manager.
        
        Args:
            data_file: Path to the JSON file for data persistence
        """
        self.data_file = data_file
        self.users: Dict[str, User] = {}
        self.tasks: Dict[str, Task] = {}
        self.current_user_id: Optional[str] = None
        self.load_data()
    
    def load_data(self):
        """Load data from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Load users
                for user_data in data.get('users', []):
                    user = User.from_dict(user_data)
                    self.users[user.id] = user
                
                # Load tasks
                for task_data in data.get('tasks', []):
                    task = Task.from_dict(task_data)
                    self.tasks[task.id] = task
                
                print(f"✓ Loaded {len(self.users)} users and {len(self.tasks)} tasks")
            else:
                print("✓ Starting with empty database")
        except Exception as e:
            print(f"⚠️ Error loading data: {e}")
            print("✓ Starting with empty database")
    
    def save_data(self):
        """Save data to JSON file"""
        try:
            data = {
                'users': [user.to_dict() for user in self.users.values()],
                'tasks': [task.to_dict() for task in self.tasks.values()]
            }
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print("✓ Data saved successfully")
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    
    def add_user(self, name: str, email: str) -> str:
        """
        Add a new user to the system.
        
        Args:
            name: User's display name
            email: User's email address
            
        Returns:
            User ID of the created user
        """
        # Validate email format
        if '@' not in email or '.' not in email.split('@')[1]:
            raise ValueError("Invalid email format")
        
        # Check if email already exists
        for user in self.users.values():
            if user.email.lower() == email.lower():
                raise ValueError("Email already exists")
        
        user = User(name, email)
        self.users[user.id] = user
        self.save_data()
        return user.id
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        return self.users.get(user_id)
    
    def list_users(self) -> List[User]:
        """Get list of all users"""
        return list(self.users.values())
    
    def set_current_user(self, user_id: str):
        """Set the current active user"""
        if user_id not in self.users:
            raise ValueError("User not found")
        self.current_user_id = user_id
    
    def get_current_user(self) -> Optional[User]:
        """Get the current active user"""
        if self.current_user_id:
            return self.users.get(self.current_user_id)
        return None
    
    def add_task(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM,
                 due_date: Optional[date] = None) -> str:
        """
        Add a new task for the current user.
        
        Args:
            title: Task title
            description: Task description
            priority: Task priority
            due_date: Task due date
            
        Returns:
            Task ID of the created task
        """
        if not self.current_user_id:
            raise ValueError("No user selected. Please select a user first.")
        
        task = Task(title, description, priority, due_date, self.current_user_id)
        self.tasks[task.id] = task
        self.save_data()
        return task.id
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """Get task by ID"""
        return self.tasks.get(task_id)
    
    def update_task(self, task_id: str, title: str = None, description: str = None,
                   priority: Priority = None, due_date: Optional[date] = None,
                   status: TaskStatus = None) -> bool:
        """
        Update an existing task.
        
        Args:
            task_id: ID of the task to update
            title: New task title
            description: New task description
            priority: New task priority
            due_date: New task due date
            status: New task status
            
        Returns:
            True if task was updated, False if task not found
        """
        task = self.tasks.get(task_id)
        if not task:
            return False
        
        task.update(title, description, priority, due_date, status)
        self.save_data()
        return True
    
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if task was deleted, False if task not found
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_data()
            return True
        return False
    
    def get_user_tasks(self, user_id: str = None) -> List[Task]:
        """
        Get all tasks for a specific user.
        
        Args:
            user_id: User ID (uses current user if not provided)
            
        Returns:
            List of tasks for the user
        """
        if user_id is None:
            user_id = self.current_user_id
        
        if not user_id:
            return []
        
        return [task for task in self.tasks.values() if task.user_id == user_id]
    
    def get_tasks_by_status(self, status: TaskStatus, user_id: str = None) -> List[Task]:
        """Get tasks filtered by status"""
        user_tasks = self.get_user_tasks(user_id)
        return [task for task in user_tasks if task.status == status]
    
    def get_tasks_by_priority(self, priority: Priority, user_id: str = None) -> List[Task]:
        """Get tasks filtered by priority"""
        user_tasks = self.get_user_tasks(user_id)
        return [task for task in user_tasks if task.priority == priority]
    
    def get_overdue_tasks(self, user_id: str = None) -> List[Task]:
        """Get overdue tasks for a user"""
        user_tasks = self.get_user_tasks(user_id)
        return [task for task in user_tasks if task.is_overdue()]
    
    def search_tasks(self, query: str, user_id: str = None) -> List[Task]:
        """
        Search tasks by title or description.
        
        Args:
            query: Search query
            user_id: User ID (uses current user if not provided)
            
        Returns:
            List of matching tasks
        """
        user_tasks = self.get_user_tasks(user_id)
        query_lower = query.lower()
        
        return [task for task in user_tasks 
                if query_lower in task.title.lower() or query_lower in task.description.lower()]


class TaskManagerCLI:
    """
    Command-line interface for the Task Manager application.
    
    This class handles user input, command parsing, and interaction with the TaskManager.
    """
    
    def __init__(self):
        """Initialize the CLI"""
        self.task_manager = TaskManager()
        self.running = True
    
    def print_header(self):
        """Print application header"""
        print("\n" + "="*60)
        print("           📋 TASK MANAGER APP 📋")
        print("="*60)
    
    def print_menu(self):
        """Print main menu options"""
        current_user = self.task_manager.get_current_user()
        user_info = f" (Current: {current_user.name})" if current_user else " (No user selected)"
        
        print(f"\n📋 MAIN MENU{user_info}")
        print("-" * 40)
        print("👤 USER MANAGEMENT:")
        print("  1. Add User")
        print("  2. List Users")
        print("  3. Select User")
        print("\n📝 TASK MANAGEMENT:")
        print("  4. Add Task")
        print("  5. List My Tasks")
        print("  6. Edit Task")
        print("  7. Delete Task")
        print("  8. Mark Task Complete")
        print("  9. Mark Task Pending")
        print("\n🔍 TASK FILTERS:")
        print("  10. View Completed Tasks")
        print("  11. View Pending Tasks")
        print("  12. View High Priority Tasks")
        print("  13. View Overdue Tasks")
        print("  14. Search Tasks")
        print("\n💾 SYSTEM:")
        print("  15. Save Data")
        print("  16. Exit")
        print("-" * 40)
    
    def get_user_input(self, prompt: str) -> str:
        """Get user input with prompt"""
        try:
            return input(f"\n{prompt}: ").strip()
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
    
    def get_date_input(self, prompt: str) -> Optional[date]:
        """Get date input from user"""
        while True:
            date_str = self.get_user_input(prompt + " (YYYY-MM-DD or press Enter to skip)")
            if not date_str:
                return None
            
            try:
                return datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("❌ Invalid date format. Please use YYYY-MM-DD")
    
    def get_priority_input(self) -> Priority:
        """Get priority input from user"""
        while True:
            priority_str = self.get_user_input("Priority (High/Medium/Low)")
            try:
                return Priority(priority_str.title())
            except ValueError:
                print("❌ Invalid priority. Please choose High, Medium, or Low")
    
    def add_user_command(self):
        """Handle add user command"""
        try:
            name = self.get_user_input("Enter user name")
            if not name:
                print("❌ Name cannot be empty")
                return
            
            email = self.get_user_input("Enter email address")
            if not email:
                print("❌ Email cannot be empty")
                return
            
            user_id = self.task_manager.add_user(name, email)
            print(f"✅ User '{name}' added successfully with ID: {user_id[:8]}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def list_users_command(self):
        """Handle list users command"""
        users = self.task_manager.list_users()
        if not users:
            print("📝 No users found")
            return
        
        print("\n👥 USERS:")
        print("-" * 50)
        for user in users:
            current_indicator = " 👤 CURRENT" if user.id == self.task_manager.current_user_id else ""
            print(f"  {user.name} ({user.email}) - ID: {user.id[:8]}{current_indicator}")
    
    def select_user_command(self):
        """Handle select user command"""
        users = self.task_manager.list_users()
        if not users:
            print("❌ No users available. Please add a user first.")
            return
        
        print("\n👥 Available Users:")
        for i, user in enumerate(users, 1):
            print(f"  {i}. {user.name} ({user.email})")
        
        try:
            choice = int(self.get_user_input("Select user number"))
            if 1 <= choice <= len(users):
                selected_user = users[choice - 1]
                self.task_manager.set_current_user(selected_user.id)
                print(f"✅ Selected user: {selected_user.name}")
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def add_task_command(self):
        """Handle add task command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        try:
            title = self.get_user_input("Enter task title")
            if not title:
                print("❌ Title cannot be empty")
                return
            
            description = self.get_user_input("Enter task description (optional)")
            priority = self.get_priority_input()
            due_date = self.get_date_input("Enter due date")
            
            task_id = self.task_manager.add_task(title, description, priority, due_date)
            print(f"✅ Task '{title}' added successfully with ID: {task_id[:8]}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def list_tasks_command(self):
        """Handle list tasks command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_user_tasks()
        if not tasks:
            print("📝 No tasks found")
            return
        
        print(f"\n📋 TASKS FOR {self.task_manager.get_current_user().name.upper()}:")
        print("-" * 80)
        
        # Sort tasks by priority and due date
        sorted_tasks = sorted(tasks, key=lambda t: (
            t.priority.value == "High",  # High priority first
            t.due_date or date.max,      # Tasks with due dates first
            t.due_date or date.max       # Then by due date
        ))
        
        for task in sorted_tasks:
            print(f"  {task}")
            if task.description:
                print(f"     Description: {task.description}")
            print(f"     Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
            print()
    
    def edit_task_command(self):
        """Handle edit task command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_user_tasks()
        if not tasks:
            print("📝 No tasks found")
            return
        
        print("\n📋 Select task to edit:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
        
        try:
            choice = int(self.get_user_input("Select task number"))
            if 1 <= choice <= len(tasks):
                task = tasks[choice - 1]
                
                print(f"\n✏️ Editing task: {task.title}")
                print("Press Enter to keep current value")
                
                new_title = self.get_user_input(f"New title (current: {task.title})")
                new_description = self.get_user_input(f"New description (current: {task.description})")
                
                print("New priority:")
                new_priority = self.get_priority_input()
                
                current_due = task.due_date.strftime('%Y-%m-%d') if task.due_date else "None"
                new_due_date = self.get_date_input(f"New due date (current: {current_due})")
                
                # Update task
                self.task_manager.update_task(
                    task.id,
                    title=new_title if new_title else None,
                    description=new_description if new_description else None,
                    priority=new_priority,
                    due_date=new_due_date
                )
                
                print("✅ Task updated successfully")
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def delete_task_command(self):
        """Handle delete task command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_user_tasks()
        if not tasks:
            print("📝 No tasks found")
            return
        
        print("\n📋 Select task to delete:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
        
        try:
            choice = int(self.get_user_input("Select task number"))
            if 1 <= choice <= len(tasks):
                task = tasks[choice - 1]
                
                confirm = self.get_user_input(f"Are you sure you want to delete '{task.title}'? (yes/no)")
                if confirm.lower() in ['yes', 'y']:
                    if self.task_manager.delete_task(task.id):
                        print("✅ Task deleted successfully")
                    else:
                        print("❌ Failed to delete task")
                else:
                    print("❌ Deletion cancelled")
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def mark_task_complete_command(self):
        """Handle mark task complete command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_tasks_by_status(TaskStatus.PENDING)
        if not tasks:
            print("📝 No pending tasks found")
            return
        
        print("\n📋 Select task to mark complete:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
        
        try:
            choice = int(self.get_user_input("Select task number"))
            if 1 <= choice <= len(tasks):
                task = tasks[choice - 1]
                self.task_manager.update_task(task.id, status=TaskStatus.COMPLETED)
                print(f"✅ Task '{task.title}' marked as complete")
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def mark_task_pending_command(self):
        """Handle mark task pending command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_tasks_by_status(TaskStatus.COMPLETED)
        if not tasks:
            print("📝 No completed tasks found")
            return
        
        print("\n📋 Select task to mark pending:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
        
        try:
            choice = int(self.get_user_input("Select task number"))
            if 1 <= choice <= len(tasks):
                task = tasks[choice - 1]
                self.task_manager.update_task(task.id, status=TaskStatus.PENDING)
                print(f"✅ Task '{task.title}' marked as pending")
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def view_completed_tasks_command(self):
        """Handle view completed tasks command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_tasks_by_status(TaskStatus.COMPLETED)
        if not tasks:
            print("📝 No completed tasks found")
            return
        
        print(f"\n✅ COMPLETED TASKS:")
        print("-" * 60)
        for task in tasks:
            print(f"  {task}")
    
    def view_pending_tasks_command(self):
        """Handle view pending tasks command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_tasks_by_status(TaskStatus.PENDING)
        if not tasks:
            print("📝 No pending tasks found")
            return
        
        print(f"\n⏳ PENDING TASKS:")
        print("-" * 60)
        for task in tasks:
            print(f"  {task}")
    
    def view_high_priority_tasks_command(self):
        """Handle view high priority tasks command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_tasks_by_priority(Priority.HIGH)
        if not tasks:
            print("📝 No high priority tasks found")
            return
        
        print(f"\n🔴 HIGH PRIORITY TASKS:")
        print("-" * 60)
        for task in tasks:
            print(f"  {task}")
    
    def view_overdue_tasks_command(self):
        """Handle view overdue tasks command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        tasks = self.task_manager.get_overdue_tasks()
        if not tasks:
            print("📝 No overdue tasks found")
            return
        
        print(f"\n⚠️ OVERDUE TASKS:")
        print("-" * 60)
        for task in tasks:
            print(f"  {task}")
    
    def search_tasks_command(self):
        """Handle search tasks command"""
        if not self.task_manager.current_user_id:
            print("❌ Please select a user first")
            return
        
        query = self.get_user_input("Enter search query")
        if not query:
            print("❌ Search query cannot be empty")
            return
        
        tasks = self.task_manager.search_tasks(query)
        if not tasks:
            print(f"📝 No tasks found matching '{query}'")
            return
        
        print(f"\n🔍 SEARCH RESULTS FOR '{query}':")
        print("-" * 60)
        for task in tasks:
            print(f"  {task}")
    
    def save_data_command(self):
        """Handle save data command"""
        self.task_manager.save_data()
    
    def run(self):
        """Main application loop"""
        self.print_header()
        
        while self.running:
            try:
                self.print_menu()
                choice = self.get_user_input("Enter your choice (1-16)")
                
                if choice == '1':
                    self.add_user_command()
                elif choice == '2':
                    self.list_users_command()
                elif choice == '3':
                    self.select_user_command()
                elif choice == '4':
                    self.add_task_command()
                elif choice == '5':
                    self.list_tasks_command()
                elif choice == '6':
                    self.edit_task_command()
                elif choice == '7':
                    self.delete_task_command()
                elif choice == '8':
                    self.mark_task_complete_command()
                elif choice == '9':
                    self.mark_task_pending_command()
                elif choice == '10':
                    self.view_completed_tasks_command()
                elif choice == '11':
                    self.view_pending_tasks_command()
                elif choice == '12':
                    self.view_high_priority_tasks_command()
                elif choice == '13':
                    self.view_overdue_tasks_command()
                elif choice == '14':
                    self.search_tasks_command()
                elif choice == '15':
                    self.save_data_command()
                elif choice == '16':
                    print("\n👋 Goodbye!")
                    self.running = False
                else:
                    print("❌ Invalid choice. Please enter a number between 1-16")
                
                if self.running:
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                input("\nPress Enter to continue...")


def main():
    """Main entry point of the application"""
    try:
        cli = TaskManagerCLI()
        cli.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
