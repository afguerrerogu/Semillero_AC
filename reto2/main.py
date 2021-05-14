import reto2 
import numpy as np

EarthOrbit = reto2.ellipse()
r_min = EarthOrbit.r_min()
r_max = EarthOrbit.r_max()
EarthOrbit.plot()

print(r_min)

OtherEllipse = reto2.ellipse(excentricity=0.8, pericenter=np.pi/3)
OtherEllipse.plot(color='cornflowerblue')

NotEllipse = reto2.ellipse(semi_major_axis= 1.5,excentricity =1.9,  pericenter=np.pi/3)
NotEllipse.plot()