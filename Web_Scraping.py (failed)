import csv
import urllib.request
from bs4 import BeautifulSoup


URL = "https://finance.yahoo.com/most-active/"


def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)

# def scraping(url):
html = download_page(URL)
stocks = []
soup = BeautifulSoup(html, features="html.parser")
stocks_list = soup.find("div", attrs={"class": "Ovx(a) Ovx(h)--print Ovy(h) W(100%)"})

for stock in stocks_list.find_all("tr"):
    name_list = stock.find("td", attrs={"class": "Va(m) Ta(start) Px(10px) Fz(s)"})
    if name_list:
        name = name_list.string
    price_list = stock.find("td", attrs={"class": "Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)"})
    if price_list:
        price = price_list.string
        stocks.append((name, price))

with open("data/stocks.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    fields = ("stock_name", "stock_price")
    writer.writerow(fields)
    writer.writerows(stocks)
