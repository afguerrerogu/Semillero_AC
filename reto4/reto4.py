#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:19:10 2021

@author: andres
"""

import numpy as np
import pandas as pd

m1 = 1
m2 = 3e-6
G = 4*np.pi**2

def div_dat(q):
    x = []
    v = []
    for i in q:
        x.append(i[:3])
        v.append(i[3:])
    return x,v


def energy(m,q):
    x, v = div_dat(q)
    KE = 0 
    PE = 0
    for i in range(len(m)):
        KE += m[i]*np.linalg.norm(v[i])**2
        for j in range(i+1,len(m)):    
            PE += (G*m[i]*m[j]/np.linalg.norm(v[i]-v[j]))        
    return 1/2*KE - 1/2 *PE

def momentum(m,q):
    x,v = div_dat(q)
    momentum = 0
    for i in range(len(m)):
        momentum += m[i]*np.cross(x[i],v[i])
    return momentum

#Data = pd.read_csv("data.dat", comment="#")
#masses = Data["M"].to_numpy()
#Data =  Data.drop("M", axis=1)
#Q = np.array(Data)


Data = np.loadtxt("S0stars.asc",comments="#")
masses = Data[:,6]
Q = np.delete(Data,6,axis=1)

E = energy(masses,Q)
L = momentum(masses,Q)