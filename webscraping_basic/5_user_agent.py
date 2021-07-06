

import requests

url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.raise_for_status()  # 문제가 생겼을지 여기서 멈춤
print("웹 스크래핑을 진행합니다.")

# print(res.text) # text 로 다 갖고오기
print(len(res.text))  # text length 갖고오기

# html 파일로 갖고올수있음.. 와 개쩐다...
# "w"는 쓰기모드 : write
with open("limhoooo.html", "w", encoding="utf8") as f:
    f.write(res.text)
