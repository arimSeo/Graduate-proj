from django.db import models
from django.contrib.auth.models import User
# from accounts.models import MyUser
from django.conf import settings

#세 가게를 각각 먼저 추천
class Recommend(models.Model):
    # user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    photos=models.ImageField()
    r_name=models.CharField(max_length=20) #가게이름
    r_type= models.CharField(max_length=5) #식당,술집,카페

    # food= models.CharField(max_length=20) #식당이름
    # cafe= models.CharField(max_length=20)  #카페이름
    # drink= models.CharField(max_length=20)  #술집이름
    def __str__(self):
        return str(self.r_name)

# 전체 가게 테이블(모델) -> 칼럼: 사진, 가게이름, 가게종류(식당/술집/카페)
# 식당만/카페만/술집만 모델 -> 칼럼: 사진, 가게이름
# 

