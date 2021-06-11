from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Voting, Voting2
from django.contrib.auth.models import User
from django.conf import settings
import random

def index(request):
    return render(request, 'index.html')

# @login_required
def gamseong(request):
    user=request.user
    print(user)
    # 각 cluster별 랜덤으로
    r_mood1=['힙한', '레트로감성', '음악이있는', '트렌디한', '세련된']
    r_mood2=['귀여운', '밝은', '아기자기한한', '러블리한']
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

    context={"random_r_mood1":random_r_mood1,"random_r_mood2":random_r_mood2,"random_r_mood3":random_r_mood3,
    "random_r_mood4":random_r_mood4,"random_r_mood5":random_r_mood5,"random_r_mood6":random_r_mood6,"random_r_mood7":random_r_mood7,
    "random_r_mood8":random_r_mood8,"r_mood1":r_mood1,"r_mood2":r_mood2,"r_mood3":r_mood3,"r_mood4":r_mood4,"r_mood5":r_mood5,
    "r_mood6":r_mood6,"r_mood7":r_mood7,"r_mood8":r_mood8,"random_p_mood1":random_p_mood1,"random_p_mood2":random_p_mood2,
    "random_p_mood3":random_p_mood3,"random_p_mood4":random_p_mood4,"random_p_mood5":random_p_mood5,"random_p_mood6":random_p_mood6,
    "random_p_mood7":random_p_mood7,"random_p_mood8":random_p_mood8,
    "p_mood1":p_mood1,"p_mood2":p_mood2,"p_mood3":p_mood3,"p_mood4":p_mood4}
    return render(request,'gamseong.html',context)

#test용
from . import testAPI
def test(request):
    r_keyword='인테리어예쁜'
    result= testAPI.find_sim_rest(r_keyword)  #result1,2로 각각 r/pmood알고리즘
    return render(request, 'test.html',{'result':result})

### 감성키워드 선택/전달~~추천알고리즘
#1. json으로 띄우기!!
#2. 감성 request 전달 받아서 연결
#3. 랜덤 선택 3개
    # 3개를 리스트나 딕셔너리에 추가
    # 해당 객체를 context로 템플릿으로 전송
    # 템플릿에서 해당 객체의 인덱스나 키를 사용해서 추출
    # 화면에 출력
from . import recommend_r, recommend_p
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def main(request):
    three={}
    try: 
        r_keyword=request.POST['r_gam']
        print(r_keyword)
        r_result= recommend_r.find_sim_rest(r_keyword) #df형식은 못가져와!!->json으로 
        three= random.sample(list(r_result.values()),3)     #json추천결과 중 랜덤으로 3개
        # print(three)    #리스트로 싸여있음->[index]로 뽑아야함!
        # print(three[0])
        #box1
        name1 =three[0]['name']
        category1 =three[0]['category']
        img1 =three[0]['dayimg']
        genre1 =three[0]['genre']
        addr1 =three[0]['addr']
        phone1 =three[0]['phone']
        rmood1 =three[0]['rmood']
        dayornight1 =three[0]['dayornight']
        #box2
        name2 =three[1]['name']
        category2 =three[1]['category']
        img2 =three[1]['dayimg']
        genre2 =three[1]['genre']
        addr2 =three[1]['addr']
        phone2 =three[1]['phone']
        rmood2 =three[1]['rmood']
        dayornight2 =three[1]['dayornight']
        #box3
        name3 =three[2]['name']
        category3 =three[2]['category']
        img3 =three[2]['dayimg']
        genre3 =three[2]['genre']
        addr3 =three[2]['addr']
        phone3 =three[2]['phone']
        rmood3 =three[2]['rmood']
        dayornight3 =three[2]['dayornight']

        context={'r_keyword':r_keyword,'r_result':r_result,
        'name1':name1,'category1':category1,'img1':img1,'genre1':genre1,'addr1':addr1,'phone1':phone1,'rmood1':rmood1,'dayornight1':dayornight1,
        'name2':name2,'category2':category2,'img2':img2,'genre2':genre2,'addr2':addr2,'phone2':phone2,'rmood2':rmood2,'dayornight2':dayornight2,
        'name3':name3,'category3':category3,'img3':img3,'genre3':genre3,'addr3':addr3,'phone3':phone3,'rmood3':rmood3,'dayornight3':dayornight3}

    except: 
        p_keyword=request.POST['p_gam']
        print(p_keyword)
        p_result= recommend_p.find_sim_rest(p_keyword)
        three= random.sample(list(p_result.values()),3)     #json추천결과 중 랜덤으로 3개
        #box1
        name1 =three[0]['name']
        category1 =three[0]['category']
        img1 =three[0]['dayimg']
        genre1 =three[0]['genre']
        addr1 =three[0]['addr']
        phone1 =three[0]['phone']
        rmood1 =three[0]['rmood']
        dayornight1 =three[0]['dayornight']
        #box2
        name2 =three[1]['name']
        category2 =three[1]['category']
        img2 =three[1]['dayimg']
        genre2 =three[1]['genre']
        addr2 =three[1]['addr']
        phone2 =three[1]['phone']
        rmood2 =three[1]['rmood']
        dayornight2 =three[1]['dayornight']
        #box3
        name3 =three[2]['name']
        category3 =three[2]['category']
        img3 =three[2]['dayimg']
        genre3 =three[2]['genre']
        addr3 =three[2]['addr']
        phone3 =three[2]['phone']
        rmood3 =three[2]['rmood']
        dayornight3 =three[2]['dayornight']

        context={'p_keyword':p_keyword,'p_result':p_result,
        'name1':name1,'category1':category1,'img1':img1,'genre1':genre1,'addr1':addr1,'phone1':phone1,'rmood1':rmood1,'dayornight1':dayornight1,
        'name2':name2,'category2':category2,'img2':img2,'genre2':genre2,'addr2':addr2,'phone2':phone2,'rmood2':rmood2,'dayornight2':dayornight2,
        'name3':name3,'category3':category3,'img3':img3,'genre3':genre3,'addr3':addr3,'phone3':phone3,'rmood3':rmood3,'dayornight3':dayornight3}
    
    return render(request,'main.html',context)



