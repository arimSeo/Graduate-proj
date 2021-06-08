import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import pymysql

#디비 장고연결
conn = pymysql.connect(host='tasty.cqca6sggc1nx.ap-northeast-2.rds.amazonaws.com',user='seo', password='tasty98!', db='tasty-db', charset='utf8')
cursor= conn.cursor()

sql="select * from myapp_restaurant"   #workbench에 있는 테이블이름 그대로
cursor.execute(sql)
cursor.fetchall()  #빼도될듯
rest=pd.read_sql(sql,conn)   #dataframe으로 만들어

conn.close()


#각각을 리스트에 담는 과정 
rest[['quantity']] = rest[['quantity']].astype('str')
rest['quantity'] =rest['quantity'].str.split(" ")

rest[['category']] = rest[['category']].astype('str')
rest['category'] =rest['category'].str.split(" ")

rest[['genre']] = rest[['genre']].astype('str')
rest['genre'] =rest['genre'].str.split(" ")

rest[['dayornight']] = rest[['dayornight']].astype('str')
rest['dayornight'] =rest['dayornight'].str.split(" ")

rest[['qualperprice']] = rest[['qualperprice']].astype('str')
rest['qualperprice'] =rest['qualperprice'].str.split(",")

rest[['rmood']] = rest[['rmood']].astype('str')
rest['rmood'] =rest['rmood'].str.split(",")

rest[['pmood']] = rest[['pmood']].astype('str')
rest['pmood'] =rest['pmood'].str.split(",")

rest[['who']] = rest[['who']].astype('str')
rest['who'] =rest['who'].str.split(",")

rest[['whenn']] = rest[['whenn']].astype('str')
rest['whenn'] =rest['whenn'].str.split(",")

rest[['purpose']] = rest[['purpose']].astype('str')
rest['purpose'] =rest['purpose'].str.split(",")


pd.set_option('max_colwidth',100)


from sklearn.feature_extraction.text import CountVectorizer

#CountVectorizer: 각 텍스트에서 단어 출현 횟수를 카운팅한 벡터
#countvectorizer 적용 위해 공백문자로 word단위 구분되는 문자열로 변환시킨다.
#한 컬럼의 리스트속 단어를 벡터화함. 
count_vect = CountVectorizer()#CountVectorizer: 각 텍스트에서 단어 출현 횟수를 카운팅한 벡터

rest['quantity'] = rest['quantity'].apply(lambda x : (' ').join(x)) #countvectorizer 적용 위해 공백문자로 word단위 구분되는 문자열로 변환시킨다.
key_mat_quantity = count_vect.fit_transform(rest['quantity']) #fit으로 모든 리스트 속 요소를 단어사전으로 만듦. transform으로 단어-문서 행렬을 만듦. 벡터화.
#key_mat_xxxx 는 각 셀의 리스트 속 단어들을 벡터화 시킨 배열(array)

rest['category'] = rest['category'].apply(lambda x : (' ').join(x))
key_mat_category = count_vect.fit_transform(rest['category'])

rest['genre'] = rest['genre'].apply(lambda x : (' ').join(x))
key_mat_genre = count_vect.fit_transform(rest['genre'])

rest['qualperprice'] = rest['qualperprice'].apply(lambda x : (' ').join(x))
key_mat_qualperprice = count_vect.fit_transform(rest['qualperprice'])

rest['dayornight'] = rest['dayornight'].apply(lambda x : (' ').join(x))
key_mat_dayornight = count_vect.fit_transform(rest['dayornight'])

rest['rmood'] = rest['rmood'].apply(lambda x : (' ').join(x))
key_mat_rmood = count_vect.fit_transform(rest['rmood'])

rest['pmood'] = rest['pmood'].apply(lambda x : (' ').join(x))
key_mat_pmood = count_vect.fit_transform(rest['pmood'])

rest['who'] = rest['who'].apply(lambda x : (' ').join(x))
key_mat_who = count_vect.fit_transform(rest['who'])

rest['whenn'] = rest['whenn'].apply(lambda x : (' ').join(x))
key_mat_whenn = count_vect.fit_transform(rest['whenn'])

rest['purpose'] = rest['purpose'].apply(lambda x : (' ').join(x))
key_mat_purpose = count_vect.fit_transform(rest['purpose'])


######코사인 유사도#######
from sklearn.metrics.pairwise import cosine_similarity

key_sim_quantity=0.06*cosine_similarity(key_mat_quantity,key_mat_quantity)
key_sim_category=0.09*cosine_similarity(key_mat_category,key_mat_category)
key_sim_genre=0.5*cosine_similarity(key_mat_genre,key_mat_genre)
key_sim_qualperprice=0.1*cosine_similarity(key_mat_qualperprice,key_mat_qualperprice)
key_sim_dayornight=0.4*cosine_similarity(key_mat_dayornight,key_mat_dayornight)
key_sim_rmood=4*cosine_similarity(key_mat_rmood,key_mat_rmood)
key_sim_pmood=2*cosine_similarity(key_mat_pmood,key_mat_pmood)
key_sim_who	=0.5*cosine_similarity(key_mat_who,key_mat_who)
key_sim_whenn=0.8*cosine_similarity(key_mat_whenn,key_mat_whenn)
key_sim_purpose=0.8*cosine_similarity(key_mat_purpose,key_mat_purpose)

key_sim = key_sim_quantity+key_sim_category+key_sim_genre+key_sim_qualperprice +key_sim_dayornight+key_sim_rmood+key_sim_pmood+key_sim_who+key_sim_whenn+key_sim_purpose
# print(key_sim.shape)
# print(key_sim[:1])

#
#식당별로 가장 유사도가 높은 순서로 식당 출력(인덱스값)
key_sim_sorted_ind =key_sim.argsort()[:, ::-1]
# print(key_sim_sorted_ind[:2])

import json
def find_sim_rest(rest_name, top_n):
  #인자로 입력된 rest DF에서 'name'칼럼이, 입력된 rest_name 데이터프레임 추출
  name_rest = rest[rest['name']== rest_name]

  #rest_name 가진 데이터프레임의 인덱스 객체를 ndarray로 반환하고
  #sorted_ind 인자로 입력된 key_sim_sorted_ind 객체에서
  #유사도 순으로 top_n개의 index 추출
  name_index = name_rest.index.values
  similar_indexes = key_sim_sorted_ind[name_index, :(top_n)]  #top_n -> 11 :views에서 인자로

  #top_n 2차원이므로 index 로 사용하기위해 array로 바꿔줘야 함.
  # print(similar_indexes)
  similar_indexes = similar_indexes.reshape(-1)
  idx2=rest.iloc[similar_indexes]

  result2=json.loads(idx2.to_json(orient='index',force_ascii=False)) 
  print(result2)

  return result2