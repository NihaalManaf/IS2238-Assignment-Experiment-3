# Task Manager App - UML Class Diagram & Data Flow Documentation

## UML Class Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                TASK MANAGER APP                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                    ENUMS                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Priority                    TaskStatus                                         │
├─────────────────────────────┬───────────────────────────────────────────────────┤
│ + HIGH: str = "High"        │ + PENDING: str = "Pending"                       │
│ + MEDIUM: str = "Medium"    │ + COMPLETED: str = "Completed"                   │
│ + LOW: str = "Low"          │                                                   │
└─────────────────────────────┴───────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                    USER                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ - id: str                                                                      │
│ - name: str                                                                    │
│ - email: str                                                                   │
│ - created_at: datetime                                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│ + __init__(name: str, email: str)                                             │
│ + to_dict() -> Dict                                                            │
│ + from_dict(data: Dict) -> User                                                │
│ + __str__() -> str                                                             │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                    TASK                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ - id: str                                                                      │
│ - title: str                                                                   │
│ - description: str                                                             │
│ - priority: Priority                                                           │
│ - due_date: Optional[date]                                                     │
│ - status: TaskStatus                                                           │
│ - created_at: datetime                                                         │
│ - updated_at: datetime                                                         │
│ - user_id: str                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ + __init__(title: str, description: str, priority: Priority,                   │
│            due_date: Optional[date], user_id: str)                             │
│ + to_dict() -> Dict                                                            │
│ + from_dict(data: Dict) -> Task                                                │
│ + update(title: str, description: str, priority: Priority,                     │
│          due_date: Optional[date], status: TaskStatus)                         │
│ + mark_complete()                                                              │
│ + mark_pending()                                                               │
│ + is_overdue() -> bool                                                         │
│ + __str__() -> str                                                             │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                TASK MANAGER                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│ - data_file: str                                                               │
│ - users: Dict[str, User]                                                       │
│ - tasks: Dict[str, Task]                                                       │
│ - current_user_id: Optional[str]                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ + __init__(data_file: str)                                                     │
│ + load_data()                                                                  │
│ + save_data()                                                                  │
│ + add_user(name: str, email: str) -> str                                       │
│ + get_user(user_id: str) -> Optional[User]                                     │
│ + list_users() -> List[User]                                                   │
│ + set_current_user(user_id: str)                                               │
│ + get_current_user() -> Optional[User]                                          │
│ + add_task(title: str, description: str, priority: Priority,                   │
│            due_date: Optional[date]) -> str                                     │
│ + get_task(task_id: str) -> Optional[Task]                                     │
│ + update_task(task_id: str, title: str, description: str,                      │
│               priority: Priority, due_date: Optional[date],                     │
│               status: TaskStatus) -> bool                                       │
│ + delete_task(task_id: str) -> bool                                            │
│ + get_user_tasks(user_id: str) -> List[Task]                                    │
│ + get_tasks_by_status(status: TaskStatus, user_id: str) -> List[Task]          │
│ + get_tasks_by_priority(priority: Priority, user_id: str) -> List[Task]         │
│ + get_overdue_tasks(user_id: str) -> List[Task]                                 │
│ + search_tasks(query: str, user_id: str) -> List[Task]                         │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                TASK MANAGER CLI                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│ - task_manager: TaskManager                                                    │
│ - running: bool                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│ + __init__()                                                                    │
│ + print_header()                                                                │
│ + print_menu()                                                                  │
│ + get_user_input(prompt: str) -> str                                            │
│ + get_date_input(prompt: str) -> Optional[date]                                 │
│ + get_priority_input() -> Priority                                              │
│ + add_user_command()                                                            │
│ + list_users_command()                                                          │
│ + select_user_command()                                                         │
│ + add_task_command()                                                            │
│ + list_tasks_command()                                                          │
│ + edit_task_command()                                                           │
│ + delete_task_command()                                                         │
│ + mark_task_complete_command()                                                  │
│ + mark_task_pending_command()                                                   │
│ + view_completed_tasks_command()                                                │
│ + view_pending_tasks_command()                                                  │
│ + view_high_priority_tasks_command()                                            │
│ + view_overdue_tasks_command()                                                  │
│ + search_tasks_command()                                                        │
│ + save_data_command()                                                           │
│ + run()                                                                         │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              RELATIONSHIPS                                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│ TaskManagerCLI ──► TaskManager (composition)                                   │
│ TaskManager ──► User (aggregation)                                             │
│ TaskManager ──► Task (aggregation)                                             │
│ Task ──► Priority (enumeration)                                                │
│ Task ──► TaskStatus (enumeration)                                              │
│ Task ──► User (association via user_id)                                        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Data Flow Description

