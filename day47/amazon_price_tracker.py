import os
import smtplib
from pprint import pp

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

EMAIL_PASS = os.getenv("EMAIL_APP_PASS")
print(EMAIL_PASS)
EMAIL = os.getenv("EMAIL")

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
}


response = requests.get(url=url, headers=headers)
response.raise_for_status()

# pp(response.text)

soup = BeautifulSoup(response.text, "html.parser")


# price = soup.select_one("div div span span.a-offscreen")

price_tag = soup.find("span", class_="aok-offscreen")

print(price_tag)
price = float(price_tag.text.strip().split()[0].split("$")[1])

if price < 100.00:
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(EMAIL, EMAIL_PASS)
        server.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"{price}")
