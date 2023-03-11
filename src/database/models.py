import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Log_file(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String)
    target_db = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    #file_ingested = relationship('Ingested', backref=dw_table)


def creste_models(tablename):
    class Create_target_table(Base):
        __tablename__ = tablename
        id = Column(Integer, primary_key=True, autoincrement=True)
        log_id = Column(Integer, ForeignKey('log.id'))
