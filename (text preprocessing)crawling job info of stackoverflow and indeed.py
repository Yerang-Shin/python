#!/usr/bin/env python
# coding: utf-8

# 직업명 텍스트 전처리

# In[1]:


import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

###### 파이썬에서는 경로명을 쓸 때 '/'를 써야함 
df = pd.read_csv("C:/workspace/jobs.csv", sep=',', encoding='utf-8')


###### 이름을 지정하여 위치를 선택시: loc / 인덱스 번호로 위치를 선택시: iloc 
###### re.sub(살릴내용, 바꾸고싶은결과, 데이터): 문자열 치환 
title_list = df.loc[:,"title"].values
new_data = []
for num in range(len(title_list)):
    text = re.sub('[^a-zA-Z/-]+', "ㄲ", title_list[num])
    if "ㄲ" in text:
        new_data.append(text)
    else:
        new_data.append('')
        
        
new_data2 = []
for num in range(len(new_data)):
    new_data2.append(re.sub('[^a-zA-Z]+', " ", new_data[num]))
print(new_data2[:10])


##### split함수는 문자열과 리스트 모두 가능 
##### [][]: 이차열 리스트 
new_data3 = []
new_data4 = []
for num in range(len(new_data2)):
    new_data3.append(new_data2[num].split())
    for cnt in range(len(new_data3[num])):
        new_data4.append(new_data3[num][cnt])


# 나라명 텍스트 전처리

# In[ ]:


###### pd.read_csv로 불러온 후 에러가 뜬다면 astype()으로 타입을 바꿔보기
###### startswith: 해당문자열로 시작하는 것을 찾음 
location = df.location.astype(str)
location_list = df.loc[:,"location"].values
new_location1 = []
for num in range(len(location_list)):
    if location_list[num].startswith('http'):
        new_location1.append('')
    else:
        new_location1.append(location_list[num])
        
        
new_location2 = []
for num in range(len(new_location1)):
    split_words = new_location1[num].split(',')
    if len(split_words) == 2:
        new_location2.append(split_words[1])
    else:
        new_location2.append(split_words[0])


# Counter를 이용하여 단어의 빈도수 계산

# In[ ]:


c = Counter(new_data4)
words = dict(c.most_common(50))


# 워드 클라우드 

# In[ ]:


matplotlib.rc('font',family = 'Malgun Gothic')
spwords=set(STOPWORDS)
spwords.add('No office location')
wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf', 
                      stopwords = spwords, background_color='white',colormap = "Accent_r",
                      width=2000, height=1500).generate_from_frequencies(words)

plt.figure(figsize=(10,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show() 

