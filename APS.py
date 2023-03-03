import math
import symbol as sym
import matplotlib.pyplot as plt
import numpy as np

#Determine a temperatura da 
# extremidade da haleta de aluminio e a 
# taxa de trasferncia de forma analitica


#DADOS
l=0.2 #metros
D =0.24 #metros
p = math.pi * D  #metros
a = math.pi*(D/2)**2 #metros
h = 25 #W/m^2.K
k=240 #W/m.K
Tinf =  273+25 #K
Tb = 373 #K
m = math.sqrt((h*p)/(k*a)) #m^2/s   

#CALCULOS EX1------------------------------------------------------------------------------------------
theta = math.cosh(0) + (h/(m*k))*math.sinh(0)

thetab= math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)

delta = theta/thetab
print(theta)
print(thetab)
print(math.cosh(m*l))
print(delta)

Tl = delta*(Tb-Tinf) + Tinf
print("Tl = ",Tl,"K")

# Calculando a distribuicao
listaTl = []
for x in np.arange(0,0.21,0.01):
    theta= math.cosh(m*(l-x)) + (h/(m*k))*math.sinh(m*(l-x))
    delta = theta/thetab
    Tl = delta*(Tb-Tinf) + Tinf
    listaTl.append(Tl)


plt.figure()
plt.plot(np.arange(0,0.21,0.01),listaTl)
plt.scatter(0.2,Tl, color="red")


plt.legend(["Tl",f"Tl na extremidade {Tl:0.3f}"])
plt.grid()
plt.xlabel("l(m)")
plt.ylabel("Tl(K)")

plt.show()

#CALCULOS EX2------------------------------------------------------------------------------------------

M = (Tb-Tinf)*(math.sqrt(h*p*k*a))
print("M = ",M)

qa = M*((math.sinh(m*l) + (h/(m*k))*math.cosh(m*l))/(math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)))

print("qa = ",qa)

#CALCULOS EX3------------------------------------------------------------------------------------------
ef = qa/(h*a*thetab)

print("eficiencia = ",ef)

#CALCULOS EX4------------------------------------------------------------------------------------------
As = a + (2 * math.pi * (D/2)) * l # area da superficie
efet = qa/(h*As*(thetab))

print("efetividade = ",efet)

#CALCULOS EX5------------------------------------------------------------------------------------------




