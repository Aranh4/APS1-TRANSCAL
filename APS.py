import math
import matplotlib.pyplot as plt
import numpy as np

#Determine a temperatura da 
# extremidade da haleta de aluminio e a 
# taxa de trasferncia de forma analitica


#DADOS
l = 0.2 #metros
D = 0.24 #metros
r = D/2 #metros
p = math.pi * 2*r  #metros
ab = math.pi*r**2 #metros
h = 25 #W/m^2.K
k = 240 #W/m.K
Tinf =  273+25 #K
Tb = 373 #K
m = math.sqrt((h*p)/(k*ab)) #m^2/s   

#CALCULOS EX1------------------------------------------------------------------------------------------

theta = math.cosh(0) + (h/(m*k))*math.sinh(0)

thetab= math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)

delta = theta/thetab
# print(theta)
# print(thetab)
# print(math.cosh(m*l))
# print(delta)

Tl = delta*(Tb-Tinf) + Tinf
print("Tl = ",round(Tl, 2),"K")

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

M = (Tb - Tinf)*(math.sqrt(h*p*k*ab))
print("M = ",round(M, 2))

qa = M*((math.sinh(m*l) + (h/(m*k))*math.cosh(m*l))/(math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)))

print("qa = ",round(qa, 2))

#CALCULOS EX3------------------------------------------------------------------------------------------

As = ab + (2 * math.pi * (D/2)) * l # area da superficie
eficiencia = qa/(h*As*(Tb-Tinf))

print("eficiencia = ",round(eficiencia*100, 2), "%")

#CALCULOS EX4------------------------------------------------------------------------------------------

efetividade = qa/(h*ab*(Tb-Tinf))
print("efetividade = ", round(efetividade, 2))

#CALCULOS EX5------------------------------------------------------------------------------------------

#para aleta infinita qa = a M
qa_infinita = M
print("qa aleta infinita = ",round(qa_infinita, 2))

#CALCULOS EX6------------------------------------------------------------------------------------------

def compara(a, b):
    nomes = ['qa', 'M']
    valores = [a, b]

    plt.figure(figsize=(10, 5))
    plt.bar(nomes, valores)

    for i, v in enumerate(valores):
        plt.text(i, v + 0.1, str(round(v, 3)), color='black', fontweight='bold') # round the value to 3 decimal places

    plt.grid()
    plt.show()

compara(qa,qa_infinita)
compararacao = qa/qa_infinita
print("comparacao qa/qa_infinita = ",round(compararacao, 2))

#CALCULOS EX7------------------------------------------------------------------------------------------

# ---------------------------------------- deu errado ----------------------------------------------
# l = 0
# coisa = ((math.sinh(m*l) + (h/(m*k))*math.cosh(m*l))/(math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)))
# while (coisa != 1):
#     l += 0.001
#     coisa = ((math.sinh(m*l) + (h/(m*k))*math.cosh(m*l))/(math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)))
# ---------------------------------------- deu errado ----------------------------------------------

l = 0.001
tole = 0.001
erro = 1
while (erro > tole):
    qa = M*((math.sinh(m*l) + (h/(m*k))*math.cosh(m*l))/(math.cosh(m*l) + (h/(m*k))*math.sinh(m*l)))
    q_inf = M
    erro = abs((qa - q_inf)/q_inf)
    l += 0.001

print("tamanho da aleta para ser igual a hipotese da aleta infinita = ",round(l, 2), "m")	
