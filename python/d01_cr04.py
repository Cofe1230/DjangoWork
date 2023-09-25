import requests;
from bs4 import BeautifulSoup;
import re

res = requests.get("https://news.daum.net/economic/")
soup = BeautifulSoup(res.content, "html.parser")
# print(soup)
links = soup.select('a[href]')
print(links)
#a[href=https...]로 시작하는 것에 들어있는 것 텍스트를 출력하고 싶다
for i in links:
  if re.search('https://v.\w+', i['href']):  # .: 임의의 문자 1개, \w : 숫자와 문자
    print(i.get_text().strip())