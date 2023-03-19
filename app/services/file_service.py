import csv
import json
import codecs
import os


from sqlalchemy.orm import Session
from ..database.model_file_service import FileTableModel
from app.database.connection import async_local_session


class FileService:
  async def creat_bulk_insert(self, file):

      try:
        async with async_local_session() as session:
                  reader = csv.reader(codecs.iterdecode(file.file, 'utf-8'))
                  chunks = []
                  for row in reader:
                    chunks.append(FileTableModel(product_brand=row[0], category=row[1], sub_category=row[2]))
                    if len(chunks) == 100:
                      session.add_all(chunks) #remove o await
                      chunks.clear()
                    if chunks:
                      session.add_all(chunks) #remove o await
                      await session.commit()
        return {"filename": file.filename, "success": True}

      except Exception as error:
        error_message = f"An error occurred while processing file {file.filename}: {str(error)}"
        self.write_file_to_json(file)
        return {"error": error_message, "filename": file.filename, "success": False}


  async def write_file_to_json(self, file):
    filename =  f"{os.path.splitext(file.filename)[0]}.json"
    print(filename)
    file_location = os.path.join('app/data/',filename)

    try:
      with open(file_location, "a") as f:
         reader = csv.reader(codecs.iterdecode(file.file, 'utf-8'))
         for row in reader:
            f.write(json.dumps({"product_brand": row[0], "category": row[1], "sub_category": row[2]}) + "\n")
            error_message = f"An error occurred while processing file {file.filename}: {str(e)}"
    except Exception as e:
      print(f"An error occurred while writing to file: {e}")
      return {"filename": file.filename, "success": False, "error": error_message }