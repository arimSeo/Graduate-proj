from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import os, json
from django.views import View
import requests
from django.http import HttpResponse, JsonResponse
# from tastyproject.settings import KAKAO_KEY
# import main_domain
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
# from myapp.models import Recommend
from django.conf import settings


# def login(request):
#     context={}
#     username=request.POST["username"]
#     password=request.POST["password1"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request,user)
#         return redirect('gamseong',user.pk)
#     else:
#         context['message']="잘못된 아이디/비밀번호 입니다."
#         return render(request, 'registration/login.html', context)

# def login(request):
#     return render(request, 'login.html')

def register(request):
    context={}
    register_form=RegisterForm()
    #추가할것!
    #성별 폼 띄우기ㅇㅇㅇㅇ완료
    #비번 일치안하면 오류 띄우기 ㅇㅇㅇㅇㅇㅇㅇㅇ완료
    #아이디 같은거 있음 오류뜸-예외처리
    # username=MyUser.objects.all()
    if request.method=="POST":
        # register_form=RegisterForm(request.POST)
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            profile = MyUser(
                user=user,
                name=request.POST["username"],
                birth=request.POST["birthday"],
                gender=request.POST["gender"],
                permit=request.POST.get('ispermit', '') == 'on')
            profile.save() 
            # 회원가입 성공! 메시지띄우고 로그인 하도록
            return redirect('accounts:login')
        else:
            message="✔ 비밀번호가 일치하지 않습니다."
            context= {'message':message,'register_form':register_form}
            return render(request,'registration/register.html',context)
    else:
        return render(request,'registration/register.html',{'register_form':register_form})


###
#소셜로그인

def kakaoLogin(request):
    # _restApiKey = settings.KAKAO_REST_API_KEY # 입력필요
    _restApiKey='81c8ef79f775f47d6e2cc9c8eef60de8'
    _redirectUrl = 'http://127.0.0.1:8000/gamseong/'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginRedirect(request):
    _qs = request.GET['code']
    # _restApiKey = os.settings.get.KAKAO_REST_API_KEY # 입력필요
    _restApiKey='81c8ef79f775f47d6e2cc9c8eef60de8'
    _redirect_uri = 'http://127.0.0.1:8000/gamseong/'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = request.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'in.html',{"_restApiKey":_restApiKey})


def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    # _url = 'https://kapi.kakao.com/v1/user/unlink'
    # _header = {
    #   'Authorization': f'bearer {_token}',
    # }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'login.html')
    else:
        return render(request, 'error.html')



# def kakao_login(request):
#     app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
#     # redirect_uri = "http://127.0.0.1:8000/" + "users/login/kakao/callback"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={'http://127.0.0.1:8000/'}&response_type=code"
#     )
    




# class KakaoLoginView(View):
#     def get(self, request):
#         code=request.GET.get('code',None)
#         redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback"
#         return redirect(
#             f"https://kauth.kakao.com/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code"
#         )


# class KakaoSignInCallbackView(View):
#     def get(self, request):
#         try:
#             authorize_code = request.GET.get("code")
#             app_key = ""
#             redirect_uri = "http://127.0.0.1:8000/"

#             token_request = requests.get(
#                 f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_key}&redirect_uri={redirect_uri}&code={authorize_code}"
#             )

#             token_json = token_request.json()
#             error = token_json.get("error", None)

#             if error is not None:
#                 return JsonResponse({"message": "INVALID_CODE"}, status=400)

#             access_token = token_json.get("access_token")

#             return JsonResponse({'access_token': access_token}, status=200)

#         except KeyError:
#             return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

#         except access_token.DoesNotExist:
#             return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

 