from . import recommend_main2
def main2(request):
    if request.POST:
        place_name=request.POST['place_name']
    recommend_list= recommend_main2.find_sim_rest(place_name,11)
    topten= list(recommend_list.values()) 
    # print(topten)

    #box1
    name1 =topten[1]['name']
    category1 =topten[1]['category']
    img1 =topten[1]['dayimg']
    genre1 =topten[1]['genre']
    addr1 =topten[1]['addr']
    phone1 =topten[1]['phone']
    rmood1 =topten[1]['rmood']
    dayornight1 =topten[1]['dayornight']
    #box2
    name2 =topten[2]['name']
    category2 =topten[2]['category']
    img2 =topten[2]['dayimg']
    genre2 =topten[2]['genre']
    addr2 =topten[2]['addr']
    phone2 =topten[2]['phone']
    rmood2 =topten[2]['rmood']
    dayornight2 =topten[2]['dayornight']
    #box3
    name3 =topten[3]['name']
    category3 =topten[3]['category']
    img3 =topten[3]['dayimg']
    genre3 =topten[3]['genre']
    addr3 =topten[3]['addr']
    phone3 =topten[3]['phone']
    rmood3 =topten[3]['rmood']
    dayornight3 =topten[3]['dayornight']
    #box4
    name4 =topten[4]['name']
    category4 =topten[4]['category']
    img4 =topten[4]['dayimg']
    genre4 =topten[4]['genre']
    addr4 =topten[4]['addr']
    phone4 =topten[4]['phone']
    rmood4 =topten[4]['rmood']
    dayornight4 =topten[4]['dayornight']
    #box5
    name5 =topten[5]['name']
    category5 =topten[5]['category']
    img5 =topten[5]['dayimg']
    genre5 =topten[5]['genre']
    addr5 =topten[5]['addr']
    phone5 =topten[5]['phone']
    rmood5 =topten[5]['rmood']
    dayornight5 =topten[5]['dayornight']
    #box6
    name6 =topten[6]['name']
    category6 =topten[6]['category']
    img6 =topten[6]['dayimg']
    genre6 =topten[6]['genre']
    addr6 =topten[6]['addr']
    phone6 =topten[6]['phone']
    rmood6 =topten[6]['rmood']
    dayornight6 =topten[6]['dayornight']
    #box7
    name7 =topten[7]['name']
    category7 =topten[7]['category']
    img7 =topten[7]['dayimg']
    genre7 =topten[7]['genre']
    addr7 =topten[7]['addr']
    phone7 =topten[7]['phone']
    rmood7 =topten[7]['rmood']
    dayornight7 =topten[7]['dayornight']
    #box8
    name8 =topten[8]['name']
    category8 =topten[8]['category']
    img8 =topten[8]['dayimg']
    genre8 =topten[8]['genre']
    addr8 =topten[8]['addr']
    phone8 =topten[8]['phone']
    rmood8 =topten[8]['rmood']
    dayornight8 =topten[8]['dayornight']
    #box9
    name9 =topten[9]['name']
    category9 =topten[9]['category']
    img9 =topten[9]['dayimg']
    genre9 =topten[9]['genre']
    addr9 =topten[9]['addr']
    phone9 =topten[9]['phone']
    rmood9 =topten[9]['rmood']
    dayornight9 =topten[9]['dayornight']
    #box10
    name10 =topten[10]['name']
    category10 =topten[10]['category']
    img10 =topten[10]['dayimg']
    genre10 =topten[10]['genre']
    addr10 =topten[10]['addr']
    phone10 =topten[10]['phone']
    rmood10 =topten[10]['rmood']
    dayornight10 =topten[10]['dayornight']

    context={"place_name":place_name, "recommend_list":recommend_list,
    'name1':name1,'category1':category1,'img1':img1,'genre1':genre1,'addr1':addr1,'phone1':phone1,'rmood1':rmood1,'dayornight1':dayornight1,
    'name2':name2,'category2':category2,'img2':img2,'genre2':genre2,'addr2':addr2,'phone2':phone2,'rmood2':rmood2,'dayornight2':dayornight2,
    'name3':name3,'category3':category3,'img3':img3,'genre3':genre3,'addr3':addr3,'phone3':phone3,'rmood3':rmood3,'dayornight3':dayornight3,
    'name4':name4,'category4':category4,'img4':img4,'genre4':genre4,'addr4':addr4,'phone4':phone4,'rmood4':rmood4,'dayornight4':dayornight4,
    'name5':name5,'category5':category5,'img5':img5,'genre5':genre5,'addr5':addr5,'phone5':phone5,'rmood5':rmood5,'dayornight5':dayornight5,
    'name6':name6,'category6':category6,'img6':img6,'genre6':genre6,'addr6':addr6,'phone6':phone6,'rmood6':rmood6,'dayornight6':dayornight6,
    'name7':name7,'category7':category7,'img7':img7,'genre7':genre7,'addr7':addr7,'phone7':phone7,'rmood7':rmood7,'dayornight7':dayornight7,
    'name8':name8,'category8':category8,'img8':img8,'genre8':genre8,'addr8':addr8,'phone8':phone8,'rmood8':rmood8,'dayornight8':dayornight8,
    'name9':name9,'category9':category9,'img9':img9,'genre9':genre9,'addr9':addr9,'phone9':phone9,'rmood9':rmood9,'dayornight9':dayornight9,
    'name10':name10,'category10':category10,'img10':img10,'genre10':genre10,'addr10':addr10,'phone10':phone10,'rmood10':rmood10,'dayornight10':dayornight10
    }
    return render(request,'main2.html',context)

