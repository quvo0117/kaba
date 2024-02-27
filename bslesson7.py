import requests
from bs4 import BeautifulSoup
from pathlib import Path  # フォルダ操作モジュール
import urllib  # url 操作モジュール
import time  # 時間操作モジュール

load_url = 'https://joytas.net/kaba/'
res = requests.get(load_url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, 'html.parser')

# Path オブジェクト作成
out_folder = Path('downloaded')

# Path オブジェクトが downloaded フォルダを作成
# (downloaded という名前が既にあってもエラーにしない)
out_folder.mkdir(exist_ok = True)


# img 要素を全部取得
images = soup.select('img')

# ファイル書き込み
for img in images:
    src = img.get('src')

    # 画像相対 URL を絶対URL に変換
    img_url = urllib.parse.urljoin(load_url, src)

    # get通信で画像をロード
    loaded_img = requests.get(img_url)

    # ファイル名を取得
    file_name = img.get('src').split('/')[-1]

    # 保存画像パス
    out_path = out_folder.joinpath(file_name)

    # wbはバイナリ書き込み
    with open(out_path, 'wb') as file:
        # content はバイナリデータ
        file.write(loaded_img.content)

    # DOS 攻撃にならないように時間をあける (1秒)
    time.sleep(1)