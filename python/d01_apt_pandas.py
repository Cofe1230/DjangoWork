import pandas as pd

#thousands 숫자 ,
df = pd.read_csv('apt_201910.csv',encoding='cp949', thousands=',')
#print(df)
print(len(df))
#행과 열의 개수를 알려준다
print(df.shape)

##앞, 뒷부분을 출력해서 파일이 어떤식으로 만들어져 있는지 확인 가능하다
print(df.head())
print(df.tail())
print("#"*20)
print(df.면적)

#면적이 200이상 출력 (if문을 안써도 된다)
print(df[df.면적>200])
print("#"*20)

#단지명, 가격, 10개출력
#loc[몇개,[출력할 columns]][조건]
print(df.loc[:10,['단지명','가격']])
print("#"*20)

#단지명, 가격, 면적이 130 초과한 조건에 맞는 데이터 출력
print(df.loc[:,['단지명','가격','면적']][df.면적>130])

#지역 이름에 강릉이 들어간 자료만 출력
print("#"*20)

#find함수는 위치값을 알려주는 것 -1보다 크다는 의미는 강릉이 있다
local_area = df[df.시군구.str.find('강릉')>-1]
print(local_area)

#지역이 강릉인 시군구 가격 면적 10개 출력
print(local_area.loc[:10,['시군구','가격','면적']])

#tuple식 표현법 결과는 같다
print(local_area.loc[:10,('시군구','가격','면적')])

#가격만 5개 출력해보자
print(df['가격'].head())

#면적이 130이 넘는 아파트의 가격
print(df.가격[df.면적>130])

#면적이 130이 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) & (df.가격<20000)])

#면적이 130이 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) | (df.가격<20000)])

#정렬
dfAsc = df.sort_values(by='가격', ascending=False)
print(dfAsc.가격)

print("#"*20)
# 6억원을 초과하는 가격으로 거래된 아파트 가격만 출력
print(df.가격[df.가격>60000])
print("#"*20)
# df.loc[원하는 행 조건, 원하는 열 조건]
# 6억원을 초과하는 가격으로 거래된 단지명(아파트), 가격 출력

print(df.loc[:,['단지명','가격']][df.가격>60000])

#단가 = 가격 / 면적
#'시군구', '면적', '단가' 10개만 출력
df['단가'] = df.가격 / df.면적
print(df.loc[:10,['시군구','면적','단가']])