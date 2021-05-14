import math
import numpy as np
from matplotlib import pyplot as plt

class ellipse:
    
    def __init__(self,semi_major_axis=1.,excentricity=0.0167,pericenter=0.):
        
        self.a = semi_major_axis
        self.e = excentricity
        self.w = pericenter
        if  self.e >=1. or self.e<0.:
            self.is_ellipse = False
            self.mes = f'The eccentricity {self.e:.5f} does not correspond to an ellipse!'
        else:
            self.is_ellipse = True
 
    
    def test(self):
        assert self.is_ellipse == True, "error"

    def semilatus(self):
        p = self.a*(1-self.e**2)
        return p
    
    def r_min(self):
        r_p = self.a*(1 - self.e)
        return r_p 
    
    def r_max(self):
        r_p = self.a*(1 + self.e)
        return r_p
    
    def plot(self, color="crimson"):
        boundary = 2*self.a
        f = np.linspace(0, 2*np.pi, 1000)
        x = self.a*(1-self.e**2)*np.cos(f)/(1+self.e*np.cos(f-self.w))
        y = self.a*(1-self.e**2)*np.sin(f)/(1+self.e*np.cos(f-self.w))

        xsemaxis = np.linspace(-self.r_max()*np.cos(self.w), 
                             self.r_min()*np.cos(self.w), 100)
        ysemiaxis = np.tan(self.w)*xsemaxis
      
        plt.figure(figsize=(7,7))
        plt.plot(x,y, color=color)
        plt.plot(xsemaxis,ysemiaxis, '--', color='grey')
        plt.axhline(color='black',alpha=0.3)
        plt.axvline(color='black',alpha=0.3)
        plt.xlim(-boundary,boundary)
        plt.ylim(-boundary, boundary)
        plt.xlabel(f'$x$')
        plt.ylabel(f'$y$')
        plt.show()
  
  