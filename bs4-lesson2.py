import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
for i in range(1,50):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    resp = requests.get(url)
    rresp = resp.content
    soup = BeautifulSoup(rresp, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    
    
    for arti in articles:
        img = arti.find('img')
        title = img.attrs['alt']
        p = arti.find('p')
        star = p['class'][1]
        price = arti.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, price, star])
df = pd.DataFrame(books, columns=['title','price','star rating'])
df.to_csv('books.csv')