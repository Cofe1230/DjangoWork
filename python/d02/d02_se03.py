from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd;
import re;

#selenium 사용해서 추출해보기

driver = wd.Chrome()
#동적 크롤링 할 때는 데이터를 받아오기전에 크롤링 하면 오류가 날 수 있어 로딩시간을 주는 것이 좋다
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')

# //*[@id="frm"]/div/table/tbody xpath를 써도 된다
tbody = driver.find_element(By.XPATH,'//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME,'tr')

data = []
for tr in trs:
  rank = tr.find_element(By.CLASS_NAME,'rank').text
  name = tr.find_element(By.CLASS_NAME,'wrap_song_info').find_element(By.TAG_NAME,'a').text
  singer = tr.find_element(By.CSS_SELECTOR,'div.ellipsis.rank02').find_element(By.TAG_NAME,'a').text
  album = tr.find_element(By.CSS_SELECTOR,'div.ellipsis.rank03').find_element(By.TAG_NAME,'a').text
  like = tr.find_element(By.CLASS_NAME,'like').find_element(By.CLASS_NAME,'cnt').text
  like = re.sub(',','',like)
  data.append([rank,name,singer,album,like])

print(data)

df1 = pd.DataFrame(data,columns=('순위','제목','가수','엘범','좋아요 수'))
df1.to_csv('melon33.csv', encoding='utf-8-sig', index=False)