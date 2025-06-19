import pandas as pd 
## 데이터를 판다스 형식으로 변환
df2 = pd.read_csv('./data/tmdb_5000_movies.csv')
top10_data = df2[['title','vote_count','vote_average']]

##  필요한 값은,  vote_average의 평균, 
C=top10_data['vote_average'].mean(axis=0)
# vote_count의 10% 지점의 값
m=top10_data['vote_count'].quantile(0.9)

# 상위 10프로만 참여한 별점만 인정하겠다.. 
a = top10_data['vote_count']>=m
tt = top10_data.loc[a]

## 위에서 만든 평균, 10프로시점의 인원수를 가지고 최종 score를 선정하는 공식을 정의합니다.
def score_rating(x, m=m, c=C):   
    v= x['vote_count']    
    R =x['vote_average']
    return (v/(v+m)*R)+(m/(m+v)*C)

temp_score = tt.apply(score_rating, axis=1) 
tt['score']=temp_score
tt = tt.sort_values('score', ascending=False)

def mtop10():
    return tt[['title','vote_count','vote_average']].head(10)
