from pydantic import BaseModel
from typing import List


class LogActivityInput(BaseModel):
    file_name: str
    target_db: str


class DefaultOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class DwTableLog(BaseModel):
    file_id: int
    table_name: str


class DataWarehouse(BaseModel):
    file_id: int
    table_name: str
    created_dt: str


class LogListOutput(BaseModel):
    id: int
    file_name: str
    data_warehouse: List[DataWarehouse]

    class Config:
        orm_mode = True
