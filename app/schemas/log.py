from pydantic import BaseModel
from typing import List


class LogActivityInput(BaseModel):
    file_name: str
    target_table: str


class DefaultOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class DwTableLog(BaseModel):
    file_id: int
    target_db: str


class DataWarehouse(BaseModel):
    id: int
    target_db: str
    file_id: int

    class Config:
        orm_mode = True


class LogListOutput(BaseModel):
    id: int
    file_name: str
    target_table: str
    databases: List[DataWarehouse]

    class Config:
        orm_mode = True
