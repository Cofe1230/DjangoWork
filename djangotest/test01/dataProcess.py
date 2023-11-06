import re
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from matplotlib  import font_manager, rc
import matplotlib.pyplot as plt
import pytagcloud
import requests
from bs4 import BeautifulSoup
import pandas as pd
import folium
import os
from djangotest.settings import TEMPLATE_DIR,STATIC_DIR
9

def make_wordCloud(data):
  message = ''
  for item in data:
    if 'message' in item.keys():
      #정규표현식에서 ^는 시작을 의미하지만 []안에서 사용하면 제외
      #[0-9]가 숫자의 패턴을 차즌ㄴ거라면 [^0-9]는 숫자는 패턴을 제외한다는 의미이다
      message = message + re.sub(r'[^\w]',' ', item['message'])+''
  nlp = Okt()
  message_M = nlp.nouns(message)
  count = Counter(message_M)
  word_count=dict()
  for tag, counts in count.most_common(80):
    if (len(str(tag))>1) :
      word_count[tag] = counts

  font_path = "c:/windows/fonts/malgun.ttf"
  wc = WordCloud(font_path, background_color="ivory", width=800, height=600)
  cloud = wc.generate_from_frequencies(word_count)
  plt.figure(figsize=(0,0))
  plt.imshow(cloud)
  plt.axis('off')
  cloud.to_file('./static/images/k_wordCloud.png')

###############################

###############################

def make_wordCloud2(data):
  message = ''
  for item in data:
    if 'message' in item.keys():
      #정규표현식에서 ^는 시작을 의미하지만 []안에서 사용하면 제외
      #[0-9]가 숫자의 패턴을 차즌ㄴ거라면 [^0-9]는 숫자는 패턴을 제외한다는 의미이다
      message = message + re.sub(r'[^\w]',' ', item['message'])+''
  nlp = Okt()
  message_M = nlp.nouns(message)
  count = Counter(message_M)
  word_count=dict()
  for tag, counts in count.most_common(80):
    if (len(str(tag))>1) :
      word_count[tag] = counts

  taglist = pytagcloud.make_tags(word_count.items(), maxsize=50)
  pytagcloud.create_tag_image(taglist,
                              './static/images/pytag_word.png',
                              size=(600,400),
                              fontname='Korean2',
                              rectangular=False)
  
def melon_crawring(data):
  header = {'User-Agent' : 'Mozilla/5.0'}
  req = requests.get('https://www.melon.com/chart/index.htm',headers=header)
  soup = BeautifulSoup(req.text,'html.parser')

  tbody = soup.select_one('#frm > div > table > tbody')
  trs = tbody.select('tr#lst50')

  # for i in range(10):
  #   rank = trs[i].select_one('span.rank').get_text()
  #   name = trs[i].select_one('div.ellipsis.rank01 > span > a').get_text()
  #   singer = trs[i].select_one(' div.ellipsis.rank02 > a').get_text()
  #   album = trs[i].select_one('td:nth-child(7) > div > div > div > a').get_text()
  #   data.append({'rank':rank,'name':name,'singer':singer,'album':album})

  for tr in trs[:10]:
    rank = tr.select_one('span.rank').get_text()
    name = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
    singer = tr.select_one(' div.ellipsis.rank02 > a').get_text()
    album = tr.select_one('td:nth-child(7) > div > div > div > a').get_text()
    data.append({'rank':rank,'name':name,'singer':singer,'album':album})
 
def map():
  ex = {'경도' : [127.061026,127.047883,127.899220,128.980455,127.104071,127.102490,127.088387,126.809957,127.010861,126.836078
                ,127.014217,126.886859,127.031702,126.880898,127.028726,126.897710,126.910288,127.043189,127.071184,127.076812
                ,127.045022,126.982419,126.840285,127.115873,126.885320,127.078464,127.057100,127.020945,129.068324,129.059574
                ,126.927655,127.034302,129.106330,126.980242,126.945099,129.034599,127.054649,127.019556,127.053198,127.031005
                ,127.058560,127.078519,127.056141,129.034605,126.888485,129.070117,127.057746,126.929288,127.054163,129.060972],
    '위도' : [37.493922,37.505675,37.471711,35.159774,37.500249,37.515149,37.549245,37.562013,37.552153,37.538927,37.492388
              ,37.480390,37.588485,37.504067,37.608392,37.503693,37.579029,37.580073,37.552103,37.545461,37.580196,37.562274
              ,37.535419,37.527477,37.526139,37.648247,37.512939,37.517574,35.202902,35.144776,37.499229,35.150069,35.141176
              ,37.479403,37.512569,35.123196,37.546718,37.553668,37.488742,37.493653,37.498462,37.556602,37.544180,35.111532
              ,37.508058,35.085777,37.546103,37.483899,37.489299,35.143421],
    '구분' : ['음식','음식','음식','음식','생활서비스','음식','음식','음식','음식','음식','음식','음식','음식','음식','음식'
             ,'음식','음식','소매','음식','음식','음식','음식','소매','음식','소매','음식','음식','음식','음식','음식','음식'
             ,'음식','음식','음식','음식','소매','음식','음식','의료','음식','음식','음식','소매','음식','음식','음식','음식'
             ,'음식','음식','음식']}
  ex = pd.DataFrame(ex)
  #print(ex)

  #지도의 중심점을 지정하기 위해 위도와 경도의 평균 구하기
  lat = ex['위도'].mean()
  long = ex['경도'].mean()

  #지도 띄우기
  m = folium.Map([lat,long],zoom_start=0)
  for i in ex.index :
    sub_lat = ex.loc[i, '위도']
    sub_long = ex.loc[i, '경도']
    title = ex.loc[i, '구분']

    folium.Marker([sub_lat,sub_long],tooltip=title).add_to(m)
    m.save(os.path.join(TEMPLATE_DIR,'bigdata/maptest.html'))


