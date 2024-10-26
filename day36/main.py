import os
import smtplib
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = '"Tesla Inc"'
AV_API_KEY = os.getenv("AV_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
# print(NEWSAPI_KEY)

yesterday = str(datetime.today().date() - timedelta(1))
dbefore_yesterday = str(datetime.today().date() - timedelta(2))


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
av_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": AV_API_KEY,
}
av_response = requests.get(
    url="https://www.alphavantage.co/query", params=av_parameters
)
av_response.raise_for_status()


av_data = av_response.json()

yest_data = av_data["Time Series (Daily)"][yesterday]
db4_yest_data = av_data["Time Series (Daily)"][dbefore_yesterday]


# print(yest_data)
# print(db4_yest_data)

yest_close = float(yest_data["4. close"])
db4_yest_close = float(db4_yest_data["4. close"])

delta = round(abs(yest_close - db4_yest_close), 4)
# print(delta)

percentage = round((delta / yest_close) * 100, 4)
# print(percentage)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
napi_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apikey": NEWSAPI_KEY,
    "pageSize": 3,
}

napi_response = requests.get(
    url="https://newsapi.org/v2/everything", params=napi_parameters
)
napi_response.raise_for_status()
print(napi_response.url)

napi_data = napi_response.json()
# print(napi_data)

napi_articles = napi_data["articles"]
# print(napi_articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if percentage > 5:
    for n in range(napi_parameters["pageSize"]):
        print(napi_articles[n]["title"])
        title = napi_articles[n]["title"].replace("\n", "")
        brief = napi_articles[n]["description"].replace("\n", "")
        print()
else:
    for n in range(napi_parameters["pageSize"]):
        print(napi_articles[n]["title"])
        title = napi_articles[n]["title"].replace("\n", "")
        brief = napi_articles[n]["description"].replace("\n", "")
        print()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
