from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#세 가게만 각각 먼저 추천 -랜덤  ---db에 넣어놓으면 타입별로 구분 되고, 그중에 랜덤.
class Restaurant(models.Model):
    idx= models.AutoField(primary_key=True)
    dayimg= models.ImageField(null=True)
    name= models.CharField(max_length=20) #가게이름
    category= models.CharField(max_length=10)    #식당,술집,카페
    addr= models.CharField(max_length=50,default='등록되지 않음')
    phone= models.TextField(max_length=20 ,default='등록되지 않음')
    main= models.TextField(max_length=50, default='등록되지 않음')
    quantity= models.CharField(max_length=10)
    genre= models.CharField(max_length=10)
    qualperprice= models.CharField(max_length=10)
    dayornight= models.CharField(max_length=5)
    rmood= models.TextField(max_length=100)
    pmood= models.TextField(max_length=100)
    who= models.TextField(max_length=50)
    whenn= models.TextField(max_length=50)
    purpose= models.TextField(max_length=50) 

    def __str__(self):
        return str(self.idx)+self.name
        # return str(self.id)

#추천결과 평가점수 저장
class Voting(models.Model):
    question = models.CharField(max_length=100,null=True)
    result5= models.IntegerField(default=0)  #매우만족
    result4= models.IntegerField(default=0)
    result3= models.IntegerField(default=0)
    result2= models.IntegerField(default=0)
    result1= models.IntegerField(default=0)

    def __str__(self):
        return self.question

class Voting2(models.Model):
    question = models.CharField(max_length=100,null=True)
    score5= models.IntegerField(default=0)      #매우만족
    score4= models.IntegerField(default=0)
    score3= models.IntegerField(default=0)
    score2= models.IntegerField(default=0)
    score1= models.IntegerField(default=0)

    def __str__(self):
        return self.question