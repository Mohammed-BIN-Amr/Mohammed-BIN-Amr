import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()  # raise an exception if the status code is not 200
except requests.exceptions.RequestException as e:
    print("Error:", e)
    sys.exit(1)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

for book in books:
    book_title = book.h3.a["title"]
    book_rating = book.p["class"][1]
    book_price = book.select_one(".price_color").get_text()[1:]
    print(f"Book titled: {book_title}")
    print(f"Has a rating of: {book_rating} stars.")
    print(f"Price: {book_price}")