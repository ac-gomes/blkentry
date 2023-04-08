
from fastapi import APIRouter, HTTPException, File, UploadFile, Request, Depends

from ..schemas.utils import DefaultOutput, ErrorOutput, StandardOutput
from ..services.file_service import FileService
from app.schemas.file import UploadForm

file_router = APIRouter(prefix='/file', tags=['upload_file'])

@file_router.post('/', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_upload_file(request: Request, from_data: UploadForm = Depends(UploadForm.from_form)):
  try:
    if not from_data.file:
      return StandardOutput(message='{Not file found}')
    else:
      print(from_data)
      file_service = FileService()
      result = await file_service.creat_bulk_insert(file = from_data.file)
      print(result)
      return StandardOutput(message=result)
  except Exception as error:
    raise HTTPException(400, detail=str(error))


# Original router
# @file_router.post('/upload_file', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
# async def create_upload_file(file: UploadFile = File(...)):

#   try:
#     if not file:
#       return StandardOutput(message='{Not file found}')
#     else:
#       file_service = FileService()
#       result = await file_service.creat_bulk_insert(file=file)
#       print(result)
#       return StandardOutput(message=result)
#   except Exception as error:
#     raise HTTPException(400, detail=str(error))
