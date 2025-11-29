from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

from agents.tool import function_tool

@dataclass
class Task:
    id: int
    description: str
    created_at: str
    due: Optional[str] = None
    status: str = "pending"
    priority: str = "normal"

@dataclass
class TaskList:
    tasks: List[Task] = field(default_factory=list)
    
    def add_task(
        self,
        description: str,
        due: Optional[str] = None,
        priority: str = "normal",
    ) -> Task:
        now_iso = datetime.utcnow().isoformat()
        new_task = Task(
            id=len(self.tasks) + 1,
            description=description,
            created_at=now_iso,
            due=due,
            priority=priority,
        )
        self.tasks.append(new_task)
        return new_task

    def list_tasks(self):
        return self.tasks

    def delete_task(self, id: int):
        # Simple deletion by filtering, assuming IDs might not be contiguous or handling index
        # For simplicity, let's just remove by ID if found
        for i, task in enumerate(self.tasks):
            if task.id == id:
                self.tasks.pop(i)
                return True
        return False

# Instantiate the global task list
task_list = TaskList()

@function_tool
def add_task_tool(description: str, due: Optional[str] = None, priority: str = "normal") -> str:
    """
    Add a new task to the LifeOS task list.

    Args:
        description: What the task is about.
        due: Optional due date/time in natural language (e.g. 'tomorrow 5pm').
        priority: Optional priority level (e.g. 'high', 'normal', 'low').
    """   
    new_task = task_list.add_task(description, due, priority)
    message = ['Task added:',
    f'ID: {new_task.id}',
    f'Description: {new_task.description}',    
    f'Priority: {new_task.priority}',
    ]
    if new_task.due:
        message.append(f'Due: {new_task.due}')

    return '\n'.join(message)   

@function_tool
def list_tasks_tool() -> str:
    """
    List all tasks in the LifeOS task list.

    """
    tasks = task_list.list_tasks()
    if not tasks:
        return 'No tasks added yet.'

    return '\n'.join([f'ID: {task.id}\nDescription: {task.description}\nPriority: {task.priority}\nDue: {task.due}' for task in tasks])

@function_tool
def delete_task_tool(id: int) -> str:
    """
    Delete a task from the LifeOS task list.

    Args:
        id: The ID of the task to delete.
    """
    success = task_list.delete_task(id)
    if success:
        return f'Task {id} deleted.'
    else:
        return f'Task {id} not found.'

