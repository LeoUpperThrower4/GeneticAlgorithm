# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:57:19 2018

@author: Leo
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

def poly(x, y):
    p = np.polyfit(x, y, 3)
    return ((p[0] * (x**3)) + (p[1]* x**2) + (p[2] * x) + p[3])

plt.plot(x, y, '*')
plt.plot(x, poly(x, y), 'r')