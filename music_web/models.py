# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class MUSIC(models.Model):
    song_name = models.CharField(max_length=200) # 歌名
    singer = models.CharField(max_length=200) # 歌手名
    frequency = models.CharField(max_length=200) # 频率
    mis_id = models.CharField(max_length=200) # 用户id
    star_id = models.CharField(max_length=200) # 唯一标识的id

    def __unicode__(self):
		  return self.song_name
     
    class Meta:
        managed = False
        db_table = 'music_web_weather'
    