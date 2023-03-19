import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class LogFile(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100), index=True)
    target_table = Column(String(50), index=True)
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)
    databases = relationship('LogDataWerehouse', backref='log', lazy='subquery')


class LogDataWerehouse(Base):
    __tablename__ = 'dw_metadata'
    id = Column(Integer, primary_key=True, autoincrement=True)
    target_db = Column(String(50), index=True)
    file_id = Column(Integer, ForeignKey('log.id'))
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)


class FileTableModel(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_brand = Column(String(100), index=True)
    category = Column(String(100), index=True)
    sub_category= Column(String(100), index=True)
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)