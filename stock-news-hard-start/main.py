import requests
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "VYEO9K4OVG7PP4EL"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "db5460f7361b4b4283207dfb70e5589b"


def get_news():
    params_news = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    response_news = requests.get(url=NEWS_ENDPOINT, params=params_news)
    print(response_news.status_code)
    articles_data = response_news.json()["articles"][:3]
    articles = []
    for article in articles_data:
        new_dict = {"title": article["title"],
                    "description": article["description"],
                    "url": article["url"]
                    }
        articles.append(new_dict)

    return articles


## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
params_stock = {
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=params_stock)
print(response_stock.status_code)

daily_data = response_stock.json()["Time Series (Daily)"]
closing_price = float(list(daily_data.values())[0]["4. close"])
previous_price = float(list(daily_data.values())[1]["4. close"])
delta = round((closing_price - previous_price) * 100 / closing_price, 1)
if delta > 0 or delta < 0:
    news_list = get_news()
    message_title = f"{STOCK} is up/down {delta}%\n\n"
    message_bodies = [f"Headline: {news['title']}\nBrief: {news['description']}\nURL: {news['url']}\n\n" for news in
                      news_list]
    message_body = message_title + "".join(message_bodies)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    # HINT 1: Consider using a List Comprehension.

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "AC6ac056104ef821352a9be010096fdeee"
    auth_token = "ce43f0c57b263aae54acd4c3f08caa62"

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=message_body,
        from_='+14842710546',
        to='+61 467 662 865'
    )

    print(message.status)

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