# movie_crawing 
def movie_crawing(data):
    req = requests.get('https://movie.daum.net/ranking/reservation')
    if req.ok :
        soup = BeautifulSoup(req.text, 'html.parser')
        # 평점, 제목 ,예매율
        ols = soup.select_one('#mainContent > div > div.box_ranking > ol' )
        rankcount = ols.select('li')
        for i  in rankcount:
            title = i.find('a' , class_='link_txt').get_text()
            point = i.find('span', 'txt_grade').get_text()
            reserve = i.find('span', {'class' : 'txt_num'}).get_text()
            reserve = re.sub(r'[%]','',reserve)
            data.append([title,float(point),float(reserve)])
            
        # print(data)

    return data   

# movie_daum_chart
def movie_daum_chart(titles, points):
    font_location="c:/Windows/fonts/malgun.ttf"
    font_name=font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family = font_name)
    plt.cla()
    plt.ylabel('영화평점')
    plt.xlabel('영화제목')
    plt.title('Top 10 영화평점')
    plt.bar(range(len(titles)), points, align='center')
    plt.xticks(range(len(titles)),list(titles),rotation=30,fontsize=5)
    plt.savefig(os.path.join(STATIC_DIR,'images\\movie_daum_fig.png'),dpi=300)

# movie_chart
def movie_chart(titles, points):
    font_location="c:/Windows/fonts/malgun.ttf"
    font_name=font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family = font_name)
    plt.cla()
    plt.ylabel('영화평점')
    plt.xlabel('영화제목')
    plt.title('Top 10 영화평점')
    plt.bar(range(len(titles)), points, align='center')
    plt.xticks(range(len(titles)),list(titles),rotation=30,fontsize=5)
    plt.savefig(os.path.join(STATIC_DIR,'images\\movie_fig.png'),dpi=300)


# weather_crawing
def weather_crawing(last_date, weather):
    req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
    soup = BeautifulSoup(req.text, 'lxml')
    # print(soup)

    for i in soup.find_all('location'):
        weather[i.find('city').text] = []
        for j in i.find_all('data'):
            temp = []
            if(len(last_date)==0) or (j.find('tmef').text > last_date[0]['tmef']):
                temp.append(j.find('tmef').text)
                temp.append(j.find('wf').text)
                temp.append(j.find('tmn').text)
                temp.append(j.find('tmx').text)
                # print('temp : ' , temp)
                weather[i.find('city').string].append(temp)
  

    print(weather)

# weather_chart
def weather_chart(result, wfs, dcounts):
    font_location="c:/Windows/fonts/malgun.ttf"
    font_name=font_manager.FontProperties(fname=font_location).get_name()
    rc('font',family=font_name)

    high = []
    low = []
    xdata = []

    for r in result.values_list():
        # print(r)
        high.append(r[5])
        low.append(r[4])
        xdata.append(r[2])
    plt.cla()
    plt.figure(figsize=(10,6))
    plt.xticks(range(len(xdata)),list(xdata),rotation=30,fontsize=8)
    plt.plot(xdata, low, label='최저기온')
    plt.plot(xdata, high, label='최고기온')
    plt.legend()
    plt.savefig(os.path.join(STATIC_DIR,'images\\weather_plot.png'),dpi=300)

    plt.cla()
    plt.bar(wfs,dcounts)
    plt.savefig(os.path.join(STATIC_DIR,'images\\weather_bar.png'),dpi=300)

    plt.cla()
    plt.pie(dcounts,labels=wfs, autopct='%.1f%%')
    plt.savefig(os.path.join(STATIC_DIR,'images\\weather_pie.png'),dpi=300)

    image_dic ={'bar' : 'weather_bar.png',
                'plot' : 'weather_plot.png',
                'pie' : 'weather_pie.png'    }
    return image_dic


