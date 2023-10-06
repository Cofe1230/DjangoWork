from bs4 import BeautifulSoup;
import requests;

#영화이름 평점 예매율

req = requests.get("https://movie.daum.net/ranking/reservation")

html = req.text
soup = BeautifulSoup(html,'html.parser')
#select 사용
ol = soup.select_one('#mainContent > div > div.box_ranking > ol')
items = ol.select('li>div.item_poster>div.thumb_cont')
data = []
for i in items :
  title = i.select_one('strong.tit_item>a').get_text()
  grade = i.select_one('span.txt_append>span.info_txt').get_text()
  reserve = i.select_one('span.txt_append>span.info_txt').findNextSibling().get_text()
  data.append([title,grade,reserve])
print(data)

#find 사용
ols = soup.find('ol',class_='list_movieranking')
lis = ols.find_all('div',class_='thumb_cont')

for i in lis :
  moviename = i.find('a', class_='link_txt').string
  moviegrade = i.find('span','txt_grade').get_text()
  movieReser = i.find('span',{'class':'txt_num'}).get_text()
  print('영화 : ',moviename, end =' / ')
  print('평점 : ', moviegrade, end=' / ')
  print('예매율 : ', movieReser)