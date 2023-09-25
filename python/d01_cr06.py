import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

res = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(res.content, "html.parser")
#container > div.aside > div > div.aside_area.aside_popular > table > tbody
tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
data = []
for i in trs:
  name = i.select_one('th>a').get_text()
  price = i.select_one('td').get_text()
  ch_direction = i.select_one('td>img')['alt']
  #ch_direction = i['class'][0]
  ch_price = i.select_one('td>span').get_text().strip()
  data.append([name,price,ch_direction,ch_price])
print(data)
##################################

# write_wb = Workbook()
# write_ws = write_wb.create_sheet('결과')
# for d in data:
#   write_ws.append(d)
# write_wb.save(r'testfinance.xlsx')