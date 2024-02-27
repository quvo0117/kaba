import requests
from bs4 import BeautifulSoup

res = requests.get('https://joytas.net/kaba/')
res.encoding = res.apparent_encoding

# 第1引数: html文字列、第2引数: パーサー指定 (今回はライブラリ不要な 'html.parser')
soup = BeautifulSoup(res.text, 'html.parser')

# BeautifulSoup オブジェクトを print に引き渡すと全文表示
# print(soup)

# タグで要素取得
element = soup.find('title')  # <title>コビトカバ</title>
print(element.text)  #コビトカバ

# 要素を結果セットとして取得 (ResultSet)
images = soup.find_all('img')
for img in images:
    # 属性にアクセスするには getメソッドを使う
    print(img.get('src'))