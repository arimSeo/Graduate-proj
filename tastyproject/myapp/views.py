from django.shortcuts import render, get_object_or_404, redirect
from .models import Recommend, ThreeRecommend
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
    # 각 cluster별 랜덤으로
    # 이거를 모델에 넣어서 pnu퀴즈처럼 꺼내는 느낌?!?or
    r_mood1=['어두운', '레트로', '빈티지한', '느낌있는', '외국감성']
    r_mood2=['정감있는', '깔끔한', '정갈한', '신선한', '깨끗한', '한국감성', '인도감성', '편한', '새로운']
    r_mood3=['이탈리아감성', '편안한', '비주얼좋은', '초코초코한', '뷰가좋은', '고급진', '개방감', '안락한', '크런키한']
    r_mood4=['독특한', '비쥬얼좋은']
    r_mood5=['집밥느낌', '모락모락한']
    r_mood6=['심플한', '우드톤', '귀여운', '은은한', '화이트톤의']
    r_mood7=['일본감성', '인테리어예쁜', '분위기좋은', '아늑한', '힐링', '태국감성', '하얀', '잔잔한']
    r_mood8=['전통있는', '중국감성', '다양한', '생기있는', '옛날의', '로컬의', '미묘한', '조그마한']

    p_mood1=['머리가복잡해','답답해','우울해', '기분전환', '행복해', '신나', '즐거워', '평온해', '무료해', '센치해', '지쳐', '에너지넘쳐']
    p_mood2=['만족스러워', '새로워', '설레', '감성터질때']
    p_mood3=['외로워', '귀찮아', '그리워']
    p_mood4=['화가나', '절망스러워']

    random_r_mood1 = random.choice(r_mood1)
    random_r_mood2 = random.choice(r_mood2)
    random_r_mood3 = random.choice(r_mood3)
    random_r_mood4 = random.choice(r_mood4)
    random_r_mood5 = random.choice(r_mood5)
    random_r_mood6 = random.choice(r_mood6)
    random_r_mood7 = random.choice(r_mood7)
    random_r_mood8 = random.choice(r_mood8)

    random_p_mood1 = random.choice(p_mood1)
    p_mood1.remove(random_p_mood1) 
    random_p_mood2 = random.choice(p_mood1)
    p_mood1.remove(random_p_mood2) 
    random_p_mood3 = random.choice(p_mood1)

    random_p_mood4 = random.choice(p_mood2)
    p_mood2.remove(random_p_mood4) 
    random_p_mood5 = random.choice(p_mood2)

    random_p_mood6 = random.choice(p_mood3)
    p_mood3.remove(random_p_mood6) 
    random_p_mood7 = random.choice(p_mood3)
    random_p_mood8 = random.choice(p_mood4)

# r/p_mood에서 앞에 random_r_mood에 존재하면 리스트에서 빼내고 다음 랜덤 버튼엔 앞에꺼에서 없는 걸로 랜덤. 
    # if request.method=="POST":
        # 메인에서 추천할 각각의 가게들
    # if request.POST:        #각 input에 감성 submit했을때 나올 추천리스트 다르게
    #     if request.POST['gam1']:   #이렇게 하면 페이지 감정 수만큼 만들???/xxxx main으로 각각 다보내면 되지않나???
    #         return redirect("main")
    context={"random_r_mood1":random_r_mood1,"random_r_mood2":random_r_mood2,"random_r_mood3":random_r_mood3,"random_r_mood4":random_r_mood4,"random_r_mood5":random_r_mood5,"random_r_mood6":random_r_mood6,"random_r_mood7":random_r_mood7,"random_r_mood8":random_r_mood8,"r_mood1":r_mood1,"r_mood2":r_mood2,"r_mood3":r_mood3,"r_mood4":r_mood4,"r_mood5":r_mood5,"r_mood6":r_mood6,"r_mood7":r_mood7,"r_mood8":r_mood8,"random_p_mood1":random_p_mood1,"random_p_mood2":random_p_mood2,"random_p_mood3":random_p_mood3,"random_p_mood4":random_p_mood4,"random_p_mood5":random_p_mood5,"random_p_mood6":random_p_mood6,"random_p_mood7":random_p_mood7,"random_p_mood8":random_p_mood8,"p_mood1":p_mood1,"p_mood2":p_mood2,"p_mood3":p_mood3,"p_mood4":p_mood4}
    return render(request,'gamseong.html',context)

def main(request):
    restaurant= ThreeRecommend.objects.all()
    # 일단 타입별로 모델에서 다불러오고(filter) <-이거는 db로 자동 알고리즘 돌려서 id값이나 이름으로 불러서! 
    food=ThreeRecommend.objects.filter(r_type="식당")
    cafe=ThreeRecommend.objects.filter(r_type="카페")
    alchol=ThreeRecommend.objects.filter(r_type="술집")
    # 식당, 카페, 술집 각각의 모델??? 아님 filter(r_type="카페")인거를 각각!
    context={"restaurant":restaurant,"food":food,"cafe":cafe,"alchol":alchol}
    return render(request,'main.html',context)

def main2(request):
    restaurant2= Recommend.objects.all()
    food2= Recommend.objects.filter(r_type='식당')
    cafe2= Recommend.objects.filter(r_type='카페')
    alchol2= Recommend.objects.filter(r_type='술집')
    context={"restaurant2":restaurant2,"food2":food2,"cafe2":cafe2,"alchol2":alchol2}
    return render(request,'main2.html',context)