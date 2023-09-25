import requests;
from bs4 import BeautifulSoup;

res = requests.get("https://news.daum.net/digital")
# #print(res)
# #print(res.content)
soup = BeautifulSoup(res.content,'html.parser')
# #print(soup)
# link_title = soup.find_all('a', 'link_txt')
# #print(link_title)
# for i in link_title:
#   print(i.get_text().strip())

links = soup.select('a[href]')
print(links)