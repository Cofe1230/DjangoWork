import pymysql;
import requests;
from bs4 import BeautifulSoup;
import matplotlib as mpl
import matplotlib.pyplot as plt

#db에서 불러와서 그래프로 그리기

#db연결
dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = 'root'

conn = pymysql.connect(host=dbURL,port=dbPort,user=dbUser, passwd=dbPass,
                       db='bigdb', charset='utf8', use_unicode=True)

insert_sql = "insert into forecast(city,tmef,wf,tmn,tmx) values(%s,%s,%s,%s,%s)"

select_weather = "select tmef from forecast order by tmef desc limit 1"

req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html = req.text
soup = BeautifulSoup(html,'lxml')

cur = conn.cursor()
weather = {}
body = soup.select_one('body')
cur.execute(select_weather)
last_date = cur.fetchone()
print(last_date)

for location in body.select('location'):
  weather[location.find('city').text]=[]
  city = location.city.text
  for data in location.select('data'):
    # tmef = data.tmef.text
    # wf = data.wf.text
    # tmn = data.tmn.text
    # tmx = data.tmx.text
    # cur.execute(insert_sql,(city,tmef,wf,tmn,tmx))
    # conn.commit()
    temp = []
    if (last_date is None) or (str(last_date[0]) < data.find('tmef').text):
      temp.append(data.find('tmef').text)
      temp.append(data.find('wf').text)
      temp.append(data.find('tmn').text)
      temp.append(data.find('tmx').text)
      weather[location.find('city').string].append(temp)
#print(weather)
for i in weather:
  for j in weather[i]:
    cur.execute(insert_sql,(i,j[0],[1],j[2],j[3]))
    conn.commit()