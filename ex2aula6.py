from math import *

#DADOS
#DADOS
l=0.3 #metros
p = 0.12 #metros
a = 0.0009 #metros
a2= (200*10**-3)**2
h = 15 #W/m^2.K
k=200 #W/m.K
Tinf =  300 #K
Tb = 350 #K
m = sqrt((h*p)/(k*a)) #m^2/s   

#CALCULOS
M = (Tb-Tinf)*(sqrt(h*p*k*a))
print("M = ",M)


qs = h*a2*(Tb-Tinf)
print("q(sem haleta) = ",qs,"W")

qsa = h*(a2-a)*(Tb-Tinf)
qa = M*((sinh(m*l) + (h/(m*k))*cosh(m*l))/(cosh(m*l) + (h/(m*k))*sinh(m*l)))
qtot = qsa + qa
print("qtot = ",qtot,"W")
