#4.4 seaborn 패키지를 이용한 시각화 

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

df = sns.load_dataset('titanic')
print(df.head())

#나이와 운임의 관계를 살펴보자.
sns.scatterplot(data=df, x='age', y='fare')
print(plt.show())

#그룹 별로 점의 색과 모양 바꾸기.
sns.scatterplot(data=df, x='age', y='fare', hue='class', style='class') #hue는 그룹 별 색깔, style은 그룹 별 모양을 의미한다. 
print(plt.show())

#seaborn을 활용한 히트맵

df_pivot = df.pivot_table(index='class',
                          columns='sex',
                          values='survived',
                          aggfunc='mean')

print(df_pivot)

sns.heatmap(df_pivot, annot=True, cmap='coolwarm')
#annot은 데이터의 값을 표시할지 여부, cmap은 팔레트의 종류로서 coolwarm 값이 높을수록 붉은색, 낮을수록 푸른색을 의미한다. 
print(plt.show())

#4.4.1 한 번에 여러 개의 그래프 나타내기 
#seaborn 패키지 함수들은 크게 'figure-level'과 'axes-level' 함수로 나뉘어져 있다.
#figure level 함수(replot, displot, catplot)
#axes level 함수(replot - scatterplot, lineplot/ displot - hisplot, kdeplot, ecdfplot, rugplot, catplot - stripplot, swarmplot, boxplot,  violinplot, pointplot, barplot)

sns.displot(data=df, x='age', hue='class', kind='hist', alpha=0.3)  #hist: 히스토그램, alpha: 투명도 조절           
plt.show()
   
sns.displot(data=df, x='age', col='class', kind='hist') #col 인자에 특정 열을 입력하면 해당 열을 기준으로 그래프가 열 방향으로 각각 분할되어 표현된다. 
plt.show()  

sns.displot(data=df, x='age', col='class', row='sex', kind='hist') #행 sex, 열 class 
plt.show()

#아래와 같이 히스토그램을 타나내는 histplot() 함수를 실행하면 오류가 발생한다. 
#sns.histplot(data=df, x='age', col='class', row='sex') 
#axes-level 함수인 histplot()로는 facetgrid 할 수 없다

plt.rc('font', family='Malgun Gothic') #한글 폰트 지정 
g, axes = plt.subplots(2, 1, figsize=(8, 6)) #subplots() 함수를 통해 2개의 axes를 생성한다. 

sns.histplot(data=df, x='age', hue='class', ax=axes[0]) #hisplot() 함수를 통해 히스토그램을 그린 후, ax = axe[0]을 입력하면 첫 번째 axes에 해당하는 그래프가 출력된다.
sns.barplot(data=df, x='class', y='age', ax=axes[1])  #barplot() 함수를 통해 막대 그래프를 그린 후, ax = axe[1]을 입력하면 두 번째 axe에 해당 그래프가 출력된다. 

axes[0].set_title('클래스별 나이 분포도') 
axes[1].set_title('클래스별 평균 나이')

g.tight_layout() #tight_layou() 함수를 입력하면 여백이 조정된다.
plt.show()