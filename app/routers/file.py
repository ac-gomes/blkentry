
from fastapi import APIRouter, HTTPException, File, UploadFile

from ..schemas.utils import DefaultOutput, ErrorOutput, StandardOutput
from ..services.file_service import FileService

file_router = APIRouter(prefix='/file', tags=['upload_file'])


@file_router.post('/upload_file', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_upload_file(file: UploadFile = File(...)):

  try:
    if not file:
      return StandardOutput(message='{Not file found}')
    else:
      file_service = FileService()
      result = await file_service.creat_bulk_insert(file=file)
      print(result)
      return StandardOutput(message=result)
  except Exception as error:
    raise HTTPException(400, detail=str(error))
      # result = await FileService.write_file_to_json(file)
      # return DefaultOutput(message=result)