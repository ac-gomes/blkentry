from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from app.routers.log import log_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
screen = Jinja2Templates(directory="templates")

app.include_router(log_router)
# app.include_router(file)


@app.get('/index/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return screen.TemplateResponse("index.html", context)

