from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.views.log import log_router #erro aqui, que vem do modulo  viewa log.py N module named schemas


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


screen = Jinja2Templates(directory="templates")


@app.get('/index/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return screen.TemplateResponse("index.html", context)

app.include_router(log_router)
# app.include_router(file_router)
