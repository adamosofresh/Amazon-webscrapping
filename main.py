from bs4 import BeautifulSoup
import requests
import smtplib

my_email = YOUR EMAIL
password = YOUR PASSWORD

link = input("post the link here:")
price_target = float(input("what is your price target?:"))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8,he;q=0.7"
}

response = requests.get(url=link, headers=headers)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
title = soup.find(id="productTitle").get_text()
price = soup.find(name="span", class_="a-offscreen").get_text()
price = price.split("$")
price = float(price[1])
print(price)
print(title)

if price < price_target:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(
            from_addr=my_email,
            to_addrs= RECEIVER EMAIL, msg=f"Subject:Price Alert!\n\n{title}\n{price}!"
        )
else:
    print("Too expensive!")
