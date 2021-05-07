from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recommand(models.Model):
    photos=models.ImageField()
    #세 가게를 각각 먼저 추천
    food= models.CharField(max_length=20) #식당이름
    cafe= models.CharField(max_length=20)  #카페이름
    drink= models.CharField(max_length=20)  #술집이름

