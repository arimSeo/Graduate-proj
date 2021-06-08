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


# 전체에서 감성기반 추천 
# class Recommend(models.Model):
#     rlist= models.ForeignKey(RestaurantList,on_delete=models.CASCADE)
#     # idx로 이름 
#     def __str__(self):
#         return str(self.rlist)

# 전체 가게 테이블(모델) -> 칼럼: 사진, 가게이름, 가게종류(식당/술집/카페)
# 식당만/카페만/술집만 모델 -> 칼럼: 사진, 가게이름

