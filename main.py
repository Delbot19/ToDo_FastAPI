from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def index():
    return {"message":"Hello world"}


@app.post("/")
async def post():
    return {"message":"Hello world from post route"}

@app.put("/")
async def put():
    return {"message":"Hello world from put route"}   


@app.get("/items")
async def listItems():
    return {"message":"list items route"}


@app.get("/items/{item_id}")
async def get_id(item_id:int):
    return {"item_id":item_id}