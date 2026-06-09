from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Log(Base):
    __tablename__ = "Logs"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, nullable=False)
    message = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)