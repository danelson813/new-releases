import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import lxml

url = "https://books.toscrape.com"

page = requests.get(url)
soup = bs(page.text, 'lxml')

books = soup.find_all('article')

index = 0
results = []
for book in books:
    title = book.find('a').find('img')['alt']
    price = book.find('p', class_='price_color').text[2:]
    result = {
        'title': title,
        'price': float(price)
    }
    print(result)
    results.append(result)
    index += 1

df = pd.DataFrame(results)
df.to_csv('results.csv', index=False)
