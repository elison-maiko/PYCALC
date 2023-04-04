import numpy as np

def funcao_escondida(x):
    return int(x)


def escondida_par(x):
    if (funcao_escondida(x)) % 2 == 0:
        return True
    else: 
        return False



def norma_op(A):
    return np.linalg.norm(A)

def apaga_par (L):
    i=0
    while i < len(L):
        if e_par ( L[i]) :
            L =  L[:i] + L[i+1:]
            i+=1
            #return
            #L = L[:i]+ L[i+1:]
            #print(L)
        else :
            i+=1
    return L
    
def e_par(x):
    if x % 2 == 0:
        return True
    else: 
        return False

Lista = np.array([1,2,3,4,5,6,7,8,9,10])

print(f"teste: {apaga_par(Lista)}")

