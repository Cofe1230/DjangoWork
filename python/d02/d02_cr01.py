from bs4 import BeautifulSoup;
import re;

html2 = """
  <html><body>
    <h1 id='title'>스크레이핑이란?</h1>
    <p id='body'>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
soup = BeautifulSoup(html2, 'html.parser')
h1 = soup.html.body.h1
print(h1)
title = soup.find(id='title')
print(title)
print('body : ', soup.find(id='body').string)

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa</li>
    </ul>
"""

soup2 = BeautifulSoup(html,'html.parser')
#https 와 shttps를 다 찾는다
#lis = soup2.find_all(href=re.compile(r'https://'))
#https로 싲가하는 것만 찾으려면 정규표현식 ^ : ~로 시작하는 을 사용한다
lis = soup2.find_all(href=re.compile(r'^https://'))
print(lis)

for e in lis :
  print(e.attrs['href'])