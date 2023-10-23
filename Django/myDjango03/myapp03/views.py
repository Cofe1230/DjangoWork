from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from myapp03.models import Board
from django.db.models import Q
from django.core.paginator import Paginator
###
import json
from myapp03 import dataProcess

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
