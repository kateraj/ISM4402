#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[7]:


pd.pivot_table(df, index=['Cars Sold'])


# In[11]:


df['Cars Sold'].max()


# In[12]:


df['Cars Sold'].mean()


# In[13]:


df['Cars Sold'].min()


# In[14]:


pd.pivot_table(df,
values=['Cars Sold'],
index=['Gender'])


# In[20]:


df['Years Experience'].mean()


# In[22]:


pd.pivot_table(df,
values=['Hours Worked'],
index=['Cars Sold'])


# In[25]:


pd.pivot_table(df,
values=['Hours Worked'],
index=['Cars Sold']) >3


# In[33]:


df2 = df.loc[df['Hours Worked'] > 3]
pd.pivot_table(df2,
index=['Gender'],
aggfunc='mean',
values=['Cars Sold','Hours Worked'])


# In[34]:


df2 = df.loc[df['Years Experience'] > 3]
pd.pivot_table(df2,
index=['Gender'],
aggfunc='mean',
values=['Cars Sold','Years Experience'])


# In[35]:


pd.pivot_table(df,
values=['Cars Sold'],
index=['SalesTraining'])


# In[ ]:




