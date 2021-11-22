#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np


# In[37]:


def calculate(list):
    a =np.array(list)
    
    maxis1= [a[[0,1,2]].mean(), a[[3,4,5]].mean(), a.mean() ]
    maxis2= [a[[ 3,4,5]].mean(), a[[6,7,5]].mean(), a.mean() ]
    vaxis1= [a[[0,1,2]].var(), a[[3,4,5]].var(), a.var() ]
    vaxis2= [a[[ 3,4,5]].var(), a[[6,7,5]].var(), a.var() ]
    mi1= [a[[0,1,2]].min(), a[[3,4,5]].min(), a.min() ]
    mi2= [a[[3,4,5]].min(), a[[6,7,5]].min(), a.min() ]
    ma1= [a[[0,1,2]].max(), a[[3,4,5]].max(), a.max() ]
    ma2= [a[[3,4,5]].max(), a[[6,7,5]].max(), a.max() ]
    su1= [a[[0,1,2]].sum(), a[[3,4,5]].sum(), a.sum() ]
    su2= [a[[3,4,5]].sum(), a[[6,7,5]].sum(), a.sum() ]
    return {
  'mean': [maxis1, maxis2, a.mean()],
  'variance': [vaxis1, vaxis2, a.var()],
        'min': [mi1, mi2, a.min()],
        'max': [ma1, ma2 , a.max()],
        'sum': [su1, su2, a.sum()] }        


# In[38]:


calculate([3,3,3,4,5,6,7,8])


# In[ ]:




