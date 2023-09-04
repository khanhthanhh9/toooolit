from pydantic import BaseModel
from typing import Optional

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str
    file_path: Optional[str]

    class Config:
        orm_mode = True