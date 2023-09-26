import re

text = "<title>지금은 문자열 연습입니다.</title>"

#그냥 찍기
print(text[0:7])

#find 사용 - 있으면 위치값 리턴 없으면 -1
print(text.find('문'))
print(text.find('파'))
#index 있으면 위치값 리턴 없으면 error
print(text.index('문'))
#print(text.index('파'))

#strip() => 공백제거 lstrip() 왼쪽 공백 제거 rstrip() 오른쪽 공백 제거
text1 = "      <title>지금은 문자열 연습입니다.</title>         "
text2 = ";"
print(text1.strip()+text2)
print(text1.lstrip()+text2)
print(text1.rstrip()+text2)

#replace 문자열 변경
print(text1.replace("<title>","<div>"))
print(text1.replace("<title>",""))

#re.search 정규 표현식으로 안에 문자 열을 찾아서 출력 안에 텍스트만 원하면 group()를 사용한다.
text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>',text3)
print(body)
body = body.group()
print(body)

#[0-9][a-z]
# ab*c : ac, abc, abbc, abbbc...
# *(0이상) +(1이상), ?(0이상 1이하) .문자
print("-"*30)
text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')

#text4 문자열에서 <title>지금은 문자열 연습</title> 출력
body = re.search("<title.*/title>",text4)
body = body.group()
print(body)
print("#"*20)
#<이후 문자(1개 이상 모두) >가 한개 까지
print(re.search('<.+?>',body).group())
print(re.search('<.+?>',text4).group())
print("#"*20)

#<.+?> 표현식에 해당하는 문자열을 공백으로 변경
body = re.sub('<.+?>','',body)
print(body)




