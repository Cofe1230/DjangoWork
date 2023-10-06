import pymysql;
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

select_sql = "select grade from daum_movie"

cur = conn.cursor()
cur.execute(select_sql)
#결과값 반환 방법
movies = cur.fetchall() #tuple형
print(type(movies))

#평점이 9점이상, 8점이상, 6점이상, 6점미만 ==> pie
movieDic = {'9점 이상' : 0,'8점 이상' : 0,'6점 이상' : 0, '6점 미만':0}
for movie in movies :
  movie = float(movie[0])
  if movie >= 9 :
    movieDic['9점 이상'] += 1
  elif movie >= 8 :
    movieDic['8점 이상'] += 1
  elif movie >= 6 :
    movieDic['6점 이상'] += 1
  else :
    movieDic['6점 미만'] += 1

print(movieDic)

#한글
font_name = mpl.font_manager.FontProperties(fname='C:/windows/fonts/malgun.ttf').get_name()
mpl.rc('font',family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(movieDic.values(),labels=movieDic.keys(),autopct='%.1f%%')
plt.show()