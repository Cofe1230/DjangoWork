from bs4 import BeautifulSoup;
import requests;
import pymysql;

#영화이름 평점 예매율

#db연결
dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = 'root'

conn = pymysql.connect(host=dbURL,port=dbPort,user=dbUser, passwd=dbPass,
                       db='bigdb', charset='utf8', use_unicode=True)
insert_sql = "insert into daum_movie(title,grade,reserve) values(%s, %s, %s)"

req = requests.get("https://movie.daum.net/ranking/reservation")

html = req.text
soup = BeautifulSoup(html,'html.parser')

#find 사용
ols = soup.find('ol',class_='list_movieranking')
lis = ols.find_all('div',class_='thumb_cont')

cur = conn.cursor()
for i in lis :
  moviename = i.find('a', class_='link_txt').string
  moviegrade = i.find('span','txt_grade').get_text()
  movieReser = i.find('span',{'class':'txt_num'}).get_text()
  print('영화 : ',moviename, end =' / ')
  print('평점 : ', moviegrade, end=' / ')
  print('예매율 : ', movieReser)
  cur.execute(insert_sql,(moviename,moviegrade,movieReser))
  conn.commit()