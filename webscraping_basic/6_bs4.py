import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# soup 객체에서 처음 발견되는 element 를 반환
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])
# test = soup.find("a", attrs={"class": "Nbtn_upload"})
# print(test)

rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.parent)
