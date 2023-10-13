import pymysql;

dbURL = '127.0.0.1'
dbPort = 3306
dbUser = 'root'
dbPass = 'root'

conn = pymysql.connect(host=dbURL,port=dbPort, user=dbUser, passwd=dbPass,
                       db='bigdb',charset='utf8',use_unicode=True)


#부산의 정보 추출
select_busan = "select * from forecast where city='부산' order by tmef desc"

cur = conn.cursor()
cur.execute(select_busan)
result = cur.fetchall()
print(result)

select_busan2 = "select max(tmx), min(tmn) from forecast where city='부산'"
cur.execute(select_busan2)
result2 = cur.fetchone()
print('최고 : ',result2[0])
print('최저 : ',result2[1])

# 날짜별 최고기온, 최저기온 출력
datas = []
for row in result:
  datas.append([row[2],row[4],row[5]])
print(datas)