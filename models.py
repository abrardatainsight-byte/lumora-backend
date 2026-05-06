from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from database import Base
import datetime

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)          # "hr" or "employee"
    company = Column(String, index=True) 

class EmotionLog(Base):
    """
    Stores one record per capture cycle.
    emotion_text holds the full 9-class label (not collapsed to 4).
    raw_score is the model's confidence for that label.
    """
    __tablename__ = "emotion_logs"
    id = Column(Integer, primary_key=True, index=True)
    employee_username = Column(String, ForeignKey("users.username"), index=True)
    emotion_text = Column(String)           
    raw_score = Column(Float, default=0.0)  
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)

class SystemState(Base):
    __tablename__ = "system_state"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True, unique=True) # REQUIRED for multi-company isolation
    capture_requested = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
