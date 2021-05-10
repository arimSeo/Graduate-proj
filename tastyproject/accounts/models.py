from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from myapp.models import Recommend
from django.conf import settings
#테이블을 만드는것! User는 장고 기존 유저, 새 유저를 만들려면 모델 추가
class MyUser(models.Model):
    M_or_F = (
        ('남', '남'),
        ('여', '여'),
        ('중성', '중성'),
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=False)
    #1. on_delete=models.CASCADE: OneToOneField가 바라보는 값이 삭제될 때 OneToOneField를 포함하는 모델 인스턴스(row)도 삭제된다.
    #2. One-to-one 모델의 역참조는 하나의 객체(single object) 를 반환하지만, 
    # ForeignKey의 역참조는 QuerySet 을 반환
    # 1명의 유저는 하나의 프로필만을 가져야 한다고 강제한다면, one-to-one을 사용할 수 있다.
    name = models.CharField(max_length=20,default=False)
    birth= models.DateField(null=True)
    gender=models.CharField( choices=M_or_F, max_length=2, null=True)
    permit = models.BooleanField(default=False)      #정보수집 동의체크
    
    def __str__(self):         #모델 클래스 객체의 문자열 표현 반환
        return str(self.user)   #admin페이지에서 user 해당 문자열로 뜸