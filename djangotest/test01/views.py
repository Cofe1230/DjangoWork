from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from test01.models import Board, Comment, Movie, Forecast
from django.db.models import Q
from django.core.paginator import Paginator
from .form import UserForm
from django.db.models.aggregates import Count, Avg
import json

###
import json
from test01 import dataProcess
import pandas as pd

#UPLOAD_DIR
UPLOAD_DIR = 'C:/Users/it/Desktop/GitClone/DjangoWork/Django/upload/'

#wordcloud
def wordcloud(request):
  a_path = "C:/Users/it/Desktop/GitClone/DjangoWork/Django/myDjango03/data/"
  data = json.loads(open(a_path+'4차 산업혁명.json','r',encoding='utf-8').read())

  dataProcess.make_wordCloud(data)

  return render(request,'bigdata/word.html',{'img_data' : 'k_wordCloud.png'})

#wordcloud2
def wordcloud2(request):
  a_path = "C:/Users/it/Desktop/GitClone/DjangoWork/Django/myDjango03/data/"
  data = json.loads(open(a_path+'4차 산업혁명.json','r',encoding='utf-8').read())

  dataProcess.make_wordCloud2(data)

  return render(request,'bigdata/word.html',{'img_data' : 'pytag_word.png'})

#melon
def melon(request):
  #순위, 곡명, 가수, 앨범
  data = []
  dataProcess.melon_crawring(data)
  return render(request, 'bigdata/melon.html',{'data':data})

#movie_chart
def movie_chart(request):
  data = []
  dataProcess.movie_crawing(data)
  #print(data)
  df = pd.DataFrame(data, columns=['제목','평점','예매율'])
  #print(df)
  #group_title = df.groupby('제목')
  group_mean = df.groupby('제목')['평점'].mean().sort_values(ascending=False).head(10)
  print(group_mean)
  dataProcess.movie_daum_chart()
  return render(request,'bigdata/movie_daum.html')

#board_form
@login_required(login_url='/login/')
def board_form(request):
  return render(request,'board/insert.html')

#board_insert
@csrf_exempt
def board_insert(request):
  #파일 업로드
  fname = ''
  fsize = 0
  if 'file' in request.FILES:
    file = request.FILES['file']
    fsize = file.size
    fname = file.name
    fp = open('%s%s' %(UPLOAD_DIR,fname),'wb')
    for chunk in file.chunks():
      fp.write(chunk)
    fp.close()
  dto = Board(writer = request.user,
              title = request.POST['title'],
              content = request.POST['content'],
              filename = fname,
              filesize = fsize,
              )
  dto.save()
      
  return redirect("/boards/")

#list_page
def board_list(request):
  page = request.GET.get('page',1)
  word = request.GET.get('word','')

  boardCount = Board.objects.filter(
    Q(title__contains = word)|
    Q(content__contains = word)).count()
  
  boardList = Board.objects.filter(
    Q(title__contains = word)|
    Q(content__contains = word)).order_by('-id')
  
  #페이징 처리
  pageSize = 5

  paginator =  Paginator(boardList,pageSize)
  page_obj = paginator.get_page(page)
  print('page_obj : ', page_obj)


  context = {
    'boardCount' : boardCount,
    'page_list' : page_obj,
    'word' : word,
  }
  return render(request, 'board/list.html', context)

#board_detail
def board_detail(request,board_id):
  board = Board.objects.get(id = board_id)
  board.hit_up()
  board.save()
  return render(request,'board/detail.html',{'board':board})

#comment_insert
@csrf_exempt
def comment_insert(request):
  id = request.POST['board_id']
  comment = Comment(writer=request.user, board_id = id,
                    content = request.POST['content'])
  comment.save()
  return redirect('/boards/'+id)

#map
def map(request):
  dataProcess.map()
  return render(request,'bigdata/map.html')

#signup
def signup(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
    else :
      print('sss')
  else:
    form = UserForm()

  return render(request,'common/signup.html',{'form' : form })


# movie_chart
def movie_chart(request):
    data = [] 
    data = dataProcess.movie_crawing(data)
    # print(data)
    df = pd.DataFrame(data, columns=['제목','평점','예매율'])
    # print(df)
    group_title = df.groupby('제목')
    # print(group_title)
   
    # 제목별 그룹화 해서 평점의 평균
    group_mean = df.groupby('제목')['평점'].mean().sort_values(ascending=False).head(10)
    # print(group_mean)
    df1 = pd.DataFrame(group_mean, columns=['평점'])
    print(df1)
    dataProcess.movie_daum_chart(df1.index, df1.평점)

    return render(request, 'bigdata/movie_duam.html', 
                  {'img_data' : 'movie_daum_fig.png'})

# movie ==> 테이블(Movie)에 insert 
def movie(request):
    data = []
    dataProcess.movie_crawing(data)
    # data 들어있는 순서 : title, point, reserve
    for r in data:
        movie = Movie(title = r[0],
                      point = r[1],
                      reserve = r[2])
        movie.save()
    return redirect('/')


# movie_dbchart 
def movie_dbchart(request):
  # movie  테이블에서 제목(title)에 해당하는 평점(point) 평균을 구하기
    # data = Movie.objects.values('title').annotate(point_avg=Avg('point'))[0:10]
    data = Movie.objects.values('title').annotate(point_avg=Avg('point')).order_by('-point_avg')[0:10]
    # print('data query : ', data.query)
    df = pd.DataFrame(data)
    print('df : ', df)
    dataProcess.movie_chart(df.title, df.point_avg)
    return render(request, 'bigdata/movie.html',
                  {'img_data' : 'movie_fig.png',
                   'data' : data })

# weather
def weather(request):
    last_date = Forecast.objects.values('tmef').order_by('-tmef')[:1]
    print('last_date query : ', last_date.query)
    weather = {}
    dataProcess.weather_crawing(last_date,weather)
    for i in weather:
        for j in weather[i]:
            dto = Forecast(city = i, tmef=j[0] ,
                           wf =j[1], tmn=j[2], tmx =j[3])
            dto.save()
    # 부산 정보만 출력
    result = Forecast.objects.filter(city='부산')
       
    result1 = Forecast.objects.filter(city='부산').values('wf').annotate(dcount=Count('wf')).values("dcount", "wf")    
    # print('result1 ' , result1.query) 
    df = pd.DataFrame(result1)
    print('df ' , df) 
    image_dic = dataProcess.weather_chart(result, df.wf, df.dcount)

    print('image_dic : ', image_dic)
    return render(request, 'bigdata/chart.html',
                  {'img_data' : image_dic})

