from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

import dateparser
from agents.tool import function_tool
from sqlmodel import select, Session

from lifeos.db import engine
from lifeos.models import Task
from sqlmodel import Field, select

def _parse_due_date(due_text: Optional[str]) -> Optional[datetime]:
    """
    Parse natural language date/time (e.g. 'tomorrow 5pm') into a datetime.
    Returns None if parsing fails or due_text is None.
    """
    if not due_text:
        return None

    parsed = dateparser.parse(due_text)
    return parsed


def _format_datetime(dt: Optional[datetime]) -> str:
    """
    Format a datetime for display, or return 'None' if not set.
    """
    if dt is None:
        return "None"
    return dt.strftime("%Y-%m-%d %H:%M UTC")

@function_tool
def add_task(
        description: str,
        due: Optional[str] = None,
        priority: str = "normal",
    ) -> str:
    """
    Add a new task to the LifeOS task list and store it in the database.

    Args:
        description: What the task is about.
        due: Optional due date/time in natural language (e.g. 'tomorrow 5pm').
    """
    due_dt = _parse_due_date(due)
    with Session(engine) as session:
        new_task = Task(
            description=description,
            due=due_dt,
            priority=priority,
        )
        session.add(new_task)
        session.commit()
        session.refresh(new_task)

        lines = [
            f"Task added:",
            f"ID: {new_task.id}",
            f"Description: {new_task.description}",
            f"Priority: {new_task.priority}",
        ]
        if new_task.due:
            lines.append(f"Due: {new_task.due}")

        return "\n".join(lines)

@function_tool
def list_tasks(status: Optional[str] = None) -> str:
    """
    List all tasks in the LifeOS task list.

    Args:
        status: Optional filter (e.g. 'pending', 'done'). If None, show all tasks.
    
    """
    with Session(engine) as session:
        if status:
            tasks_list = session.exec(select(Task).where(Task.status == status)).all()
        else:
            tasks_list = session.exec(select(Task)).all()

        if not tasks_list:
            return "No tasks found."

        lines = []
        for task in tasks_list:
            lines.append(f"ID: {task.id}")
            lines.append(f"Description: {task.description}")
            lines.append(f"Priority: {task.priority}")
            if task.due:
                lines.append(f"Due: {task.due}")
            lines.append("---")

        return "\n".join(lines)    


