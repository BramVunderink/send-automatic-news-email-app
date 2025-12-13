import requests
from send_email import send_email

api_key = "ac262d94649641d88143bdcfa1c510e3"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2025-11-13&sortBy=publishedAt&apiKey=" \
    "ac262d94649641d88143bdcfa1c510e3"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
