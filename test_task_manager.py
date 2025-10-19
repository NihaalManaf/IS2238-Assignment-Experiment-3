#!/usr/bin/env python3
"""
Test script for Task Manager App to verify core functionality.
"""

import os
import tempfile
from task_manager import TaskManager, Priority, Task


def test_task_manager():
    """Test the core TaskManager functionality."""
    print("Testing Task Manager Core Functionality...")
    
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        # Initialize task manager
        tm = TaskManager(temp_file)
        
        # Test adding tasks
        print("1. Testing task addition...")
        task1 = tm.add_task("Test Task 1", "Description 1", "2024-12-31", Priority.HIGH, "User1")
        task2 = tm.add_task("Test Task 2", "Description 2", "2024-12-25", Priority.MEDIUM, "User2")
        
        assert task1.id == 1
        assert task1.title == "Test Task 1"
        assert task1.priority == Priority.HIGH
        assert task1.user == "User1"
        print("✓ Task addition works correctly")
        
        # Test getting tasks by user
        print("2. Testing task retrieval by user...")
        user1_tasks = tm.get_tasks_by_user("User1")
        user2_tasks = tm.get_tasks_by_user("User2")
        
        assert len(user1_tasks) == 1
        assert len(user2_tasks) == 1
        assert user1_tasks[0].title == "Test Task 1"
        assert user2_tasks[0].title == "Test Task 2"
        print("✓ Task retrieval by user works correctly")
        
        # Test editing tasks
        print("3. Testing task editing...")
        tm.edit_task(task1.id, title="Updated Task 1", priority=Priority.LOW)
        updated_task = tm.get_task_by_id(task1.id)
        
        assert updated_task.title == "Updated Task 1"
        assert updated_task.priority == Priority.LOW
        print("✓ Task editing works correctly")
        
        # Test marking tasks complete
        print("4. Testing task completion...")
        tm.mark_task_complete(task1.id, True)
        completed_task = tm.get_task_by_id(task1.id)
        
        assert completed_task.completed == True
        print("✓ Task completion works correctly")
        
        # Test task statistics
        print("5. Testing task statistics...")
        stats = tm.get_task_statistics("User1")
        
        assert stats['total'] == 1
        assert stats['completed'] == 1
        assert stats['pending'] == 0
        print("✓ Task statistics work correctly")
        
        # Test deleting tasks
        print("6. Testing task deletion...")
        success = tm.delete_task(task2.id)
        
        assert success == True
        assert tm.get_task_by_id(task2.id) is None
        print("✓ Task deletion works correctly")
        
        # Test data persistence
        print("7. Testing data persistence...")
        tm2 = TaskManager(temp_file)
        remaining_tasks = tm2.get_tasks_by_user("User1")
        
        assert len(remaining_tasks) == 1
        assert remaining_tasks[0].title == "Updated Task 1"
        print("✓ Data persistence works correctly")
        
        print("\n🎉 All tests passed! Task Manager is working correctly.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        raise
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def test_error_handling():
    """Test error handling scenarios."""
    print("\nTesting Error Handling...")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        tm = TaskManager(temp_file)
        
        # Test invalid date format
        print("1. Testing invalid date format...")
        try:
            tm.add_task("Test", "Desc", "invalid-date", Priority.LOW, "User1")
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "Invalid date format" in str(e)
            print("✓ Invalid date format handled correctly")
        
        # Test empty title
        print("2. Testing empty title...")
        try:
            tm.add_task("", "Desc", "2024-12-31", Priority.LOW, "User1")
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "Task title cannot be empty" in str(e)
            print("✓ Empty title handled correctly")
        
        # Test invalid user
        print("3. Testing invalid user...")
        try:
            tm.add_task("Test", "Desc", "2024-12-31", Priority.LOW, "InvalidUser")
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "Invalid user" in str(e)
            print("✓ Invalid user handled correctly")
        
        # Test editing non-existent task
        print("4. Testing editing non-existent task...")
        try:
            tm.edit_task(999, title="New Title")
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "Task with ID 999 not found" in str(e)
            print("✓ Non-existent task editing handled correctly")
        
        print("✓ All error handling tests passed!")
        
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)


if __name__ == "__main__":
    test_task_manager()
    test_error_handling()
    print("\n🚀 Task Manager App is ready for production use!")
