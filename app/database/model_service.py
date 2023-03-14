import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship



Base = declarative_base()


class LogFile(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100), index=True)
    target_db = Column(String(50), index=True)
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)
    werehouse = relationship('LogDataWerehouse', backref='log')


class LogDataWerehouse(Base):
    __tablename__ = 'dw_metadata'
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String(50), index=True)
    file_id = Column(Integer, ForeignKey('log.id'))
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)
