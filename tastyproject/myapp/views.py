from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
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
    r_mood1=['힙한', '레트로감성', '음악이있는', '트렌디한', '세련된']
    r_mood2=['귀여운', '밝은', '아기자기한한', '러블리한', '화이트톤']
    r_mood3=['따뜻한', '정갈한', '아담한', '일본감성', '아늑한', '도란도란']
    r_mood4=['친절한', '쾌적한', '심플한', '편한', '즐거운', '색다른']
    r_mood5=['정감있는', '전통있는', '옛날의']
    r_mood6=['시끌벅적한', '활기찬', '그리운']
    r_mood7=['청결한', '새로운', '소담한', '건강한']
    r_mood8=['모던한', '감각적인', '주택개조']

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

    # if request.method=="POST":
        # 메인에서 추천할 각각의 가게들
    # if request.POST:                #각 input에 감성 submit했을때 나올 추천리스트 다르게
    #     gam=request.POST['gam']
    #     return render(request, 'main.html',{'gam':gam})

    context={"random_r_mood1":random_r_mood1,"random_r_mood2":random_r_mood2,"random_r_mood3":random_r_mood3,"random_r_mood4":random_r_mood4,"random_r_mood5":random_r_mood5,"random_r_mood6":random_r_mood6,"random_r_mood7":random_r_mood7,"random_r_mood8":random_r_mood8,"r_mood1":r_mood1,"r_mood2":r_mood2,"r_mood3":r_mood3,"r_mood4":r_mood4,"r_mood5":r_mood5,"r_mood6":r_mood6,"r_mood7":r_mood7,"r_mood8":r_mood8,"random_p_mood1":random_p_mood1,"random_p_mood2":random_p_mood2,"random_p_mood3":random_p_mood3,"random_p_mood4":random_p_mood4,"random_p_mood5":random_p_mood5,"random_p_mood6":random_p_mood6,"random_p_mood7":random_p_mood7,"random_p_mood8":random_p_mood8,"p_mood1":p_mood1,"p_mood2":p_mood2,"p_mood3":p_mood3,"p_mood4":p_mood4}
    return render(request,'gamseong.html',context)

# test용 -감성키워드 선택/전달~~추천알고리즘
#1. json으로 띄우기!!!!!!!!!!!!!!!!!!!
#2. 감성 request 전달 받아서 연결!!!!!!!!!(html상 문제다-파라미터 받기)
from . import testAPI
def test(request):
    r_keyword='인테리어예쁜'
    result= testAPI.find_sim_rest(r_keyword)  #result1,2로 각각 r/pmood알고리즘

    return render(request, 'test.html',{'result':result})

##
from . import recommend_r, recommend_p
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# def main(request,rest_id):
def main(request):
    restaurant= Restaurant.objects.all()
    # rest= Restaurant.objects.get(id=rest_id)
    # idx=Recommend.objects.filter(rest_id=rest_id)

    # r_gam이면~/p_gam이면~ ->form두개로!!!!
    context = dict()
    # resultCafe={}
    # resultFood={}
    # resultBar={}
    try: 
        r_keyword=request.POST['r_gam']
        print(r_keyword)
        r_result= recommend_r.find_sim_rest(r_keyword) #df형식은 못가져와!!->json으로 
        context['r_keyword']=r_keyword
        context['r_result']=r_result

        # 랜덤 선택 3개
        # 3개를 리스트나 딕셔너리에 추가
        # 해당 객체를 context로 템플리스오 전송
        # 템플릿에서 해당 객체의 인덱스나 키를 사용해서 추출
        # 화면에 출력

        for i,v in r_result.items():    #items() : object받음
            # resultCafe[v["name"]] = {'이름': v["name"] , '종류':v["category"], '사진':v["dayimg"]}
            place_name =v['name']      #키값이 중복되서 마지막 애만 뜸.
            p_category =v['category']
            p_img= v['dayimg']
            p_genre=v['genre']
        
        # context['resultCafe']=resultCafe
        context['place_name']=place_name
        context['p_category']=p_category
        context['p_img']=p_img
        context['p_genre']=p_genre
    except: 
        p_keyword=request.POST['p_gam']
        print(p_keyword)
        p_result= recommend_p.find_sim_rest(p_keyword)
        context['p_keyword']=p_keyword
        context['p_result']=p_result

        for i,v in p_result.items():    #items() : object받음
            # resultCafe[v["name"]] = {'이름': v["name"] , '종류':v["category"], '사진':v["dayimg"]}
            place_name =v['name']      #키값이 중복되서 마지막 애만 뜸.
            p_category =v['category']
            p_img= v['dayimg']
            p_genre=v['genre']
            #이미지 필드 가져오는거 여기서 모델에서 가져와서 연결-이미지 미디어가 있는 주소
        
        # context['resultCafe']=resultCafe
        context['place_name']=place_name
        context['p_category']=p_category
        context['p_img']=p_img
        context['p_genre']=p_genre

        print(v["name"], v["category"], v['dayimg'])

    #키-value로 받아서 뷰에서 변수로 넣고 html에서 input에 {{식당name}}로 받아서 그다음에 전달-감성키워드처럼
   
    return render(request,'main.html',context)

from . import recommend_main2
def main2(request):
    restaurant2= Restaurant.objects.all()
    # restaurant1=get_object_or_404(Restaurant,idx=idx)

    if request.POST:
        place_name=request.POST['place_name']
    recommend_list= recommend_main2.find_sim_rest(place_name,11)

   
    context={"restaurant2":restaurant2,"place_name":place_name, "recommend_list":recommend_list}
    return render(request,'main2.html',context)


def detail(request):
    detail_contents=Restaurant.objects.all()
    # detail_contents=Restaurant.objects.get(idx=idx)
    return render(request,'detail.html')