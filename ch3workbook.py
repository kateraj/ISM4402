#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
    columns=['Names', 'Grades'])
df
grades2 = [0 if i < 0 else i for i in grades]


# In[ ]:




