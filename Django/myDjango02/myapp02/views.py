from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp02.models import Board, Comment
from django.db.models import Q
from .form import UserForm
from django.core.paginator import Paginator

import math

# Create your views here.

UPLOAD_DIR = 'C:/Users/it/Desktop/GitClone/DjangoWork/Django/upload/'

#signup
def signup(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      print('ttt')
      form.save()
    else :
      print('sss')
  else:
    form = UserForm()

  return render(request,'common/signup.html',{'form' : form })

#write_form
def write_form(request):
  return render(request,'board/insert.html')

#insert
@csrf_exempt
def insert(request):
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

  dto = Board(writer=request.POST['writer'],
              title = request.POST['title'],
              content = request.POST['content'],
              filename = fname,
              filesize = fsize,
              )
  dto.save()
      
  return redirect("/list_page/")

#boardlist
def boardlist(request):
  page = request.GET.get('page',1)
  word = request.GET.get('word','')
  field = request.GET.get('field','title')

  #count
  #Q연산자
  if field == 'all':
    boardCount = Board.objects.filter(Q(writer__contains=word)|
                                      Q(title__contains=word)|
                                      Q(writer__contains=word)).count()
  elif field == 'write':
    boardCount = Board.objects.filter(Q(writer__contains=word)).count()
  elif field == 'title':
    boardCount = Board.objects.filter(Q(title__contains=word)).count()
  elif field == 'content':
    boardCount = Board.objects.filter(Q(content__contains=word)).count()
  else :
    boardCount = Board.objects.all().count

  #page
  ### 123 [다음] | [이전]456[다음] | [이전]78
  pageSize = 5
  blockPage = 3
  currentPage = int(page)
  totPage = math.ceil(boardCount/pageSize) #총 페이지 수
  startPage = math.floor((currentPage-1)/blockPage)*blockPage+1
  endPage = startPage + blockPage -1 
  if endPage > totPage :
    endPage = totPage

  start = (currentPage-1)*pageSize
  
  #내용
  if field == 'all':
    boardList = Board.objects.filter(Q(writer__contains=word)|
                                      Q(title__contains=word)|
                                      Q(writer__contains=word)).order_by('-id')[start:start+pageSize]
  elif field == 'write':
    boardList = Board.objects.filter(Q(writer__contains=word)).order_by('-id')[start:start+pageSize]
  elif field == 'title':
    boardList = Board.objects.filter(Q(title__contains=word)).order_by('-id')[start:start+pageSize]
  elif field == 'content':
    boardList = Board.objects.filter(Q(content__contains=word)).order_by('-id')[start:start+pageSize]
  else :
    boardList = Board.objects.all().order_by('-idx')[start:start+pageSize]

  context={'boardList':boardList,
           'boardCount':boardCount,
           'field':field,
           'word':word,
           'startPage':startPage,
           'endPage' : endPage,
           'totPage' : totPage,
           'blockPage':blockPage,
           'range' : range(startPage,endPage+1),
           'currentPage' : currentPage}
  
  return render(request,'board/boardlist.html',context)

#board detail
def detail(request, board_id):
  board = Board.objects.get(id = board_id)
  board.hit_up()
  board.save()
  return render(request,'board/detail.html',{'board':board})

#list_page
def list_page(request):
  page = request.GET.get('page',1)
  word = request.GET.get('word','')

  boardCount = Board.objects.filter(
    Q(writer__contains = word)|
    Q(title__contains = word)|
    Q(content__contains = word)).count()
  
  boardList = Board.objects.filter(
    Q(writer__contains = word)|
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
  return render(request, 'board/list_page.html', context)

#comment_insert
@csrf_exempt
def comment_insert(request):
  id = request.POST['board_id']
  comment = Comment(writer='aa', board_id = id,
                    content = request.POST['content'])
  comment.save()
  return redirect('/boards/'+id)