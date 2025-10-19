# Task Manager App

A comprehensive command-line task management system designed for two users, built with Python 3.11+ using only the standard library.

## 🎯 Features

### User Management

- ✅ Add users with name and email validation
- ✅ List all users in the system
- ✅ Select active user for task operations
- ✅ Email uniqueness validation

### Task Management

- ✅ Add tasks with title, description, priority, and due date
- ✅ Edit existing tasks (all fields can be updated)
- ✅ Delete tasks with confirmation
- ✅ Mark tasks as complete or pending

### Task Filtering & Search

- ✅ View tasks by completion status (completed/pending)
- ✅ Filter tasks by priority (High/Medium/Low)
- ✅ Find overdue tasks automatically
- ✅ Search tasks by title or description

### Data Persistence

- ✅ Automatic saving after each operation
- ✅ JSON file storage for data persistence
- ✅ Data loading on application startup
- ✅ Error handling for file operations

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- No external dependencies required

### Installation

1. Clone or download the `task_manager.py` file
2. Make it executable (optional):
   ```bash
   chmod +x task_manager.py
   ```

### Running the Application

```bash
python3 task_manager.py
```

## 📋 Usage Guide

### 1. User Management

Start by adding users to the system:

1. **Add User**: Enter user name and email address
2. **List Users**: View all users in the system
3. **Select User**: Choose the active user for task operations

### 2. Task Operations

Once a user is selected, you can manage tasks:

1. **Add Task**: Create new tasks with:

   - Title (required)
   - Description (optional)
   - Priority: High 🔴, Medium 🟡, Low 🟢
   - Due date: YYYY-MM-DD format (optional)

2. **List Tasks**: View all tasks for the current user
3. **Edit Task**: Modify existing task details
4. **Delete Task**: Remove tasks with confirmation
5. **Mark Complete/Pending**: Change task status

### 3. Task Filtering

Filter and search tasks efficiently:

- **View Completed Tasks**: See finished tasks
- **View Pending Tasks**: See active tasks
- **View High Priority Tasks**: Focus on urgent items
- **View Overdue Tasks**: Find tasks past due date
- **Search Tasks**: Find tasks by title or description

## 🏗️ Architecture

### UML Class Diagram

The application follows a clean architecture with the following components:

```
TaskManagerCLI ──► TaskManager ──► User/Task Models
     │                    │              │
     │                    │              │
User Interface    Business Logic    Data Models
```

### Core Classes

- **`TaskManagerCLI`**: Command-line interface and user interaction
- **`TaskManager`**: Core business logic and data management
- **`User`**: User model with validation
- **`Task`**: Task model with status and priority management
- **`Priority`**: Enum for task priorities (High, Medium, Low)
- **`TaskStatus`**: Enum for task status (Pending, Completed)

### Data Flow

1. **Initialization**: Load existing data from JSON file
2. **User Operations**: Add, list, and select users
3. **Task Operations**: CRUD operations on tasks
4. **Data Persistence**: Automatic saving after each operation
5. **Filtering**: Query tasks by various criteria

## 📁 Data Storage

The application stores data in a JSON file (`task_manager_data.json`) with the following structure:

```json
{
  "users": [
    {
      "id": "unique-user-id",
      "name": "User Name",
      "email": "user@example.com",
      "created_at": "2024-01-01T00:00:00"
    }
  ],
  "tasks": [
    {
      "id": "unique-task-id",
      "title": "Task Title",
      "description": "Task Description",
      "priority": "High",
      "due_date": "2024-01-15",
      "status": "Pending",
      "created_at": "2024-01-01T00:00:00",
      "updated_at": "2024-01-01T00:00:00",
      "user_id": "user-id"
    }
  ]
}
```

## 🧪 Testing

Run the test suite to verify functionality:

```bash
python3 test_task_manager.py
```

The test suite validates:

- User management operations
- Task CRUD operations
- Multi-user support
- Data filtering and search
- Data persistence
- Error handling

## 🔧 Error Handling

The application includes comprehensive error handling:

- **Input Validation**: Email format, date format, priority levels
- **Business Logic Validation**: User existence, task ownership
- **File I/O Errors**: Graceful handling of data file issues
- **User Interruption**: Clean exit on Ctrl+C
- **Data Integrity**: Validation of data consistency

## 📊 Example Session

```
============================================================
           📋 TASK MANAGER APP 📋
============================================================

📋 MAIN MENU (No user selected)
----------------------------------------
👤 USER MANAGEMENT:
  1. Add User
  2. List Users
  3. Select User

📝 TASK MANAGEMENT:
  4. Add Task
  5. List My Tasks
  6. Edit Task
  7. Delete Task
  8. Mark Task Complete
  9. Mark Task Pending

🔍 TASK FILTERS:
  10. View Completed Tasks
  11. View Pending Tasks
  12. View High Priority Tasks
  13. View Overdue Tasks
  14. Search Tasks

💾 SYSTEM:
  15. Save Data
  16. Exit
----------------------------------------

Enter your choice (1-16): 1
Enter user name: Alice Johnson
Enter email address: alice@example.com
✅ User 'Alice Johnson' added successfully with ID: 322aa31e
```

## 🎨 Visual Indicators

The application uses clear visual indicators:

- **Task Status**: ✓ (completed), ○ (pending)
- **Priority**: 🔴 (High), 🟡 (Medium), 🟢 (Low)
- **Overdue**: ⚠️ OVERDUE indicator
- **Current User**: 👤 CURRENT indicator
- **Success/Error**: ✅/❌ status messages

## 🔒 Data Security

- Email uniqueness validation prevents duplicate accounts
- User-specific task isolation ensures privacy
- Data validation prevents malformed entries
- Graceful error handling prevents data corruption

## 🚀 Production Ready

This application is production-ready with:

- ✅ Comprehensive error handling
- ✅ Input validation and sanitization
- ✅ Data persistence and recovery
- ✅ Clean, maintainable code structure
- ✅ Extensive documentation
- ✅ Test coverage
- ✅ User-friendly interface
- ✅ Multi-user support
- ✅ No external dependencies

## 📝 License

This project is provided as-is for educational and demonstration purposes.

## 🤝 Contributing

This is a demonstration project. For production use, consider:

- Adding database support
- Implementing user authentication
- Adding task categories/tags
- Implementing task sharing between users
- Adding task templates
- Implementing task dependencies
