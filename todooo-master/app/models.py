from sqlalchemy import Column, Integer, String
from app.database import Base

# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
    file_path = Column(String, nullable=True)
