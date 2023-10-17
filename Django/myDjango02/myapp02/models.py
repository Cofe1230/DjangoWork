from django.db import models
from datetime import datetime

# Create your models here.
class Board(models.Model):
  writer = models.CharField(null=False,max_length=50)
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