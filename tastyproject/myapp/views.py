from django.shortcuts import render, get_object_or_404
from .models import Recommand
from django.contrib.auth.models import User

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)

# @login_required
def gamseong(request):
    # user = get_object_or_404(User)
    # all_user= User.objects.all()
    # myuser= User.objects.get(user=request.user)
    # return render(request,'gamseong.html',{'all_user':all_user,'myuser':myuser})
    restaurant= Recommand.objects.all()
    # if request.method=="POST":
        # 메인에서 추천할 각각의 가게들
    return render(request,'gamseong.html')

def main(request):
    return render(request,'main.html')