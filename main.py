from fastapi import FastAPI
from scrap import main as scrap_main
app = FastAPI()

@app.get("/scrap")
async def getFreeMarket(item_search : str ,number_items: int):
    return await scrap_main(item_search,number_items)