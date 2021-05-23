from django.shortcuts import render, get_object_or_404, redirect
from .models import Recommend
from django.contrib.auth.models import User
# from accounts.models import MyUser
from django.conf import settings
import random

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)

# @login_required
def gamseong(request,pk):
    user=request.user
    restaurant= Recommend.objects.all()
    #랜덤으로
    # 이거를 모델에 넣어서 pnu퀴즈처럼 꺼내는 느낌?!?or
    r_mood=['아기자기한', '힙한','어두운','이국적인','고급스러운']
    p_mood=['울적한','화나는','기분전환이 필요한','센치한','신나는']

    random_r_mood1 = random.choice(r_mood)
    r_mood.remove(random_r_mood1)  
    #변수로 넣으면 에러남 -> remove는 리턴값이 없기때문에 따로 변수x, 삭제된체로 r_mood리스트에 담김 
    print(r_mood)
    random_r_mood2 = random.choice(r_mood)
    r_mood.remove(random_r_mood2) 
    random_r_mood3 = random.choice(r_mood)
    print(r_mood)
    r_mood.remove(random_r_mood3)
    random_r_mood4 = random.choice(r_mood)

    random_p_mood1 = random.choice(p_mood)
    p_mood.remove(random_p_mood1)
    random_p_mood2 = random.choice(p_mood)
    p_mood.remove(random_p_mood2)
    random_p_mood3 = random.choice(p_mood)
    p_mood.remove(random_p_mood3)
    random_p_mood4 = random.choice(p_mood)

    

# r/p_mood에서 앞에 random_r_mood에 존재하면 리스트에서 빼내고 다음 랜덤 버튼엔 앞에꺼에서 없는 걸로 랜덤. 

    # 
    # if request.method=="POST":
        # 메인에서 추천할 각각의 가게들
    # if request.POST:        #각 input에 감성 submit했을때 나올 추천리스트 다르게
    #     if request.POST['gam1']:       #이렇게 하면 페이지 감정 수만큼 만들어야함,,
    #         return redirect("main")
    context={'restaurant':restaurant,"random_r_mood1":random_r_mood1,"random_r_mood2":random_r_mood2,"random_r_mood3":random_r_mood3,"random_r_mood4":random_r_mood4,"r_mood":r_mood,"random_p_mood1":random_p_mood1,"random_p_mood2":random_p_mood2,"random_p_mood3":random_p_mood3,"p_mood":p_mood}
    return render(request,'gamseong.html',context)

def main(request):
    restaurant= Recommend.objects.all()
    context={"restaurant":restaurant}
    return render(request,'main.html',context)

def main2(request):
    return render(request,'main2.html')