### 1. Application Initialization Flow

```
Start Application
    ↓
Initialize TaskManagerCLI
    ↓
Initialize TaskManager
    ↓
Load Data from JSON File
    ↓
Display Welcome Header
    ↓
Enter Main Menu Loop
```

### 2. User Management Flow

```
User Management Operations:
    ↓
Add User: name, email → Validate → Create User → Save to JSON
    ↓
List Users: Load from Memory → Display All Users
    ↓
Select User: Display Users → User Choice → Set Current User
```

### 3. Task Management Flow

```
Task Management Operations:
    ↓
Add Task: title, description, priority, due_date → Validate → Create Task → Save to JSON
    ↓
List Tasks: Filter by Current User → Sort by Priority/Due Date → Display Tasks
    ↓
Edit Task: Select Task → Update Fields → Save Changes → Update JSON
    ↓
Delete Task: Select Task → Confirm → Remove from Memory → Update JSON
    ↓
Mark Complete/Pending: Select Task → Update Status → Save Changes
```

### 4. Data Persistence Flow

```
Data Operations:
    ↓
Load Data: Read JSON File → Parse JSON → Create Objects → Store in Memory
    ↓
Save Data: Convert Objects to Dict → Serialize to JSON → Write to File
    ↓
Auto-save: Triggered after each modification operation
```

### 5. Task Filtering and Search Flow

```
Filter Operations:
    ↓
By Status: Filter Tasks by TaskStatus → Display Results
    ↓
By Priority: Filter Tasks by Priority → Display Results
    ↓
Overdue Tasks: Check due_date < today() → Display Overdue Tasks
    ↓
Search Tasks: Query title/description → Case-insensitive Match → Display Results
```

## System Architecture

### Core Components:

1. **TaskManager**: Central business logic layer

   - Manages users and tasks
   - Handles data persistence
   - Provides CRUD operations
   - Implements filtering and search

2. **TaskManagerCLI**: User interface layer

   - Handles user input/output
   - Validates user input
   - Orchestrates business operations
   - Provides menu-driven interface

3. **Data Models**:
   - **User**: Represents system users
   - **Task**: Represents individual tasks
   - **Enums**: Priority and TaskStatus for type safety

### Data Storage:

- **Format**: JSON file (`task_manager_data.json`)
- **Structure**:
  ```json
  {
    "users": [
      { "id": "...", "name": "...", "email": "...", "created_at": "..." }
    ],
    "tasks": [
      {
        "id": "...",
        "title": "...",
        "description": "...",
        "priority": "...",
        "due_date": "...",
        "status": "...",
        "created_at": "...",
        "updated_at": "...",
        "user_id": "..."
      }
    ]
  }
  ```

### Error Handling:

- Input validation at CLI level
- Business logic validation at TaskManager level
- File I/O error handling for data persistence
- Graceful handling of user interruptions (Ctrl+C)

### Key Features Implemented:

✅ Add, edit, delete tasks
✅ Mark tasks as complete/incomplete
✅ Assign due dates (YYYY-MM-DD format)
✅ Set task priorities (High, Medium, Low)
✅ View tasks per user
✅ Filter tasks by status, priority, overdue
✅ Search tasks by title/description
✅ Data persistence with JSON storage
✅ User management (add, list, select users)
✅ Comprehensive error handling
✅ User-friendly command-line interface