#추천평가페이지
def detail(request):
    vote=Voting.objects.get() 
    vote2=Voting2.objects.get()
    context={"vote":vote, "vote2":vote2}
    return render(request,'detail.html',context)
 
def end(request):
    context={}
    vote=Voting.objects.get() 
    vote2=Voting2.objects.get()
    context['vote']=vote    
    context['vote2']=vote2

    try:
        if request.POST['ans1']=='5':
            vote.result5 +=1
        elif request.POST['ans1']=='4':
            vote.result4 +=1
        elif request.POST['ans1']=='3':
            vote.result3 +=1
        elif request.POST['ans1']=='2':
            vote.result2 +=1
        elif request.POST['ans1']=='1':
            vote.result1 +=1
        vote.save()
            
        if request.POST['ans2']=='5':
            vote2.score5 +=1
        elif request.POST['ans2']=='4':
            vote2.score4 +=1
        elif request.POST['ans1']=='3':
            vote2.score3 +=1
        elif request.POST['ans1']=='2':
            vote2.score2 +=1
        elif request.POST['ans1']=='1':
            vote2.score1 +=1
        vote2.save()
    except:  
        message="✔ 반드시 하나를 선택해주세요 ✔"
        context['message']=message
        return render(request,'detail.html',context)
    
    
    return render(request,'end.html',context)