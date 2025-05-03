from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    due_date = Column(DateTime, nullable=True)
    completed = Column(Boolean, default=False)
    priority = Column(Integer, default=1)  # 1: Low, 2: Medium, 3: High
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign key to link tasks with users
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationship with the User model
    owner = relationship("User", back_populates="tasks")