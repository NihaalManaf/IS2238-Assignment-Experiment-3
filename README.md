# Task Manager App

A simple, production-ready command-line task management system for two users built with Python 3.11 and the standard library only.

## Features

- **User Management**: Support for two users (User1 and User2)
- **Task Operations**: Add, edit, delete, and mark tasks as complete/incomplete
- **Task Properties**:
  - Title and description
  - Due date (YYYY-MM-DD format)
  - Priority levels (Low, Medium, High)
  - Completion status
- **Data Persistence**: Tasks are automatically saved to `tasks.json`
- **User-Specific Views**: Each user sees only their own tasks
- **Statistics**: View task counts (total, completed, pending)
- **Robust Error Handling**: Comprehensive input validation and error messages

## Installation & Usage

### Prerequisites

- Python 3.11 or higher
- No external dependencies required (uses only standard library)

### Running the Application

1. **Start the Task Manager:**

   ```bash
   python3 task_manager.py
   ```

2. **Select a User:**

   - Choose between User1 and User2
   - View task statistics for each user

3. **Main Menu Options:**
   - **View Tasks**: Display all tasks for the current user
   - **Add Task**: Create a new task with title, description, due date, and priority
   - **Edit Task**: Modify existing task properties
   - **Delete Task**: Remove a task (with confirmation)
   - **Mark Task Complete/Incomplete**: Toggle task completion status
   - **Switch User**: Change to the other user
   - **Exit**: Close the application

### Task Management

#### Adding a Task

1. Select "Add Task" from the main menu
2. Enter task title (required)
3. Enter task description
4. Enter due date in YYYY-MM-DD format
5. Select priority level (1=Low, 2=Medium, 3=High)

#### Editing a Task

1. Select "Edit Task" from the main menu
2. Enter the task ID to edit
3. Enter new values (press Enter to keep current values)
4. Confirm changes

#### Task Properties

- **ID**: Unique identifier (auto-generated)
- **Title**: Task name (required, cannot be empty)
- **Description**: Detailed task description
- **Due Date**: Target completion date (YYYY-MM-DD format)
- **Priority**: Low (🟢), Medium (🟡), or High (🔴)
- **Status**: Completed (✓) or Pending (○)
- **User**: Assigned user (User1 or User2)
- **Timestamps**: Created and last updated dates

## Data Storage

Tasks are automatically saved to `tasks.json` in the same directory as the application. The file contains:

- All task data in JSON format
- Next available task ID
- Automatic backup on every operation

## Error Handling

The application includes comprehensive error handling for:

- Invalid date formats
- Empty task titles
- Invalid user selections
- Non-existent task IDs
- File I/O errors
- JSON parsing errors

## Testing

Run the included test suite to verify functionality:

```bash
python3 test_task_manager.py
```

The test suite covers:

- Task CRUD operations
- User management
- Data persistence
- Error handling scenarios
- Input validation

## Code Structure

### Core Classes

- **`Task`**: Data model representing a single task
- **`Priority`**: Enum for task priority levels
- **`TaskManager`**: Core business logic and data management
- **`TaskManagerCLI`**: Command-line interface and user interaction

### Key Features

- **Type Hints**: Full type annotation for better code maintainability
- **Dataclasses**: Clean data modeling with `@dataclass`
- **Enum Usage**: Type-safe priority levels
- **Error Handling**: Comprehensive exception handling
- **Data Validation**: Input sanitization and validation
- **Persistence**: JSON-based data storage
- **User Experience**: Intuitive menu system with clear prompts

## Example Usage Session

```
============================================================
           TASK MANAGER APP
============================================================

Select User:
1. User1 (Tasks: 0, Completed: 0, Pending: 0)
2. User2 (Tasks: 0, Completed: 0, Pending: 0)
0. Exit
Enter your choice: 1

Welcome, User1!

==================================================
TASK MANAGER - User1
==================================================
Tasks: 0 | Completed: 0 | Pending: 0

1. View Tasks
2. Add Task
3. Edit Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Switch User
0. Exit
Enter your choice: 2

==================================================
ADD NEW TASK
==================================================
Enter task title: Complete project documentation
Enter task description: Write comprehensive documentation for the new API
Enter due date (YYYY-MM-DD): 2024-12-31

Priority levels:
1. Low
2. Medium
3. High
Select priority (1-3): 3

Task added successfully! Task ID: 1
```

## Production Readiness

This application is production-ready with:

- ✅ Comprehensive error handling
- ✅ Input validation and sanitization
- ✅ Data persistence and recovery
- ✅ Type safety and documentation
- ✅ Clean, maintainable code structure
- ✅ User-friendly interface
- ✅ Robust testing coverage
- ✅ Professional coding standards
