from dotenv import load_dotenv
import requests
import os

load_dotenv()
stock_api = os.getenv('STOCK_API_KEY')

company_ticker = input("Enter a company ticker.\n").upper()
news_url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={company_ticker}&apikey={stock_api}'
news_r = requests.get(news_url)
news_data = news_r.json()

stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company_ticker}&interval=5min&apikey={stock_api}'
stock_r = requests.get(stock_url)
stock_data = stock_r.json()

print(news_r.status_code)
print(stock_r.status_code)

data_to_render = {}



for day in stock_data["Time Series (Daily)"]: 
    
    day_data = stock_data["Time Series (Daily)"][day]
    split_date = day.split("-")
    formatted_date = "".join(split_date)
    relevant_news = []
  
    for news in news_data["feed"]: 
        formatted_news_date = news["time_published"].split("T")[0]

        if formatted_date == formatted_news_date: 
            relevant_news.append(f"Title: {news['title']}\nSource: {news['source']}\nUrl: {news['url']}\n")


    data_to_render[day] = {
        'prices': {
            'open': day_data["1. open"],
            'close': day_data["4. close"],
            'high': day_data["2. high"],
            'low': day_data["3. low"],
        }, 
        'relevant news': relevant_news
    }

    # print(f"-----------{day}-----------\n")
    # print(f'Open: {day_data["1. open"]}')
    # print(f'Close: {day_data["4. close"]}')
    # print(f'High: {day_data["2. high"]}')
    # print(f'Low: {day_data["3. low"]}\n ')
    # print("Relevant News\n")
    # for news in relevant_news: 
    #     if formatted_date == formatted_news_date: 
    #         print(news)

    # print("------------------------------\n")


    

for  day in data_to_render: 
    prices = data_to_render[day]['prices']
    news = data_to_render[day]['relevant news']

    if len(news) > 0:

        print(f"-----------{day}-----------\n")
        print(f'Open: {prices["open"]}')
        print(f'Close: {prices["close"]}')
        print(f'High: {prices["high"]}')
        print(f'Low: {prices["low"]}\n ')      

        print("Relevant News\n")

        for article in news: 
                print(article)

        print(f"--------------------------------\n")  
        