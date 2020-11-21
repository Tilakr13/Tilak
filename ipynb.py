#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy import stats
stats.norm.cdf(740,711,29)


# In[3]:


stats.norm.cdf(740,711,29) - stats.norm.cdf(697,711,29)


# In[4]:


import pandas as pd
import numpy as np


# In[5]:


beml_df = pd.read_csv("BEML.csv")
beml_df[0:5]


# In[6]:


glaxo_df = pd.read_csv("GLAXO.csv")
glaxo_df[0:5]


# In[10]:


beml_df = beml_df[['Date', 'Close']]
glaxo_dfx = glaxo_df[['Date', 'Close']]


# In[11]:


beml_df


# In[13]:


beml_df= beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))
glaxo_df= glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))


# In[14]:


beml_df


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(glaxo_df.Close);
plt.xlabel('Time');
plt.ylabel("Close Price")


# In[18]:


plt.plot(beml_df.Close);
plt.xlabel('Time');
plt.ylabel('Close Price')


# 
