import requests
from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days = 1)
day_yes = today - timedelta(days = 2)

stock_data = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" : "K8AUGT2N4WG33RBR"
}

news_data = {
    "apiKey": "c2353837c68c4c45a605181f6bb8b8d5",
    "q": "Tesla Inc"
}

New_apikEY = "c2353837c68c4c45a605181f6bb8b8d5"
Stocky_apiKey = "K8AUGT2N4WG33RBR"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response_news = requests.get(url=NEWS_ENDPOINT, params=news_data)
response_news.raise_for_status()
news_content = response_news.json()

req_data = news_content['articles'][0]
title =  req_data['title']
desc =  req_data['description'][0:200]

response = requests.get(url=STOCK_ENDPOINT, params=stock_data)
response.raise_for_status()
final_news_data = response.json()

open_Todaydata = final_news_data['Time Series (Daily)'][str(yesterday)]['1. open']
close_todayData = final_news_data['Time Series (Daily)'][str(day_yes)]['4. close']
percent_diff = ((float(open_Todaydata) - float(close_todayData))/float(close_todayData)) * 100
if percent_diff <0:
    up_down = "🔻"
else:
    up_down = "🔺"

if abs(percent_diff) > 5:
    print("Price is stable")
else:
    print(f"{STOCK_NAME}: {up_down}{abs(round(percent_diff,2))}%")
    print(f"Headline: {title}")
    print(f"Brief: {desc}")
