# LifeOS

LifeOS is a personal AI Operating System designed to help you manage your daily tasks and activities using intelligent agents.

## Features

- **Task Manager Agent**: A dedicated agent to help you create, track, and manage your tasks using natural language.
    - **Add Tasks**: Create tasks with descriptions, due dates, and priority levels.
    - **List Tasks**: View all your pending tasks.
    - **Delete Tasks**: Remove tasks by ID.

## Project Structure

```
LifeOS/
├── src/
│   └── lifeos/
│       ├── lifeos_agents/
│       │   └── task_agent.py    # Task Manager Agent definition
│       ├── tools/
│       │   └── tasks.py         # Task management tools and logic
│       └── run_task_agent.py    # Script to run the Task Manager Agent
├── data/                        # Data storage
├── .env                         # Environment variables
├── pyproject.toml               # Project configuration and dependencies
└── README.md                    # Project documentation
```

## Setup

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    This project uses `uv` for dependency management.
    ```bash
    uv sync
    ```
    Or install manually:
    ```bash
    uv add openai agents python-dotenv truststore
    ```
3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

### Run the Task Manager Agent

To interact with the Task Manager Agent, run the following command:

```bash
uv run src/lifeos/run_task_agent.py
```

This script demonstrates adding a task ("Cook chicken for dinner") and listing all tasks.

## Development

- **Agents**: Defined in `src/lifeos/lifeos_agents/`.
- **Tools**: Defined in `src/lifeos/tools/`.
