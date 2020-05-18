# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:05:13 2020

@author: Vali
"""

import numpy as np
import matplotlib.pyplot as plt

def euler(x0, omega, stepsize):
      x0_ = x0 + stepsize*f(x0,omega)
      #y0 = y0 - stepsize*(omega**2*x0)
      return x0_
  
#def luler(x0, omega, stepsize):
      #x1 = x0 + stepsize*(-omega**2*x0)
      #return x0

#def heun(f, y0, parameters, stepsize):
     #y_new = y0 - stepsize*(-omega**2*x)
     #return y_new
     
     
def f(x0, omega):
    
    return -omega**2*x0

#def exact(t, x0, alpha):
    #return x0 * np.cos(alpha*t)

x0 = 1
omega = 1
h = 0.05
t = np.arange(0., 20*np.pi, h) 
xs = [x0]
#x_new = []
x0_=euler(x0,omega,h)

plt.plot(t[0], x0, 'ro')
  
for tn in t[1:]:
    
    x0 = x0 + h*0.5*(f(x0, omega)+ f(x0_, omega))
    #x = x + h*0.5*((euler(x0, y0, omega, h )))
    plt.plot(tn, x0, 'ro')
    xs += [x0]    
    
    

plt.show()
