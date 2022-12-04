#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 09:36:56 2022

@author: francescacottrell
"""
# IMPORTING PACKAGES
import numpy as np
import matplotlib.pyplot as plt
from cfd.initial_conditions import *
from cfd.operators import *

#-----------------------------------------------------------------------------

# DEFINING THE DOMAIN

# grid length 
L = 10
# number of cells in grid
nx = 100
# width of cells
dx = L/nx

# creating grid
x = np.linspace(0, L, nx+1)
# initial field is Gaussian of amplitude 1 centered at midpoint of domain
f0 = gaussian(x, 1, 5, 0.5)
# plotting domain
plt.plot(x, f0, 'kx')
# x and y axis labels
plt.xlabel('x', fontsize = 15)
plt.ylabel('f', fontsize = 15)
# adding gridlines to the plot
plt.grid(linestyle = '--')
plt.show()













