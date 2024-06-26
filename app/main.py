from fastapi import FastAPI , Request
import pathlib
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR/ "templates" ))
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_view(request:Request):
    return templates.TemplateResponse("home.html",{"request":request,"abc":123})
