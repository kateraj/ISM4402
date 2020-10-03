#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

import numpy as np
df['isBusy'] = np.where(df['exercises', 'studies']>3, >17)
df.tail(10)

