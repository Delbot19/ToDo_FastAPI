"""
Il s'agit de la page main.
"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def index():
    """
        Il s'agit de la page main.
    """
    return {"message":"Hello world"}
