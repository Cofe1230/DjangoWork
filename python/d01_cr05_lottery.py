import requests;
from bs4 import BeautifulSoup

res = requests.get("https://m.dhlottery.co.kr/gameResult.do?method=byWin")
soup = BeautifulSoup(res.content,"html.parser")
#print(soup)
lottery_num = soup.find_all('span', class_ = 'ball')
lottery_num2 = soup.select('span.ball')
#print(lottery_num)
for i in lottery_num:
  print(i.get_text(), end='\t')

print()

#개발자 도구에서 추출할 값 우클릭 => Copy => Copyselector 
#container > div > div.bx_lotto_winnum > span:nth-child(1)
nums = soup.select('#container > div > div.bx_lotto_winnum > span.ball')
for i in nums:
  print(i.string, end='\t')