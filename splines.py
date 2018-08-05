
# coding: utf-8

# In[82]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
get_ipython().magic('matplotlib inline')


# In[157]:


x = np.array([0, 1.11111111, 2.22222222, 3.33333333, 4.44444444, 5.55555556, 6.66666667, 7.77777778, 8.88888889, 10])
x2 = np.linspace(min(x),max(x),100)
y = np.array([0, 4, 5, 8, 7, 6, 6, 8, 9, 10])


# In[158]:


interp = interpolate.interp1d(x, y, 'cubic')
y2 = interp(x2)


# In[159]:


plt.scatter(x, y)
plt.plot(x2, y2)
plt.show()


# In[ ]:




