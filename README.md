# scrap_market
`This is and study project, to train my scrap skills`

`This project aims to extract from the Mercado Livre website, to view all the data you searched for in a single Api.`

## 🗿 Features 🗿
* Collects the title, link, price and the thumbnail of any product that you search for.
* This scrap uses bs4 and requests.
* This Api uses fastApi to center all the information you got.
* Can scrap 100+ products from Mercado Livre.
* Allows you to download the data you have searched.

## 🪛 Requirements 🪛
`First of all, you gonna need to clone this repo.`
`1st:`
```
git init
```
`2st. Use this:` 
```
git clone https://github.com/VictorHugoReinicke/scrap_market.git
```
`3st. Access the paste with`
```
cd marketfree
```
`
4st. Install all the necessary library:
`  
```
pip install -r requirements.txt
```

## ♣️ How to use ♣️
`At least, you should access the terminal and uses:`
```
uvicorn main:app
```
`Then access your localhost(probably http://127.0.0.1:800 by default) and then put /docs to see the api`
```
http://127.0.0.1:8000/docs
```

#### Credits
* This readme.md is a model that I used from @forever-prata
