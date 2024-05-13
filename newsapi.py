import requests
import json

query = input("What type of news are you interested IN?")
url = (f"https://newsapi.org/v2/everything?q={query}&"
       f"from=2024-04-12&sortBy=publishedAt&apiKey=366726b63d8a4873935ea50bc773fee3")

r = requests.get(url)
news = json.loads(r.text)
print(news, type(news))
