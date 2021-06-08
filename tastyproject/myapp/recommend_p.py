import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import pymysql
import os
#감성키워드 ~~~~~      #요고를 디비랑 장고 연결로

# from datetime import datetime
# print('START TIME : ',str(datetime.now())[10:19] )  #속도 측정용

csv_path = os.path.join(os.path.dirname(__file__), 'p_dis_words.csv')
simpmood=pd.read_csv(csv_path)


#디비 장고연결
conn = pymysql.connect(host='tasty.cqca6sggc1nx.ap-northeast-2.rds.amazonaws.com',user='seo', password='tasty98!', db='tasty-db', charset='utf8')
cursor= conn.cursor()

sql="select idx,dayimg,name,category,genre,pmood from myapp_restaurant"   #workbench에 있는 테이블이름 그대로
cursor.execute(sql)
# result = pd.read_sql_query(sql,conn)    #=rest???
cursor.fetchone()  #빼도될듯
rest=pd.read_sql(sql,conn)   #dataframe으로 만들어
########print(rest)
# result.to_csv(r'pandas_output.csv',index=False)
conn.close()

# 
# 파이썬에서 print하면 튜플형식으로 되서 아래에 리스트로 담기지가 않음! 
#그래서 dataframe으로 만들어 프린트하면 됨!
rest[['pmood']] = rest[['pmood']].astype('str')
rest['pmood'] =rest['pmood'].str.split(',')

# print(rest)     #rest=restaurant
# print(simpmood)
#키워드별 감성 유사한거 리스트에 넣는 코드
import ast
for i in range(0,len(simpmood)):
  simpmood['words'][i] = ast.literal_eval(simpmood['words'][i])
# 
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

rest['pmood'] = rest['pmood'].apply(lambda x : (' ').join(x))
u=count_vect.fit(rest['pmood'])
rest_mat_pmood=count_vect.transform(rest['pmood'])

simpmood['words'] = simpmood['words'].apply(lambda x : (' ').join(x))
key_mat_pmood=count_vect.transform(simpmood['words'])
#
# print(u.get_feature_names())
# print(key_mat_pmood.toarray())
#

######코사인 유사도#######
from sklearn.metrics.pairwise import cosine_similarity

pmood_sim=cosine_similarity(key_mat_pmood,rest_mat_pmood)

# print(pmood_sim.shape)
# print(pmood_sim[:10])

pmood_sim_sorted_ind =pmood_sim.argsort()[:, ::-1]
import json

def find_sim_rest(key_name):
  #인자로 입력된 rest DF에서 'name'칼럼이, 입력된 rest_name 데이터프레임 추출
  name_key = simpmood[simpmood['NM']== key_name]

  #key_name 가진 데이터프레임의 인덱스 객체를 ndarray로 반환하고
  #sorted_ind 인자로 입력된 key_sim_sorted_ind 객체에서
  #유사도 순으로 top_n개의 index 추출
  name_index = name_key.index.values
  similar_indexes = pmood_sim_sorted_ind[name_index, :20]   # 10개 

  #top_n 2차원이므로 index 로 사용하기위해 array로 바꿔줘야 함.
  # print(similar_indexes)
  similar_indexes = similar_indexes.reshape(-1)
  print(similar_indexes)
  idx= rest.iloc[similar_indexes]
  print(idx)
  result=json.loads(idx.to_json(orient='index',force_ascii=False))  

  return result


