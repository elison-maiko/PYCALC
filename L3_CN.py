def potencia(base, exp):
    '''
    Calcula a potencia de um numero dado a base e o expoente
    '''
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado

def fatorial(n):
    """
    Calcula o fatorial de um número inteiro não negativo.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def sin(x):
    resultado = 0
    for i in range (0,15):
        expoete = (2*i)+1
        termo = (potencia(-1,i)) * potencia (x, expoete) / fatorial(expoete)
        resultado += termo
    return resultado

def cos(x):
    resultado = 0
    for i in range (0,15):
        expoete = (2*i)
        termo = (potencia(-1,i)) * potencia (x, expoete) / fatorial(expoete)
        resultado += termo
    return resultado


def invsqrt(x):

    for i in range(0,30):
        termo = potencia((-1),i) * fatorial(2*i) * potencia(x-1, i) / (potencia(fatorial(i),2) * potencia(4,i))
        resultado =+ termo

    return resultado


def ordena(L):
    
    n = len(L)
    Ln = []
    for k in range(n):
        Ln.append(L[k])
 

    for i in range(n):
        for j in range(i+1, n):
            if Ln[j] < Ln[i]:
                Ln[i], Ln[j] = Ln[j], Ln[i]
                
    return Ln


def logaritmos_base2(x):
    if x <= 0:
        return float('nan')




def Collatz(x0):
    cont = 0
    while x0 != 1:
        if x0 % 2 != 0: #verifica se é impar
            x0 = 3*x0 + 1
        else:
            x0 = x0/2
        cont +=1
    return cont


        





print("Resultados: ")
print(Collatz(3732423))
