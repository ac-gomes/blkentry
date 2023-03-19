from pydantic import BaseModel
from typing import List

#Use this to input file name into log table
class UploadSingleFile(BaseModel):
    filename: str


#Product
class FileTableFileds(BaseModel):
    product_brand = str
    category = str
    sub_category= str
    created_dt = str