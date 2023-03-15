# 4.1 데이터 시각화 
#파이썬에는 데이터 시각화에 matplotlib 또는 pandas 패키지를 사용
#고급 시각화에는 seabron 패키지 사용 


import seaborn as sns
import matplotlib.pyplot as plt  #matplotlib 패키지 중에서 pyplot 모듈을 plt로 불러온다. 

df = sns.load_dataset('penguins')  

#plt.scatter(df['flipper_length_mm'], df['body_mass_g']) #scatter() 산점도 함수 내에 x축과 y축 정보 
#plt.show() #그래프 출력 

#df_group = df.groupby('species')['body_mass_g'].mean().reset_index() #'species' 별로 그룹을 묶은 후 'body_mass_g' 열의 평균을 구한다. 그 후 reset_index() 메서드를 통해 데이터프레임 형태로 나타낸다. 
#plt.bar(x=df_group['species'], height=df_group['body_mass_g']) #막대 그래프를 나타내는 bar() 함수 내에 x축과 높이 정보(hegiht)를 입력
#plt.show() #그래프 출력 

plt.rc('font', family='Malgun Gothic') #한글 폰트 지정 
plt.hist(df['body_mass_g'], bins=30) #히스토그램을 나타내는 hist() 함수 내에 나타내고자 하는 열을 입력한다. bins 인자에는 히스토그램을 몇 개의 구간으로 나눌지를 입력한다. 
plt.xlabel('Body Mass') # x축과 y축 레이블, 제목에 원하는 제묵을 입력한다. 
plt.ylabel('Count')
plt.title('펭귄의 몸무게 분포')
plt.show() 

import pandas as pd 

#df_unrate = pd.read_csv('https://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv')
#print(df_unrate.head())

#df_unrate['DATE'] = pd.to_datetime(df_unrate['DATE'])
#plt.plot(df_unrate['DATE', df_unrate['VALUE']]) #plot() 함수는 선 그래프를 나타내며, x축과 y축 정보를 각각 입력한다. 
#plt.show()

#4.2.1 한 번에 여러 개의 그래프 나타내기 
# stateless API(objected-based): 내가 지정한 figure, 내가 지정한 axes에 그림을 그리는 방법 
# stateful API(state-based): 현재의 figure, 현재의 axes에 그림을 그리는 방법 

fig, axes = plt.subplots(2, 1, figsize=(10, 6)) 
# plt.subplpot(2,1)을 통해 figure 내에 2행 1열로 2개의 axes객체를 만든다.  
# figsize=(10,6)을 통해 figure의 가로 세로 길이를 10과 6으로 고정한다.  

# 첫 번째 그림 
#axes[0].scatter(df['flipper_length_mm'], df['body_mass_g']) #산점도 
#axes[0].set_xlabel('날개 길이(mm)')   
#axes[0].set_ylabel('몸무게(g)')
#axes[0].set_title('날개와 몸무게 간의 관계')
#axes[0].set_title

# 두 번째 그림 
#axes[1].hist(df['body_mass_g'], bins=30)
#axes[1].set_xlabel('Body Mass')
#axes[1].set_ylabel('Count')
#axes[1].set_title('펭귄의 몸무게 분포')
#axes[1].set_title

#간격 조정
#plt.subplots_adjust(left=0.1,           #두 그림이 겹쳐 보이므로 subplots_adjust() 함수를 통해 여백을 조정 
#                    right=0.95,
#                    bottom=0.1,
#                    top=0.95,
#                    wspace=0.5,
#                    hspace=0.5)

#plt.show()

#하나의 그림(figure) 내에 2개의 그래프(axes)가 동시에 출력되었다.
#stateless 방법은 figure 내에 원하는 만큼 axes 객체를 나눈 후, axes를 지정하여 그래프를 표현
#반면에, stateful 방식은 subplot()을 통해 현재 axes를 설정하면 해당 부분에 그림을 그리게 된다. 

#plt.figure(figsize=(10,6))

#첫 번째 그림 
plt.subplot(2, 1, 1)
plt.scatter(df['flipper_length_mm'], df['body_mass_g'])
plt.xlabel('날개 길이(mm)')
plt.ylabel('몸무게(g)')
plt.title('날개와 몸무게 간의 관계 ')

#두 번째 그림 
plt.subplot(2, 1, 2)
plt.hist(df['body_mass_g'], bins=30)
plt.xlabel('Body Mass')
plt.ylabel('Count')
plt.title('펭귄의 몸무게 분포')

plt.subplots_adjust(left=0.1,            
                    right=0.95,
                    bottom=0.1,
                    top=0.95,
                    wspace=0.5,
                    hspace=0.5)

plt.show()