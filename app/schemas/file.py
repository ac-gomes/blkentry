from fastapi import Form, File, UploadFile
from pydantic import BaseModel

#Use this to input file name into log table
class UploadSingleFile(BaseModel):
    filename: str


#Product
class FileTableFileds(BaseModel):
    product_brand = str
    category = str
    sub_category= str
    created_dt = str

class UploadForm(BaseModel):
        database: str
        table: str
        file: UploadFile


        @classmethod
        def from_form(
            cls,
            database: str = Form(...),
            table: str = Form(...),
            file: UploadFile = File(...)
        ):
            return cls (
            database = database,
            table = table,
            file = file

            )

