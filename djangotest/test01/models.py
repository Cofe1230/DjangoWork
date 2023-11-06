from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Board(models.Model):
  writer = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(null=False,max_length=200)
  content = models.TextField(null=False)
  hit = models.IntegerField(default=0)
  post_date = models.DateTimeField(default=datetime.now, blank=False)
  filename = models.CharField(null=True, blank=True, default='', max_length=500)
  filesize = models.IntegerField(default=0)
  down = models.ImageField(default=0)

  def hit_up(self):
    self.hit += 1
  
  def down_up(self):
    self.down +=1

class Comment(models.Model):
  board = models.ForeignKey(Board,on_delete=models.CASCADE)
  writer = models.CharField(null=False, max_length=50)
  content = models.TextField(null=False)
  post_date = models.DateTimeField(default=datetime.now, blank=False)
  
class Movie(models.Model):  
    # title, point, reserve
    title = models.CharField(null=False, max_length=500)
    point = models.FloatField(default=0.0)  
    reserve = models.FloatField(null=False,default=0.0) 

class Forecast(models.Model):  
    city = models.CharField(null=False, max_length=200)  
    tmef = models.TextField(null=True)
    wf = models.TextField(null=True)
    tmn = models.IntegerField(default=0)
    tmx = models.IntegerField(default=0)