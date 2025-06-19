import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
f='The Dark Knight Rises' ## 입력할 영화 제목(클라이언트가 보내준 영화 제목)

df1=pd.read_csv('./data/tmdb_5000_movies.csv')
df2=df1[['original_title','overview']]
co_data=df2['overview']
mo_data=df2['original_title']
co_data=co_data.fillna('')
co_data.isnull().values.any()

tf=TfidfVectorizer(stop_words='english')   
tf_matrix=tf.fit_transform(co_data)  
cosine_sim=linear_kernel(tf_matrix,tf_matrix)


find_num=pd.Series(mo_data.index, index=df2['original_title'])
def toptop10(fname):
    number_idx=find_num[fname]  ## 문자열로 영화의 인덱스명(번호)를 찾는다
    aa=list(enumerate(cosine_sim[number_idx]))
    data_sort=sorted(aa,key=lambda x : x[1], reverse=True)
            ## aa 리스트로 정렬해라.. 기준은 각 튜플의 1번째 값으로 정렬해라. 내림차순이다.
    fdata=data_sort[1:11]
    r_movie= []
    for i in fdata:
        b={'name':mo_data[i[0]]}
        r_movie.append(b)
    return r_movie  ## 클라이언트에게 응답할 자료