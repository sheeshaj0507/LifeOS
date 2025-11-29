from agents.agent import Agent

from typing import Dict, Any
from lifeos.tools.tasks import add_task_tool, list_tasks_tool, delete_task_tool


def build_task_agent() -> Agent:
    """
    Create the Task Manager Agent for LifeOS.
    """
    tools = [
        add_task_tool,
        list_tasks_tool,
        delete_task_tool
    ]

    agent = Agent(
        name="Task Manager Agent",
        instructions=(
            "You are my personal Task Manager for LifeOS. "
            "You help me create, track, and list tasks. "
            "When I ask to add or create a task, call the add_task tool. "
            "When I ask to see my tasks, call the list_tasks tool. "
            "Be concise and clear in your responses."
        ),
        tools=tools,
        model="gpt-4.1-mini",
    )

    return agent
