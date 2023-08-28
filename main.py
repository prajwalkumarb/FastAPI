from fastapi import FastAPI
import models as models
from database import engine
from Router import auth,todos,users
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse 

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/ststic",StaticFiles(directory = "static"),name = "static")

@app.get("/")
def root():
    return RedirectResponse(url="/todos",status_code=status.HTTP_302_FOUND)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
