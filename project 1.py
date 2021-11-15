#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[99]:


data= pd.read_csv(r'C:\Users\Matti\Desktop\adult.data.csv')


# In[100]:


data.describe()


# In[101]:


data


# In[102]:


a=data[['age','sex']]


# In[103]:


c=a.set_index('sex')


# In[104]:


media=c.drop(index='Female')


# media_età

# In[105]:


media.mean()


# In[106]:


data.loc[(data['race']!= 'Black') & (data['race']!= 'White')]


# In[107]:


data.loc[data['race']== 'White']


# In[108]:


data['race'].value_counts()


# In[109]:


education=data['education'].value_counts()


# In[110]:


bachelors_perc=(5355/32561)


# In[111]:


bachelors_perc


# In[112]:


edu=education.tolist()


# In[113]:


edu


# In[114]:


aa=data['education'].value_counts()


# In[115]:


aa


# In[116]:


educ=pd.DataFrame({'education':[10501,
 7291,
 5355,
 1723,
 1382,
 1175,
 1067,
 933,
 646,
 576,
 514,
 433,
 413,
 333,
 168,
 51]}, index=[ 'hs-grad', 'some-college', 'bacherlors', 'masters', 'assoc-voc', '11th', 'assoc-acdm', '10th', '7th-8yh', 'prof-school', '9th','12th', 'doctorate', '5th-6th', '1st-4th', 'preschool'])


# In[117]:


educ


# In[118]:


(5355+1723+413)/educ.sum()


# In[119]:


data[['salary','education']]


# In[120]:


salary=data[['salary','education']].set_index('salary')


# In[121]:


salary


# In[122]:


salari=salary.drop(index= '<=50K')


# In[123]:


salari['education'].value_counts()


# In[124]:


quarta_domanda=959+2221+306


# In[125]:


quarta_domanda/educ.sum()


# In[126]:


data['hours-per-week','sex']


# In[127]:


bb=data['hours-per-week']


# In[128]:


bb.min()


# In[129]:


ccc=data[['salary','hours-per-week']].set_index('salary')


# In[130]:


ccc


# In[131]:


cccc=ccc.drop(index='<=50K')


# In[132]:


data.loc[(data['hours-per-week']==1)&(data['salary']=='>50K')]


# In[133]:


data.loc[data['hours-per-week']==1].count()


# In[134]:


2/20


# In[137]:


p=data[['native-country','salary']]


# In[142]:


pp=p.loc[p['salary']=='>50K']


# In[145]:


pp['native-country'].value_counts()


# In[150]:


occupation=data.loc[(data['native-country']=='India') & (data['salary']=='>50K')]


# In[152]:


occupation['occupation'].value_counts()


# In[ ]:




