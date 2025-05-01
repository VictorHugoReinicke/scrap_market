from fastapi import FastAPI
from scrap import main as scrap_main
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}