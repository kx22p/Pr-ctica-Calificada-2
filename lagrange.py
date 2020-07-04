import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#INGRESO DE DATOS

xi = np.array([-3, -1, 2, 4])
fi = np.array([0, 4, 3, 1])

#PROCEDIMIENTO

n = len(xi)
x = sym.Symbol('x')
polinomio = 0
for i in range(0,n,1):
	numerador = 1 
	denominador = 1
	for j in range(0,n,1):
		if (i!=j):
			numerador = numerador*(x-xi[j])
			denominador = denominador*(xi[i]-xi[j])
		termino = (numerador/denominador)*fi[i]
	polinomio = polinomio + termino
polisimple = sym.expand(polinomio)

px = sym.lambdify(x,polinomio)

#VECTORES PARA GRAFICAS

muestras = 51
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)

#SALIDA

print('polinomio: ')
print(polinomio)
print('polisimple: ')
print(polisimple)

#GRAFICA

plt.plot(xi,fi,'o')
plt.plot(p_xi,pfi)
plt.show()
