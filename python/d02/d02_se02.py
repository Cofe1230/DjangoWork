from selenium import webdriver as wd
from bs4 import BeautifulSoup
import re;

driver = wd.Chrome()
driver.get('https://www.melon.com/chart/index.htm')

#원하는 내용이 소스에 없기 때문에 정적 추출하면 데이터를 받아 올 수 없다
#f12 눌러서 소스 보는 것 처럼 받아오는 방법
page = driver.page_source
# print(page)

soup = BeautifulSoup(page,'html.parser')
tbody = soup.select_one('#frm > div > table > tbody')
trs = tbody.select('tr#lst50')

data = []

for tr in trs :
  rank = tr.select_one('span.rank').get_text()
  name = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
  singer = tr.select_one(' div.ellipsis.rank02 > a').get_text()
  album = tr.select_one('td:nth-child(7) > div > div > div > a').get_text()
  like = tr.select_one('td:nth-child(8) > div > button > span.cnt').get_text()
  like = re.sub('\n총건수\n','',like) #필요없는 부분 삭제
  like = re.sub(',','',like)
  data.append([rank,name,singer,album,like])

print(data)

# melon.csv 순위, 곡명, 가수, 앨범, 좋아요\n
with open('melon.csv','w', encoding='utf-8-sig') as file :
  file.write('순위,곡명,가수,앨범,좋아요\n')
  for item in data:
    row = ','.join(item)
    file.write(row+'\n')

