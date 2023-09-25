import re
import codecs

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()

print(script101[:100])

Line = re.findall(r'Monica:.+',script101)
print(Line)
print("-"*20)
print(Line[:3])
print(type(Line))
print("-"*20)
All = re.findall(r'All:.+',script101) #All:다음 문자열 찾아와라
print(All) #All의 모든 대사
print(All[-1]) #마지막 대사
print(len(All)) # 몇개?

print("-"*20)
char = re.compile(r'[A-Z][a-z]+:') # compile : 추출하는 포맷을 지정하는 함수 대문자 이후 소문자~문자열 :로 끝남
print(re.findall(char,script101))

a = [1, 2, 3, 4, 5, 2, 2]
print(a)
print(set(a)) #set : 중복을 허용하지 않는 자료구조

print(set(re.findall(char,script101)))
y = set(re.findall(char,script101))
print(type(y))
#set을 list로 바꾸자
print("#"*20)
z = list(y)
print(type(z))
print(z)
##마지막 :을 빼고싶다
for i in z :
  print(i[:-1])
##변수에 담아보자
character = []
for i in z :
  character += [i[:-1]]
print(character)

print("#"*20)
character2 = []
for i in z :
  char = re.sub(':','',i)
  print(char,end=',')
  character2.append(char)
print(character2)