from pathlib import Path
from typing import Generator

from sqlmodel import SQLModel, create_engine, Session


# ---------- Database configuration ---------- #

# Path to the SQLite database file
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "tasks.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create all database tables if they do not exist yet.
def init_db() -> None:    
    SQLModel.metadata.create_all(engine)

# Generator for database sessions
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
