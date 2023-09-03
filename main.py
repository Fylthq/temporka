import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time DATETIME,
    temperature FLOAT
)
''')

conn.commit()

conn.close()

import requests
from bs4 import BeautifulSoup

url = "https://example.com/weather"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

temperature_element = soup.find("span", {"class": "temperature"})


temperature = float(temperature_element.text.split()[0])

print(f"Поточна температура: {temperature}°C")
