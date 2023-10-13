import wordcloud
import matplotlib.pyplot as plt

keywords = {'안녕' : 2, '하세요' : 1,'빅데이터' : 15, '웹크롤링':3}
#한글
wc = wordcloud.WordCloud(font_path='C:/windows/fonts/malgun.ttf')
cloud=wc.generate_from_frequencies(keywords)

figure = plt.figure()
plt.imshow(cloud)
plt.show()
figure.savefig('word.png')