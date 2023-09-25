
import pandas as pd

# numpy : 수치 데이터를 다루는 라이브러리
# pandas : 데이터 분석에 자주 사용하는 테이블 형태를 다루는 라이브러리
  # 1차원 자료구조 : Series
  # 2차원 : Dataframe
  # 3차원 : Panel
# 리스트 [] 튜플 () 딕셔너리 {}
data = {
  'name' : ['Mark', 'Jane', 'aaa', 'rr'],
  'age' : [33 , 44 , 55 , 11],
  'score' : [91.2 , 88.5 , 55.6 , 88.0]
 }
#print(data)
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df['age'].mean())
print(df.age)