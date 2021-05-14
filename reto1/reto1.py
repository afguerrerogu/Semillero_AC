import numpy as np
import math

m1 = 1
m2 = 3e-6

G = 4*np.pi**2

xsol = [0,0,0]
xtierr = [1,0,0]

vsol = [0,0,0]
vtierr = [0,6.2778,0]

def mag(x): 
    return math.sqrt(sum(i**2 for i in x))

def distance(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)

def energy(x1,x2,v1,v2):
    r =  distance(x1,x2)
    return 1/2*m1*mag(v1)**2 + 1/2 * m2 * mag(v2)**2 - (G*m1*m2)/r

def momentum(x1,x2,v1,v2):
    return m1*np.cross(x1,v1) + m2*np.cross(x2,v2)
 
E = energy(xsol,xtierr,vsol,vtierr)
L = momentum(xsol,xtierr,vsol,vtierr)
print(E)
print(L)