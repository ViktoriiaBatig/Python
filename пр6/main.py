import requests
from bs4 import BeautifulSoup
import sqlite3
import sys


# Перенаправляємо стандартний вивід у файл
sys.stdout = open('output.txt', 'w')


# URL-адреса сайту Rozetka для категорії ноутбуків
url = "https://rozetka.com.ua/notebooks/c80004/"


# Робимо HTTP-запит та отримуємо HTML-код сторінки
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


products = []
product_tiles = soup.find_all("div", class_="goods-tile__inner")


# Парсимо інформацію про кожен товар
for tile in product_tiles:
    title = tile.find("span", class_="goods-tile__title").text.strip()
    price = tile.find("span", class_="goods-tile__price-value").text.strip()
    image_element = tile.find("img", class_="goods-tile__picture")
    if image_element:
        image_url = image_element["src"]
    else:
        image_url = ""


    product = {
        "title": title,
        "price": price,
        "image_url": image_url
    }


    products.append(product)


# Створюємо з'єднання з базою даних
conn = sqlite3.connect("products.db")
cursor = conn.cursor()


# Створюємо таблицю, якщо її ще немає
create_table_query = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price TEXT NOT NULL,
    image_url TEXT NOT NULL
)
"""
cursor.execute(create_table_query)


# Записуємо дані в таблицю
for product in products:
    title = product["title"]
    price = product["price"]
    image_url = product["image_url"]


    cursor.execute(
        "INSERT INTO products (title, price, image_url) VALUES (?, ?, ?)",
        (title, price, image_url),
    )


conn.commit()
conn.close()


print("Дані успішно записані в базу даних з сайту Rozetka")


# Закриваємо файл для виводу
sys.stdout.close()


