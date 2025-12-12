import requests

api_key = "ac262d94649641d88143bdcfa1c510e3"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2025-11-12&sortBy=publishedAt&apiKey=" \
    "ac262d94649641d88143bdcfa1c510e3"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
