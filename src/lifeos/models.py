from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    description: str = Field(min_length=1)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    due: Optional[datetime] = None
    priority: str = "normal"
    status: str = "pending"