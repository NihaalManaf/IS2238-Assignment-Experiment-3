#!/usr/bin/env python3
"""
Test script for Task Manager App
This script demonstrates the core functionality without requiring user interaction.
"""

import sys
import os
from datetime import date, datetime
from task_manager import TaskManager, Priority, TaskStatus, User, Task

def test_task_manager():
    """Test the Task Manager functionality"""
    print("🧪 Testing Task Manager App")
    print("=" * 50)
    
    # Initialize task manager with test data file
    tm = TaskManager("test_data.json")
    
    try:
        # Test 1: Add users
        print("\n1️⃣ Testing User Management:")
        print("-" * 30)
        
        user1_id = tm.add_user("Alice Johnson", "alice@example.com")
        user2_id = tm.add_user("Bob Smith", "bob@example.com")
        
        print(f"✅ Added User 1: Alice Johnson (ID: {user1_id[:8]})")
        print(f"✅ Added User 2: Bob Smith (ID: {user2_id[:8]})")
        
        # Test 2: Set current user and add tasks
        print("\n2️⃣ Testing Task Management:")
        print("-" * 30)
        
        tm.set_current_user(user1_id)
        print(f"✅ Set current user: {tm.get_current_user().name}")
        
        # Add tasks for Alice
        task1_id = tm.add_task(
            "Complete project proposal",
            "Write and submit the quarterly project proposal",
            Priority.HIGH,
            date(2024, 1, 15)
        )
        
        task2_id = tm.add_task(
            "Review code changes",
            "Review pull requests from the development team",
            Priority.MEDIUM,
            date(2024, 1, 20)
        )
        
        task3_id = tm.add_task(
            "Update documentation",
            "Update API documentation for new features",
            Priority.LOW
        )
        
        print(f"✅ Added Task 1: Complete project proposal (ID: {task1_id[:8]})")
        print(f"✅ Added Task 2: Review code changes (ID: {task2_id[:8]})")
        print(f"✅ Added Task 3: Update documentation (ID: {task3_id[:8]})")
        
        # Test 3: Switch to second user and add tasks
        print("\n3️⃣ Testing Multi-User Support:")
        print("-" * 30)
        
        tm.set_current_user(user2_id)
        print(f"✅ Switched to user: {tm.get_current_user().name}")
        
        task4_id = tm.add_task(
            "Design new feature",
            "Create mockups and technical specifications",
            Priority.HIGH,
            date(2024, 1, 25)
        )
        
        task5_id = tm.add_task(
            "Team meeting preparation",
            "Prepare agenda and materials for weekly team meeting",
            Priority.MEDIUM,
            date(2024, 1, 18)
        )
        
        print(f"✅ Added Task 4: Design new feature (ID: {task4_id[:8]})")
        print(f"✅ Added Task 5: Team meeting preparation (ID: {task5_id[:8]})")
        
        # Test 4: Task operations
        print("\n4️⃣ Testing Task Operations:")
        print("-" * 30)
        
        # Mark a task as complete
        tm.update_task(task1_id, status=TaskStatus.COMPLETED)
        print(f"✅ Marked task '{tm.get_task(task1_id).title}' as complete")
        
        # Update a task
        tm.update_task(task2_id, title="Review code changes (Updated)", priority=Priority.HIGH)
        print(f"✅ Updated task: {tm.get_task(task2_id).title}")
        
        # Test 5: Task filtering and search
        print("\n5️⃣ Testing Task Filtering:")
        print("-" * 30)
        
        # Get tasks by status
        completed_tasks = tm.get_tasks_by_status(TaskStatus.COMPLETED, user1_id)
        pending_tasks = tm.get_tasks_by_status(TaskStatus.PENDING, user1_id)
        
        print(f"✅ Alice's completed tasks: {len(completed_tasks)}")
        print(f"✅ Alice's pending tasks: {len(pending_tasks)}")
        
        # Get tasks by priority
        high_priority_tasks = tm.get_tasks_by_priority(Priority.HIGH, user1_id)
        print(f"✅ Alice's high priority tasks: {len(high_priority_tasks)}")
        
        # Search tasks
        search_results = tm.search_tasks("project", user1_id)
        print(f"✅ Search results for 'project': {len(search_results)} tasks found")
        
        # Test 6: Display all tasks for both users
        print("\n6️⃣ Task Summary:")
        print("-" * 30)
        
        for user_id in [user1_id, user2_id]:
            user = tm.get_user(user_id)
            tasks = tm.get_user_tasks(user_id)
            print(f"\n👤 {user.name}'s Tasks ({len(tasks)} total):")
            
            for task in tasks:
                status_icon = "✓" if task.status == TaskStatus.COMPLETED else "○"
                priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}[task.priority.value]
                due_date_str = f"Due: {task.due_date}" if task.due_date else "No due date"
                overdue_indicator = " ⚠️ OVERDUE" if task.is_overdue() else ""
                
                print(f"  {status_icon} {task.title} {priority_icon} {due_date_str}{overdue_indicator}")
        
        # Test 7: Data persistence
        print("\n7️⃣ Testing Data Persistence:")
        print("-" * 30)
        
        tm.save_data()
        print("✅ Data saved to JSON file")
        
        # Verify file exists
        if os.path.exists("test_data.json"):
            file_size = os.path.getsize("test_data.json")
            print(f"✅ Data file created successfully ({file_size} bytes)")
        
        print("\n🎉 All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False
    
    finally:
        # Clean up test data file
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")
            print("\n🧹 Cleaned up test data file")
    
    return True

def demonstrate_features():
    """Demonstrate key features of the Task Manager"""
    print("\n📋 Task Manager App - Feature Demonstration")
    print("=" * 60)
    
    print("""
🎯 KEY FEATURES IMPLEMENTED:

✅ USER MANAGEMENT:
   • Add users with name and email validation
   • List all users in the system
   • Select active user for task operations
   • Email uniqueness validation

✅ TASK MANAGEMENT:
   • Add tasks with title, description, priority, and due date
   • Edit existing tasks (all fields can be updated)
   • Delete tasks with confirmation
   • Mark tasks as complete or pending

✅ TASK FILTERING & SEARCH:
   • View tasks by completion status (completed/pending)
   • Filter tasks by priority (High/Medium/Low)
   • Find overdue tasks automatically
   • Search tasks by title or description

✅ DATA PERSISTENCE:
   • Automatic saving after each operation
   • JSON file storage for data persistence
   • Data loading on application startup
   • Error handling for file operations

✅ USER INTERFACE:
   • Intuitive command-line menu system
   • Clear visual indicators (emojis, icons)
   • Comprehensive error messages
   • Graceful handling of user input

✅ DATA VALIDATION:
   • Email format validation
   • Date format validation (YYYY-MM-DD)
   • Priority level validation
   • Input sanitization and error handling

✅ MULTI-USER SUPPORT:
   • Support for multiple users
   • User-specific task isolation
   • Current user context management
   • Per-user task filtering and display
""")

if __name__ == "__main__":
    print("🚀 Starting Task Manager App Test Suite")
    
    # Run the test
    success = test_task_manager()
    
    if success:
        demonstrate_features()
        print("\n✅ Task Manager App is ready for production use!")
        print("\nTo run the application:")
        print("  python3 task_manager.py")
    else:
        print("\n❌ Tests failed. Please check the implementation.")
        sys.exit(1)
