import re
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pytagcloud

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
  
