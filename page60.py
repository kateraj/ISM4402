#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df = df.sort_values(by=['name','grade', 'age'],ascending=[True, True])
df.head()

