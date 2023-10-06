from bs4 import BeautifulSoup;
import requests;
import pandas as pd;

#https://www.weather.go.kr/weather/observation/currentweather.jsp
#지역, 온도 습도

req = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(req.text,'html.parser')

tbody = soup.select_one('#weather_table > tbody')
#print(tbody)
data = []
for tr in tbody.select('tr') :
  tds = tr.select('td')
  print('지역 = ',tds[0].text )
  print('온도 = ',tds[5].text )
  print('습도 = ',tds[-4].text )
  print()
  data.append([tds[0].text,tds[5].text,tds[-4].text])

print(data)

# for item in data :
#   print(item)

#일반적인 csv파일 만들기
# with open('weather33.csv','w') as file :
#   print('파일저장')
#   file.write('point, temp, hum \n')
#   for item in data:
#     row = ','.join(item) #scv파일 ,로 연결하기
#     file.write(row+'\n')

# csv파일 pandas로 읽기
# df = pd.read_csv('weather33.csv',encoding='euc-kr')
# print(df)

#pandas를 이용한 csv파일 저장
# df1 = pd.DataFrame(data, columns=('point','temp','hum'))
# df1.to_csv('weather44.csv', encoding='euc-kr', index=False)

df = pd.read_csv('weather44.csv',encoding='euc-kr')
print(df)