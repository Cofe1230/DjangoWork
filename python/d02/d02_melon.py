import requests;
from bs4 import BeautifulSoup;
import re;

header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup)

tbody = soup.select_one('#frm > div > table > tbody')
trs = tbody.select('tr#lst50')

data = []

for tr in trs :
  rank = tr.select_one('span.rank').get_text()
  name = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
  singer = tr.select_one(' div.ellipsis.rank02 > a').get_text()
  album = tr.select_one('td:nth-child(7) > div > div > div > a').get_text()
  like = tr.select_one('td:nth-child(8) > div > button > span.cnt').get_text()
  like = re.sub('\n총건수\r\n\t\t\t\t\t\t\t\t\t\t\t\t0\r\n\t\t\t\t\t\t\t\t\t\t\t','',like) #필요없는 부분 삭제
  like = re.sub(',','',like)
  data.append([rank,name,singer,album,like])

print(data)