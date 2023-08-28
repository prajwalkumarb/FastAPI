import sys
from xml.dom import UserDataHandler
from click import password_option
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, APIRouter, Request, Form
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_password_hash, verify_password

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class userVerification(BaseModel):
    username:str
    password : str
    new_password : str


@router.get("/edit-password", response_class=HTMLResponse)
async def edit_user_view(request: Request):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)


    return templates.TemplateResponse("edit-user-password.html", {"request": request, "todo":user})




@router.post("edit-password", response_class=HTMLResponse)
async def edit_todo_commit(request: Request, username: str = Form(...),
                           description: str = Form(...), password: str = Form(...),
                           db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    user_data = db.query(models.users).filter(models.users.username == username).first()

    msg = "Invalid username or password"

    if user_data is not None:
        if username==user_data.username and verify_password(password ,user_data.hashed_password):
            user_data.hashed_password = get_password_hash(password_option)
            db.add(user_data)
            db.commit()
            msg = 'password updated'
    
    return templates.TemplateResponse("edit-user-password.html",{"request":request,"user":user,"msg":msg})