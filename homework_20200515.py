#!/usr/bin/env python
# coding: utf-8

# Lab1 : Matplotlib 사용해보기

# In[32]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[6]:


ex2data1 = pd.read_csv(r'C:\\workspace\\ex2data1.txt', header=None)


# In[11]:


ex2data1.columns = ["Exam1 score","Exam2 score","lable3"]
ex2data1[:5]


# In[12]:


from matplotlib import rcParams, style
style.use('ggplot')
rcParams['font.size'] = 12


# In[25]:


Admitted = ex2data1[ex2data1['lable3']==1]
Not_admitted = ex2data1[ex2data1['lable3'] ==0]

admitted_sc = plt.scatter(Admitted['Exam1 score'],Admitted['Exam2 score'], marker='o', color='g')
Not_admitted_sc = plt.scatter(Not_admitted['Exam1 score'],Not_admitted['Exam2 score'], marker='+', color='r')

plt.legend((admitted_sc,Not_admitted_sc), ('Admitted','Not admitted'),loc='upper right')
plt.axis([20,110,20,110])
plt.xlabel("Exam1 score")
plt.ylabel("Exam2 score")


# Lab2 : scikit learn 사용해보기 

# In[29]:


from sklearn.linear_model import LinearRegression
data = pd.read_csv(r'C:\workspace\housing_data.txt', sep='\s+',header = None)
data [:10]


# In[30]:


data.columns = ['CRIM','ZN', 'INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
data [:10]


# In[34]:


X = np.array(data['AGE']) 
y = np.array(data['MEDV'])
get_ipython().run_line_magic('pinfo', 'X.shape')
X = X.reshape(-1,1)
y = y.reshape(-1,1)
reg = LinearRegression()
reg.fit(X, y)
reg.coef_
reg.intercept_

plt.scatter(X,y)

x = np.linspace(0,100,num=1000)
plt.plot(x,reg.intercept_ + x*reg.coef_[0])
plt.show()


# * 함수 만들기

# In[49]:


file_path = r'C:\workspace\housing_data.txt'
def cal_data(col1,col2):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    data = pd.read_csv(file_path, sep='\s+',header = None)
    X = np.array(data[col1]) 
    y = np.array(data[col2])
    X = X.reshape(-1,1)
    y = y.reshape(-1,1)
    reg = LinearRegression()
    reg.fit(X, y)
    reg.coef_
    reg.intercept_

    plt.scatter(X,y)

    x = np.linspace(0,100,num=1000)
    plt.plot(x,reg.intercept_ + x*reg.coef_[0])
    return plt.show()


# In[50]:


cal_data(6,13)


# In[ ]:





# In[ ]:




