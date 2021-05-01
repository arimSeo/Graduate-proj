from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# pitapet에서 UserLocation 모델 참고
class UserCheck(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    #1. on_delete=models.CASCADE: OneToOneField가 바라보는 값이 삭제될 때 OneToOneField를 포함하는 모델 인스턴스(row)도 삭제된다.
    #2. One-to-one 모델의 역참조는 하나의 객체(single object) 를 반환하지만, 
    # ForeignKey의 역참조는 QuerySet 을 반환
    # 1명의 유저는 하나의 프로필만을 가져야 한다고 강제한다면, one-to-one을 사용할 수 있다.
    ispermit= models.BooleanField('',default=False)  #정보수집 동의체크
