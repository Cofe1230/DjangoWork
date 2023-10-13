from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from myapp01.models import Board
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
def list(request):
  boardList = Board.objects.all()
  context = {'boardList' : boardList}
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
  return render(request,'board/detail1.html',{'dto' : dto})

#delete
def delete(request, board_idx):
  #print(board_idx)
  Board.objects.get(idx=board_idx).delete()
  return redirect("/list/")