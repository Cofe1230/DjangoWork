import pandas as pd

# year  sales
# 2018  350
# 2019  400
# 2020  1050
# 2021  2000
# 2022  1000
data_dic={
  'year' : [2018, 2019, 2020, 2021, 2022],
  'sales' : [350, 400, 1050, 2000, 1000]
}

print(data_dic)
print(type(data_dic))

df = pd.DataFrame(data_dic)
print(df)
print(type(df))

print('='*20)

df2 = pd.DataFrame([[78.5, 92.4, 73.5], [76.3, 56.6, 96.3]],
                   index=['중간고사','기말고사'],
                   columns = ['1반', '2반', '3반'])
print(df2)

df3 = pd.DataFrame([[20201101, 'Kim', 90, 95],[20201102, 'Lee', 80, 85],
                    [20201103, 'Hong', 70, 75], [20201104, 'Park', 60, 95]],
                    columns=['학번','이름','중간고사','기말고사'])

print(df3)
print('df3 중간고사 합계 : ', df3.중간고사.sum())
print('df3 기말고사 합계 : ', df3.기말고사.sum())

#새로운 column을 만들때는 df3.{columnName} 이런식의 표현은 불가능하다
df3['총점'] = df3.중간고사 + df3.기말고사
print(df3)
print('='*20)
print(df3.sum())
print("시험평균 ㅣ ",df3.총점.mean())
print('*'*20)
df4 = pd.DataFrame([[20201101, 'Kim', 90, 95],[20201102, 'Lee', 80, 85],
                    [20201103, 'Hong', 70, 75], [20201104, 'Park', 60, 95]])
print(df4)
df4.columns = ['학번','이름','중간고사','기말고사']
print(df4)
print(df4.tail())

#csv 출력 pandas는 간편하게 가능하다

df3.to_csv('pandas2.csv',header='False')
#pandas csv파일 읽기
df5 = pd.read_csv('pandas2.csv',encoding='utf-8')
print(df5)