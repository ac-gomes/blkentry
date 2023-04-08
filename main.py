from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routers.log import log_router
from app.routers.file import file_router
from app.schemas.file import UploadForm

from app.schemas.utils import DefaultOutput, ErrorOutput, StandardOutput
from app.services.file_service import FileService
from app.schemas.file import UploadForm


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
screen = Jinja2Templates(directory="templates")

# app.include_router(log_router)

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return screen.TemplateResponse("upload-file.html", context)


@app.post('/', response_class=HTMLResponse, response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_upload_file(request: Request, form_data: UploadForm = Depends(UploadForm.from_form)):
  try:
    if not form_data.file:
      return StandardOutput(message='{Not file found}')
    else:
      print(f"databse: {form_data.database}, \n table: {form_data.table}, \n file:{form_data.file}")
      file_service = FileService()
      result = await file_service.creat_bulk_insert(file = form_data.file)
      print("Result: ",result)
    return screen.TemplateResponse("upload-file.html", {'request': request})
  except Exception as error:
    print(error)
    raise HTTPException(400, detail=str(error))


