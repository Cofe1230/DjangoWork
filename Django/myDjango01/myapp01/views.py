from django.shortcuts import render,redirect
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from myapp01.models import Board,Comment


import urllib.parse
import math

# Create your views here.

#upload 경로
UPLOAD_DIR = 'C:/Users/it/Desktop/GitClone/DjangoWork/Django/upload/'

#write_form
def write_form(request):
  return render(request,'board/write.html')

#insert
@csrf_exempt #csrf 사용안함
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
      
  return redirect("/list/")

#list 전체보기(기본)
# def list(request):
#   boardList = Board.objects.all()
#   boardCount = Board.objects.count
#   context = {'boardList' : boardList,'boardCount':boardCount}
#   return render(request,'board/list.html',context)

def list(request):
  page = request.GET.get('page',1)
  word = request.GET.get('word','')
  field = request.GET.get('field','title')

  #count
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
                                      Q(writer__contains=word)).order_by('-idx')[start:start+pageSize]
  elif field == 'write':
    boardList = Board.objects.filter(Q(writer__contains=word)).order_by('-idx')[start:start+pageSize]
  elif field == 'title':
    boardList = Board.objects.filter(Q(title__contains=word)).order_by('-idx')[start:start+pageSize]
  elif field == 'content':
    boardList = Board.objects.filter(Q(content__contains=word)).order_by('-idx')[start:start+pageSize]
  else :
    boardList = Board.objects.all().order_by('-idx')[start:start+pageSize]

  context={'boardList':boardList,
           'boardCount':boardCount,
           'startPage':startPage,
           'endPage' : endPage,
           'totPage' : totPage,
           'blockPage':blockPage,
           'range' : range(startPage,endPage+1),
           'currentPage' : currentPage}
  
  return render(request,'board/list.html',context)

#detail_idx 상세보기
def detail_idx(request):
  id = request.GET['idx']
  #print('id : ', id)
  dto = Board.objects.get(idx=id)
  dto.hit_up()
  dto.save()
  return render(request,'board/detail.html',{'dto' : dto})

#detail
def detail(request, board_idx):
  print('board_idx : ', board_idx)
  dto = Board.objects.get(idx=board_idx)
  dto.hit_up()
  dto.save()
  #Comment List
  commentList = Comment.objects.filter(board_idx = board_idx).order_by('-idx') #내림차순 정렬
  commentCnt = Comment.objects.filter(board_idx = board_idx).count
  print('comment sql : ',commentList.query)
  print('commentCnt : ', commentCnt)
  return render(request,'board/detail1.html',{'dto' : dto,
                                              'commentList' : commentList,
                                              'commentCnt':commentCnt})

#delete
def delete(request, board_idx):
  #print(board_idx)
  Board.objects.get(idx=board_idx).delete()
  return redirect("/list/")

#download_count
def download_count(request):
  id = request.GET['idx']
  #print(id)
  dto = Board.objects.get(idx = id)
  dto.down_up() # 다운로드 수 증가
  dto.save()
  count = dto.down #다운로드 수
  #print ("count : ", count)
  return JsonResponse({'idx':id,'count':count})

#downlaod
def download(request):
  id = request.GET['idx']
  dto = Board.objects.get(idx = id)
  path = UPLOAD_DIR + dto.filename
  #한글일 경우 파싱
  #filename = urllib.parse.quote(dto.filename)
  filename = dto.filename

  with open(path, 'rb') as file:
    response = HttpResponse(file.read(),content_type='applicaiton/octet-stream')
    response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(filename)
  
  return response

#update_form
def update_form(request,board_idx):
  dto = Board.objects.get(idx=board_idx)
  return render(request,'board/update.html',{'dto' : dto})

#update
@csrf_exempt
def update(request) : 
  id = request.POST['idx']
  dto = Board.objects.get(idx=id)

  #파일 업로드
  fname = dto.filename
  fsize = dto.filesize

  #file 수정
  if 'file' in request.FILES:
    file = request.FILES['file']
    fsize = file.size
    fname = file.name
    fp = open('%s%s' %(UPLOAD_DIR,fname),'wb')
    for chunk in file.chunks():
      fp.write(chunk)
    fp.close()

  dto_update = Board(id,
                    writer=request.POST['writer'],
                    title = request.POST['title'],
                    content = request.POST['content'],
                    filename = fname,
                    filesize = fsize,)
  dto_update.save()

  return redirect("/list/") 

#comment_insert
@csrf_exempt
def comment_insert(request):
  id = request.POST['idx']
  dto = Comment(board_idx = id,
                writer = 'aa',
                content = request.POST['content'])
  dto.save()
  #return redirect("detail_idx/?idx="+id)
  return redirect("/detail/"+id)