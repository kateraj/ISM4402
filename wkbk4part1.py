#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']

if group_names >= 80: 
    print ("Pass")
else:
    print ("Fail")


# In[ ]:





# In[ ]:




