from django.shortcuts import render, get_object_or_404, redirect
from .models import Recommend
from django.contrib.auth.models import User
# from accounts.models import MyUser
from django.conf import settings

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)

# @login_required
def gamseong(request,pk):
    restaurant= Recommend.objects.all()
    # if request.method=="POST":
        # 메인에서 추천할 각각의 가게들
    if request.POST:        #각 input에 감성 submit했을때 나올 추천리스트 다르게
        if request.POST['gam1']:       #이렇게 하면 페이지 감정 수만큼 만들어야함,,
            return redirect("main")
    return render(request,'gamseong.html',{'restaurant':restaurant})

def main(request):
    return render(request,'main.html')

def main2(request):
    return render(request,'main2.html')