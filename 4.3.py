#pandas 패키지를 이용한 시각화 
#line 선 그래프 / bar 수직 막대 그래프 / barh 수평 막대 그래프 / hist 히스토그램 
# box 박스 플롯 / kde 커널 밀도 그래프 / area 면적 그래프 / pie 파이 그래프 / scatter 산점도 그래프 / hexbin 고밀도 산점도 그래프 

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 


df = sns.load_dataset('diamonds')
print(df.head())

#carat과 price 간의 관계를 살펴보자. 

#plt.rc('font', family='Malgun Gothic')
#df.plot.scatter(x='carat', y='price', figsize=(10,6), title='캐럿과 가격 간의 관계')
#plt.show()

df.plot.scatter(x='carat', y='price', c='cut', cmap='Set2', figsize=(10,6))  #cmap에 파레트를 지정한다. 
plt.show()

df['price'].plot.hist(figsize=(10,6), bins=20)
plt.show()

#히스토그램으로 표현하고 싶은 열만 선택한 후, plot.hist() 메서드를 적용하면 히스토그램이 표현된다. 
#color에 따른 carat의 평균을 막대 그래프로 표현 
df.groupby('color')['carat'].mean().plot.bar(figsize=(10,6)) 
# 'color' 별로 그룹을 묶은 후 'carat'의 평균을 구한다. 
# 구해진 값에 plot.bar() 메서드를 적용해 막대 그래프로 표현 
plt.show()