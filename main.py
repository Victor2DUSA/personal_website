from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home Page"})

@app.get("/blog/")
def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request, "title": "Blog Page"})

@app.get("/projects/")
def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "title": "Projects Page"})

@app.get("/skills/")
def skills(request: Request):
    return templates.TemplateResponse("skills.html", {"request": request, "title": "Skills Page"})




