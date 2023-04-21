'''
===============  Escopo Básico: ================
Para determinar uma solução para f(x) = 0, dada uma aproximaçao aprox

Entradas:  aprox (aproximação) , tol (tolerancia), Nmax (n maximo de interações)
Saida: solução aproximada ou msg de erro

iteracoes = 1
while i < Nmax
    p = aprox - f(aprox)/f'(aprox)
    if (abs(p-aprox) < tol)
        print("Aproximação feita com sucesso!")
        return p
    iteracoes +=1
    aprox = p

print("O metodo falhou após Nmax iteracoes")
'''
import numpy as np
## Ex 01


def f(x): return x*x - 6
def df(x): return 2*x


def Metodo_Newton(p0, tol, iteracoes):
    i = 0
    while i < iteracoes:
        p = p0 - f(p0)/df(p0)
        if abs(p-p0) < tol:
            print(f"Aproximação bem sucedida apos {iteracoes} iteracoes")
            return p
        print( f"Iteracao {i}: {p}")
        i += 1
        p0 = p
    print(f"O metodo falhou apos {iteracoes} iteracoes")
    return p


## Ex 01
# def f(x): return x*x - 6
# def df(x): return 2*x
# print(Metodo_Newton(3, 0.00001, 10))

##Ex 02
# def f(x): return x*x*x + np.cos(x)
# def df(x): return 3*(x*x) - np.sin(x)
# print(Metodo_Newton(-2, 10**(-5), 10))
import math
def f(x): 
    return 1/2 + (x*x)/4 - x*np.sin(x) - np.cos(2*x)

def df(x): return x/2 - np.sin(x) -x*np.sin(x) + np.sin(2*x)/4

print(Metodo_Newton(5*np.pi, 10**(-5), 100))





