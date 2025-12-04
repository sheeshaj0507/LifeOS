from lifeos.db import init_db, engine
from lifeos.models import Task
from sqlmodel import Session, select
import dateparser

# Initialize database
init_db()

# Test adding a task
print("Testing add_task...")
try:
    with Session(engine) as session:
        new_task = Task(
            description="Test task",
            due=None,
            priority="high",
        )
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        print(f"✓ Task added successfully: ID={new_task.id}, Description={new_task.description}")
except Exception as e:
    print(f"✗ Error adding task: {e}")
    import traceback
    traceback.print_exc()

# Test listing tasks
print("\nTesting list_tasks...")
try:
    with Session(engine) as session:
        tasks_list = session.exec(select(Task)).all()
        print(f"✓ Found {len(tasks_list)} tasks")
        for task in tasks_list:
            print(f"  - ID: {task.id}, Description: {task.description}")
except Exception as e:
    print(f"✗ Error listing tasks: {e}")
    import traceback
    traceback.print_exc()
