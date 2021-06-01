from django.shortcuts import render, get_object_or_404, redirect
from .models import RestaurantList
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
def gamseong(request):
    user=request.user
    print(user)
    # 각 cluster별 랜덤으로
    # 이거를 모델에 넣어서 pnu퀴즈처럼 꺼내는 느낌?!?or
    r_mood1=['소소한', '정갈한', '건강한', '가벼운', '알록달록한', '부드러운']
    r_mood2=['숨은', '이탈리아감성', '루프탑', '벨기에감성']
    r_mood3=['고급스러운', '어두운', '비쥬얼좋은', '빈티지한']
    r_mood4=['푸짐한', '다이어트', '진짜의', '유명한', '학생감성', '복잡한', '소박한']
    r_mood5=['따뜻한', '아늑한', '포근한', '아담한', '감성있는', '뷰가좋은', '캐쥬얼한']
    r_mood6=['동남아감성', '활기찬', '신기한']
    r_mood7=['예쁜', '빛나는', '사랑스러운', '클래식한', '청량한', '잔잔한', '베이지톤의']
    r_mood8=['오래된', '옛날의', '시끄러운']

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
    p_mood1.remove(random_p_mood3) 
    random_p_mood7 = random.choice(p_mood1)

    random_p_mood4 = random.choice(p_mood2)
    p_mood2.remove(random_p_mood4) 
    random_p_mood5 = random.choice(p_mood2)
    random_p_mood6 = random.choice(p_mood3)
    random_p_mood8 = random.choice(p_mood4)

# r/p_mood에서 앞에 random_r_mood에 존재하면 리스트에서 빼내고 다음 랜덤 버튼엔 앞에꺼에서 없는 걸로 랜덤. 
    # if request.method=="POST":
        # 메인에서 추천할 각각의 가게들
    if request.POST:                #각 input에 감성 submit했을때 나올 추천리스트 다르게
        gam=request.POST['gam']     #이렇게 하면 페이지 감정 수만큼 만들???/xxxx main으로 각각 다보내면 되지않나???
        return render(request, 'main.html',{'gam':gam} )
    context={"random_r_mood1":random_r_mood1,"random_r_mood2":random_r_mood2,"random_r_mood3":random_r_mood3,"random_r_mood4":random_r_mood4,"random_r_mood5":random_r_mood5,"random_r_mood6":random_r_mood6,"random_r_mood7":random_r_mood7,"random_r_mood8":random_r_mood8,"r_mood1":r_mood1,"r_mood2":r_mood2,"r_mood3":r_mood3,"r_mood4":r_mood4,"r_mood5":r_mood5,"r_mood6":r_mood6,"r_mood7":r_mood7,"r_mood8":r_mood8,"random_p_mood1":random_p_mood1,"random_p_mood2":random_p_mood2,"random_p_mood3":random_p_mood3,"random_p_mood4":random_p_mood4,"random_p_mood5":random_p_mood5,"random_p_mood6":random_p_mood6,"random_p_mood7":random_p_mood7,"random_p_mood8":random_p_mood8,"p_mood1":p_mood1,"p_mood2":p_mood2,"p_mood3":p_mood3,"p_mood4":p_mood4}
    return render(request,'gamseong.html',context)

def main(request):
    restaurant= RestaurantList.objects.all()
    # 일단 타입별로 모델에서 다불러오고(filter) <-이거는 db로 자동 알고리즘 돌려서 id값이나 이름으로 불러서! 
    food=RestaurantList.objects.filter(category="식당")
    cafe=RestaurantList.objects.filter(category="카페")
    alchol=RestaurantList.objects.filter(category="술집")
    # 감성value받아서 키워드 유사 + (감성이름을 pk로-그럼 모델만들어야하나,,)
    # 식당, 카페, 술집 각각의 모델??? 아님 filter(r_type="카페")인거를 각각!
    context={"restaurant":restaurant,"food":food,"cafe":cafe,"alchol":alchol}
    return render(request,'main.html',context)

def main2(request):
    restaurant2= RestaurantList.objects.all()
    # food2= RestaurantList.objects.filter(r_type='식당')
    # cafe2= RestaurantList.objects.filter(r_type='카페')
    # alchol2= RestaurantList.objects.filter(r_type='술집')
    context={"restaurant2":restaurant2}
    return render(request,'main2.html',context)