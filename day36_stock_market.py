news_api = "65abf95bb23e4f65aec8bac029e6abc0"
stock_api = "UQAJK7J49CZV1AYS"

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={stock_api}'
stock_r = requests.get(stock_url)
stock_data = stock_r.json()

company_name = input("Enter a company name.\n").lower()
news_url = f'https://newsapi.org/v2/everything?q=%22{company_name}%22&apiKey=65abf95bb23e4f65aec8bac029e6abc0'
news_r = requests.get(news_url)
news_data = news_r.json()

# print(news_data["status"])

all_news_articles = news_data["articles"]
all_descriptions = []

for i in range(len(all_news_articles)): 
    all_descriptions.append(all_news_articles[i]["title"])
    # all_descriptions.append(all_news_articles[i]["content"])

for description in all_descriptions: 
    print(f"{description}\n")

# Ask user for the company name
# replace q keyword with company name in the news url api

# If company exists and theres new present it else tell user theres no news found

# Check for news regarding  company

# Pull up descriptions tied to the said company 

# Cross reference publish day and stock trading info for that day