from datetime import date
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base



Base = declarative_base()


class LogFile(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String)
    target_db = Column(String)