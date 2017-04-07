
from django.db import models

class Article(models.Model):
    title = models.CharField(u'標題', max_length=256)
    content = models.TextField(u'大概')
 
    pub_date = models.DateTimeField(u'發表時間', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新時間',auto_now=True, null=True)
    
class Person(models.Model):
    first_name = models.CharField(u'姓氏',max_length=30)
    last_name = models.CharField(u'名字',max_length=30)
    
    
    
    
class Ubike(models.Model):
    sno = models.CharField(primary_key=True,max_length=20)
    sna = models.CharField('站名',max_length=20)
    sarea = models.CharField('區域',max_length=20)
    lat = models.CharField('緯度',max_length=30)
    lng = models.CharField('經度',max_length=30)
    ar = models.CharField('位置',max_length=30)
    sareaen = models.CharField('區域英文',max_length=30)
    snaen = models.CharField('站名英文',max_length=30)
    aren = models.CharField('位置英文',max_length=30)
