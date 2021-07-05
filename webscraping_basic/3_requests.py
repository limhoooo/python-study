

import requests

res = requests.get("http://github.com/limhoooo")
res.raise_for_status()  # 문제가 생겼을지 여기서 멈춤
print("웹 스크래핑을 진행합니다.")

# print(res.text) # text 로 다 갖고오기
print(len(res.text))  # text length 갖고오기

# html 파일로 갖고올수있음.. 와 개쩐다...
# "w"는 쓰기모드 : write
with open("myhompage.html", "w", encoding="utf8") as f:
    f.write(res.text)
