from pydantic import BaseModel

class DefaultOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str