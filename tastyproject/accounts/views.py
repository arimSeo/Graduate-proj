from django.conf import settings
from django.shortcuts import render, redirect
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


def register(request):
    # register_form=UserCreationForm()   #유저생성폼을 만든다
    # my_user=User.objects.get(user=request.user)
    # user_form=MyUser(instance=my_user)
    #추가할것!
    #성별 폼 띄우기
    #비번 일치안하면 오류 띄우기 -예외처리
    #아이디 같은거 있음 오류뜸-예외처리
    if request.method=="POST":
        if request.POST["password1"] == request.POST["password2"]:
            # username = request.POST['username']
            # password = request.POST['password1']
            # try:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            profile = MyUser(
                user=user,
                name=request.POST["username"],
                birth=request.POST["birthday"],
                permit=request.POST.get('ispermit', '') == 'on')
            profile.save()
            return redirect('gamseong')
                # user = User(username=username)
                # user.set_password(password)
                # user.save()
                
                # login(request,user)
                # return redirect('gamseong')
            # except:
            #     message = '존재하는 아이디입니다.'
            #     context['message'] = message      #context정의안됬다고 에러뜸
            #     return redirect('register')
    else:
        return render(request,'registration/register.html')
        # return render(request,'registration/register.html',{'user_form':user_form,'my_user':my_user})


###
#소셜로그인
def kakaoLogin(request):
    _restApiKey = settings.KAKAO_REST_API_KEY # 입력필요

    _redirectUrl = 'http://127.0.0.1:8000/'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginRedirect(request):
    _qs = request.GET['code']
    _restApiKey = settings.KAKAO_REST_API_KEY # 입력필요
   
    _redirect_uri = 'http://127.0.0.1:8000/'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 's.html')


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

 