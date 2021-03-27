from django.urls import path
from .views import login, register, kakaoLoginRedirect, kakaoLogin, kakaoLogout


urlpatterns = [
    path('login/', login , name="login"),
    path('register/', register, name="register"),
    path('kakao/login/', kakaoLogin, name="kakao"),   #name이 html {% url '' %}에 들어갈부분
    path('kakaoLoginRedirect/', kakaoLoginRedirect ),
    path('kakaoLogout/',kakaoLogout),
    # path('KakaoLoginCallbackView/', KakaoLoginCallbackView.as_view(), name="k")
]
