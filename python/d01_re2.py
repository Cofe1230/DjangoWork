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

print("#"*25)
print()
print()
print(script101)

ch = 'Scene:'
ch = re.sub(':','',ch)
print(ch)

a = '제 이메일 주소는 greate@naver.com'
a += ' 오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)
a1 = re.findall(r'[a-z]+@[a-z.]+',a)
print(a1)

##############################
words = ['apples', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
mm = []
for i in words:
  mm += re.findall('a[a-z]+',i)
print(mm)

for i in words:
  m = re.search(r'a[a-z]+',i)
  if m:
    print(m.group())
print()

for i in words :
  #m = re.match(r'a[a-z]+',i) # match : 시작 위치에서 pattern을 찾음
  m = re.match(r'a\D+',i) #\d(숫자) \D(숫자 아닌) >> a이후로 숫자가 아닌것 모두 추가
  if m:
    print(">>>> ", m.group())
