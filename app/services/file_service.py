import csv
import json
import codecs
import os


from sqlalchemy.orm import Session
from ..database.model_file_service import FileTableModel
from app.database.connection import engine, async_local_session


class FileService:
  async def creat_bulk_insert(file):

      try:
        async with async_local_session() as session:
                  reader = csv.reader(codecs.iterdecode(file.file, 'utf-8'))
                  chunks = []
                  for row in reader:
                    chunks.append(FileTableModel(product_brand=row[0], category=row[1], sub_category=row[2]))
                    if len(chunks) == 100:
                      session.add_all(chunks)
                      chunks.clear()
                    if chunks:
                      session.add_all(chunks)
                      await session.commit()
        return {"filename": file.filename, "success": True}

      except Exception as e:
        print(e)
        filename =  f"{os.path.splitext(file.filename)[0]}.json"
        file_location = os.path.join('app/data/',filename)

        with open(file_location, "a") as f:
            reader = csv.reader(codecs.iterdecode(file.file, 'utf-8'))
            for row in reader:
              f.write(json.dumps({"product_brand": row[0], "category": row[1], "sub_category": row[2]}) + "\n")

        return {"filename": file.filename, "success": False}


  async def write_file_to_json(file):
   try:
    filename =  f"{os.path.splitext(file.filename)[0]}.json"
    file_location = os.path.join('app/data/',filename)

    with open(file_location, "a") as f:
       reader = csv.reader(codecs.iterdecode(file.file, 'utf-8'))
       for row in reader:
          f.write(json.dumps({"product_brand": row[0], "category": row[1], "sub_category": row[2]}) + "\n")
          return {"filename": file.filename, "success": False}
   except Exception as error:
      return {{"filename": file.filename, "error": error}}
