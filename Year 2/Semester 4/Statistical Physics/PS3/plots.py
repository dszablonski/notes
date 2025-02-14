#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:21:28 2025

@author: dominik
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k
from scipy.constants import physical_constants
import numpy.ma as M 

ev = physical_constants['electron volt'][0]
N = 6e23
#ev = k
def E(T):
    x = ev /(k*T)
    numerator = 2 * ev * np.sinh(x)
    
    denominator = 1 + (2*np.cosh(x))
    
    return -numerator/denominator

def C_v(T):
    
    x = ev /(k*T)
    coef = 2 * k * (x**2)
    
    numerator = 2 + np.cosh(x)
    
    denominator = (1 + 2*np.cosh(x))**2
    
    return coef * (numerator/denominator)

def S(T):
    x=ev /(k*T)
    
    term_1 = N*k*np.log(1 + 2*np.cosh(x))
    
    numerator = 2 * N * ev * np.sinh(x)
    
    denominator = T * (1 + 2*np.cosh(x))
    # N\ k\ln\left(1\ +\ 2\ \cosh\left(\frac{a}{kx}\right)\right)\ -\ \frac{2Na\sinh\left(\frac{a}{kx}\right)}{x\left(1\ +\ 2\cosh\left(\frac{a}{kx}\right)\right)}
    return term_1 - (numerator/denominator)

def plotter(function, x_label, y_label, name):
    T = np.linspace(0, 1e5, num = 100000)
    
    vals = function(T)

    plt.plot(T, vals, "r-")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.annotate(("Choosing $\epsilon = 1eV$"
                  "\n"
                  r"$N = 6\times10^{23}$"
                        
                  ), (6e4,4e-24), bbox = dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.grid()
    #plt.title("Low Temp Limit")
    plt.plot()
    plt.savefig(name, dpi=1000)

#plotter(E, r"$1/T$", r"$\langle E\rangle$", "E high.pdf")

#plotter(C_v,r"$T$", r"$\langle C_V\rangle$", "C_V.pdf")

plotter(S, "$T$", r"$\langle S \rangle$", "S.pdf")