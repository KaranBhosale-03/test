#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import pandas as pd
import requests as r
import matplotlib.pyplot as plt

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs6339/ex/L2.2/'
file_1 = 'colors.csv'

#pull employment
res = r.get(url + file_1)
dfcol = pd.read_csv(io.StringIO(res.text)) 
dfcol

#pandas df boxplot.meh.
dfcol.boxplot()
plt.show()

#let's look at outliers.
dfcol['numerics'].hist()
plt.show()

#bit cleaner.  let's do a box plot
plt.boxplot(dfcol['numerics'])
plt.show()

#well that's ugly.  Let's look at a slightly not terrible version.
dfcol['numerics2'].hist()
plt.show()

#bit cleaner.  let's do a box plot
plt.boxplot(dfcol['numerics2'])
plt.show()

#Question, what do we do with outliers?  


# In[ ]:




