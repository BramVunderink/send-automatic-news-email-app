import requests
from send_email import send_email
from datetime import date

today = date.today().isoformat()

api_key = "ac262d94649641d88143bdcfa1c510e3"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    f"from={today}&" \
    "sortBy=publishedAt&" \
    "apiKey=ac262d94649641d88143bdcfa1c510e3&" \
    "language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's news\n\n"

for article in content["articles"][:20]:
    body += (article["title"] + "\n"
             + article["description"] + "\n"
             + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(body)
