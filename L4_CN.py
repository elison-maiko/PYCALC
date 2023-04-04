import numpy as np

# EX 01 (Com erro não identificado):
def funcao_escondida(x):
    return int(x)


def escondida_par(x):
    if (funcao_escondida(x)) % 2 == 0:
        return True
    else: 
        return False


# Ex 02(Com erro não identificado):
def norma_op(A):
    return np.linalg.norm(A)



# Ex 03:
def apaga_par (L):
    i=0
    while i < len(L):
        if e_par ( L[i]) :
            L =  L[:i] + L[i+1:]
            i+=1
            print(L)
        else :
            i+=1
    return L
    
def e_par(x):
    if x % 2 == 0:
        return True
    else: 
        return False

# Ex04:

# Parte de teste de funções:
