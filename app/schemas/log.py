from pydantic import BaseModel
# from sqlalchemy.types import  DateTime


class LogActivityInput(BaseModel):
    file_name: str
    target_db: str

class DefaultOutput(BaseModel):
    message: str
