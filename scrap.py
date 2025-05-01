from curl_cffi import requests
from bs4 import BeautifulSoup
import asyncio

async def search_items(search_item, itens):
    final_links = []
    numbers_pages = (itens // 50) + (1 if itens % 50 > 0 else 0)
    for page_number in range(numbers_pages):
        page = await url(search_item, page_number + 1)
        response = requests.request("GET", page, impersonate="chrome")
        soup = BeautifulSoup(response.text, "html.parser")
        links = [
            link.find("a").get("href")
            for link in soup.find_all("div", {"class": "poly-card__content"})
        ]
        final_links.extend(links)
    return final_links

async def url(search_item, item_number):
    page_number = ((item_number - 1) // 50) + 1
    desde = ((page_number - 1) * 50) + 1
    return(f"https://lista.mercadolivre.com.br/{search_item}/_Desde_{desde}_AGE*GROUP_6725189_NoIndex_True")

async def main():
    return await search_items('graxa', 100)

if __name__ == "__main__":
    asyncio.run(main())