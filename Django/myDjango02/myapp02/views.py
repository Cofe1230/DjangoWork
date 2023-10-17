from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp02.models import Board

# Create your views here.

UPLOAD_DIR = 'C:/Users/it/Desktop/GitClone/DjangoWork/Django/upload/'

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
      
  return redirect("/write_form/")