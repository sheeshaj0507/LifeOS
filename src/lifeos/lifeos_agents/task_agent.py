from agents.agent import Agent

from typing import Dict, Any
from lifeos.tools.tasks import add_task, list_tasks


def build_task_agent() -> Agent:
    """
    Create the Task Manager Agent for LifeOS.
    """
    tools = [
        add_task,
        list_tasks,
    ]

    agent = Agent(
        name="Task Manager Agent",
        instructions=(
            "You are my personal Task Manager for LifeOS. "
            "You help me create, track, and list tasks. "
            "When I ask to add or create a task, call the add_task tool. "
            "When I ask to see my tasks, call the list_tasks tool. "
            "When I ask to delete a task, call the delete_task tool. "
            "Be concise and clear in your responses."
        ),
        tools=tools,
        model="gpt-4.1-mini",
    )

    return agent
