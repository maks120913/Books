import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

book_titles = []

for page_num in range(1, 51):
    url = base_url.format(page_num)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Сторінку {page_num} не вдалося завантажити")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')

    for h3 in soup.find_all('h3'):
        book_title = h3.find('a')['title']
        book_titles.append(book_title)

for title in book_titles:
    print(title)
