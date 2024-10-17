"""def fonction(x):
    res = 1 / x
    return res

print("Entrez les bornes de l'intervalle")
a = float(input("Entrez la borne1: "))
b = float(input("Entrez borne2: "))
n = int(input("Entrez le nombre de subdivisions:"))

h = (b - a) / n

def simpson():
    som = fonction(a) + fonction(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            som += 2 * fonction(x)
        else:
            som += 4 * fonction(x)
    return (h / 3) * som

print(simpson())

import math
e = abs(math.log(2) - simpson())
print(e)"""
"""a=float(input("x0: "))
b=float(input("f(x0): "))
c=float(input("x1: "))
d=float(input("f(x1): "))
e=float(input("x2: "))
f=float(input("f(x2): "))"""

def fonction(x):
    return 2

