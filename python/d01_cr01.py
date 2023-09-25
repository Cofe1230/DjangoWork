from bs4 import BeautifulSoup;

html = """
  <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup)

#h1에 있는 것을 출력해보자
h1 = soup.html.h1
print(h1)
p = soup.html.p
print(p)

#두번째 p가 찍고싶은데?
p1=p.next_sibling.next_sibling
print(p1)

#h1의 문자만 출력해보자
print("h1 : ", h1.string)