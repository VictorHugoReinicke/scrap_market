from curl_cffi import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
# import asyncio
# import pandas as pd

async def search_items(search_item, items):
    final_links = []
    numbers_pages = (items // 50) + (1 if items % 50 > 0 else 0)
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
    if item_number % 50 == 0:
        page_number = (item_number // 50 - 1) * 48 + 1
    else:
        page_number = (item_number // 50) * 48 + 1
    return(f"https://lista.mercadolivre.com.br/{search_item}/_Desde_{page_number}_NoIndex_True")

async def parser_product(links):
    products = []
    for link in tqdm(links):
        response = requests.request("GET", link, impersonate="chrome")

        soup = BeautifulSoup(response.text, "html.parser")
        data_json = json.loads(
            soup.find("script", {"type": "application/ld+json"}).string
        )
        product = {
            "product_link": link,
            "product_price": data_json["offers"]["price"],
            "product_title": data_json["name"],
            "product_image": data_json["image"],
        }
        products.append(product)

    print(len(products))
    return products

# def to_save(products):
#     df = pd.DataFrame(products)
#     return df.to_csv("marketfree/scrap_data.csv", index=False)

async def main(search_item, items):
    links = await search_items(search_item,items)
    return await parser_product(links)
    # to_save(products)

if __name__ == "__main__":
    print(main(search_item="", items=1))