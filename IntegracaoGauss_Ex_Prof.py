import numpy as np


def f(t):
    return t * t * np.log(t)


t_nos_2 = [-np.sqrt(3) / 3, +np.sqrt(3) / 3]
C_pesos_2 = [1, 1]

t_nos_3 = [-np.sqrt(15) / 5, 0, np.sqrt(15) / 5]
C_pesos_3 = [5 / 9, 8 / 9, 5 / 9]


def g(s):
    return f(1 + (s + 1) / 4) / 4


Int_2 = C_pesos_2[0] * g(t_nos_2[0]) + C_pesos_2[1] * g(t_nos_2[1])

print("Integral com 2 nos: ", Int_2)

Int_3 = C_pesos_3[0] * g(t_nos_3[0]) + C_pesos_3[1] * g(
    t_nos_3[1]) + C_pesos_3[2] * g(t_nos_3[2])

print("Integral com 3 nos: ", Int_3)

q = lambda x: np.exp(-1 / (x * x)) if (x != 0) else (0)

Int_q_3 = C_pesos_3[0] * q(t_nos_3[0]) + C_pesos_3[1] * q(
    t_nos_3[1]) + C_pesos_3[2] * q(t_nos_3[2])

print("Integral da funcao q com 3 nos: ", Int_q_3)

t_4 = [(1 / 35) * np.sqrt(525 - 70 * np.sqrt(30)),
       -(1 / 35) * np.sqrt(525 - 70 * np.sqrt(30)),
       (1 / 35) * np.sqrt(525 + 70 * np.sqrt(30)),
       -(1 / 35) * np.sqrt(525 + 70 * np.sqrt(30))]
C_4 = [(1 / 36) * (18 + np.sqrt(30)), (1 / 36) * (18 + np.sqrt(30)),
       (1 / 36) * (18 - np.sqrt(30)), (1 / 36) * (18 - np.sqrt(30))]

Int_q_4 = sum([
    C_4[i] * (lambda x: np.exp(-1 / (x * x)) if (x != 0) else (0))(t_4[i])
    for i in range(4)
])

print("Integral da funcao q com 4 nos: ", Int_q_4)

Inttt = sum([
    C_4[i] * (lambda s: np.exp(-1 / ((-0.2 + (1 / 2) * (s + 1))**2))/2 if
              (s != -0.6) else (0))(t_4[i]) for i in range(4)
])

print("Integral: ", Inttt)
