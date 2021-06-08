from django.urls import path
from django.conf.urls.static import static
from .views import login, register, kakaoLoginRedirect, kakaoLogin, kakaoLogout,kakaoLoginRedirect
from django.contrib.auth import views as auth_views  #auth_views라고 이름->장고에 있는 기존 LoginView이용함

app_name='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view() ,name="login"),   
    #registeration폴더안에 template 안넣고 하기위해 위( template_name='accounts/login.html')안 처럼 accounts앱 디렉터리에서 login.html 파일을 참조하게 한다.
    path('register/', register, name="register"),
    path('kakao/login/', kakaoLogin, name="kakao"),   #name이 html {% url '' %}에 들어갈부분
    path('kakaoLoginRedirect/', kakaoLoginRedirect ),
    path('kakaoLogout/',kakaoLogout),
    # path('KakaoLoginCallbackView/', KakaoLoginCallbackView.as_view(), name="k")
]
