import datetime
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title_text = models.CharField(max_length=100) # 제목 -> 옵션 찾아보고 변경가능
    content_text = models.CharField(max_length=1000) # 내용 -> 옵션 찾아보고 변경가능
    pub_date = models.DateTimeField(auto_now_add=True) # 자동으로 오늘 날짜로 생성 -> 옵션 찾아보고 변경가능
    
    def __str__(self):
        return self.title_text