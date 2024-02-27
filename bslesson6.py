import requests
from bs4 import BeautifulSoup

res = requests.get('https://joytas.net/kaba/')
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, 'html.parser')

# li 要素の中の a を全部取得
links = soup.select('li a')

# ファイル書き込み
with open('zoo.txt', 'w', encoding='utf-8') as file:
    for link in links:
        file.write(f'{link.text}: {link.get('href')}\n')
