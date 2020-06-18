#!/usr/bin/env python
# coding: utf-8

# 다음 뉴스 크롤링 실습

# In[7]:


import requests
from bs4 import BeautifulSoup as bs


# In[8]:


res = requests.get("https://news.daum.net/digital")
soup = bs(res.content, 'html.parser')
div1 = soup.find('div', class_='section_cate section_headline')
strong_list1 = div1.find_all('strong', class_='tit_thumb')
strong_list2 = div1.find_all('strong', class_='tit_mainnews')


# In[9]:


###### find('a').get('href') 기억하기 

final_url = []
for strong1 in strong_list1:
    final_url.append(strong1.find('a').get('href'))

for strong2 in strong_list2:
    final_url.append(strong2.find('a').get('href'))
    
print(final_url)


# In[10]:


text_sum = []
for news_url in final_url:
    getrequests = requests.get(news_url)
    Soup = bs(getrequests.content,'html.parser')
    result = Soup.find("div", {'id':'harmonyContainer'})
    text_sum.append(result.get_text())
    print(text_sum)

