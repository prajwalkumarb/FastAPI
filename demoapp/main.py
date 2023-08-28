from fastapi import FastAPI


app = FastAPI()

@app.get("/abcd")
def index():
    return {'name':'######Prajwal','age':21} 