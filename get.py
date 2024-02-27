import requests

# 指定 URL に GET通信
res = requests.get('https://joytas.net/kaba/')
# 文字化け対策
res.encoding = res.apparent_encoding

print(res.text)