
from fastapi import APIRouter, HTTPException, File, UploadFile

from ..schemas.utils import DefaultOutput, ErrorOutput
from ..services.file_service import FileService

file_router = APIRouter(prefix='/file', tags=['upload_file'])


@file_router.post('/upload_file', response_model= DefaultOutput, responses={400: {'model': ErrorOutput}})
async def create_upload_file(file: UploadFile = File(...)):
  try:
    if not file:
      return DefaultOutput(message='Not file found')
    else:
      await FileService.creat_bulk_insert(file)
      return DefaultOutput(message=file.filename)
  except Exception as error:
    raise HTTPException(400, detail=str(error))
      # result = await FileService.write_file_to_json(file)
      # return DefaultOutput(message=result)