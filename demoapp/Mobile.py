from fastapi import Body, FastAPI


app = FastAPI()

mobile = [
    {"Model":"realme","cost":20000,"Y O M":2021},
    {"Model":"Redmi","cost":25000,"Y O M":2023},
    {"Model":"Oppo","cost":18000,"Y O M":2020},
    {"Model":"OnePlus","cost":30000,"Y O M":2023},
    {"Model":"iPhone","cost":57000,"Y O M":2023},
    {"Model":"Nokia","cost":2000,"Y O M":2015}
    ]

@app.get("/Mobile")
def read_all_mobiles():
    return mobile

@app.get("/Mobile/{dynamic_param}/{dynamic_param1}/{dynamic_param2}")
def read_all_mobiles(dynamic_param,dynamic_param1,dynamic_param2):
    return {'My Mobile':dynamic_param,'Cost':dynamic_param1,'Y O M':dynamic_param2}

@app.get("/Mobile/{Mobile_Model}")
def read_model(Mobile_Model:str):
    for Model in mobile:
        if Model.get("Model")=="oppo":
            return Model
        
@app.post("/Mobile/creating_Model")
def creating_Model(new_Model=Body()):
    mobile.append(new_Model)

@app.get("/mobile/{Model}")
def read_model(Model:str):
    return_model=[]
    for i in mobile:
        if i.get('Model').casefold()==Model.casefold():
            return_model.append(i)
    return return_model

@app.put("/Mobile/Update_mobile")
def Update_mobile(updated_mobile=Body()):
    for i in range(len(mobile)):
        if mobile[i].get('Model').casefold()==updated_mobile.get('Model').casefold():
            mobile[i]=updated_mobile

@app.delete("/Mobile/delect_mobile/{mobile_Model}")
def delect_mobile(mobile_Model):
    for i in range(len(mobile)):
        if mobile[i].get('Model').casefold()==mobile_Model.casefold():
            mobile.pop(i)