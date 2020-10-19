#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
result = sm.ols(formula='grade ~ age- 1', data=df).fit()
result = sm.ols(formula='grade ~ exercise- 1', data=df).fit()
result = sm.ols(formula='grade ~ study- 1', data=df).fit()
result.summary()

