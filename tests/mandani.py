from cProfile import label
from nis import cat
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from fuzzy.membership_function import Membership_Function as MF
from utils.graphs import Graph
from fuzzy.operators import Union
import skfuzzy as fuzz

point_n = 200
x = np.linspace(-10,  10, point_n, endpoint=True) # Definindo intervalo dos antecedentes
y = np.linspace(  0,  10, point_n, endpoint=True) # Definindo intervalo dos consequentes

ante = np.array([
    MF.trapezoidal(x,-20, -15, -6, -3), # A1
    MF.trapezoidal(x, -6,  -3,  3,  6), # A2 
    MF.trapezoidal(x,  3,   6, 15, 20)  # A3
])
cons = np.array([
    MF.trapezoidal(y,-2.46,-1.46, 1.46, 2.46), # B1
    MF.trapezoidal(y, 1.46, 2.46,    5,    7), # B2
    MF.trapezoidal(y,    5,    7,   13,   15)  # B3
])

'''
    Regras de ativação
    > Se x1 é A1, então y é B3
    > Se x1 é A2, então y é B2
    > Se x1 é A3, então y é B1
'''

output = list()
for active in range(y.shape[0]):
    w = np.array([
        np.minimum(ante[0][active], ante[0]),
        np.minimum(ante[1][active], ante[1]),
        np.minimum(ante[2][active], ante[2])
    ])
    actv_cons = np.array([
        np.minimum(ante[0][active], cons[2]),
        np.minimum(ante[1][active], cons[1]),
        np.minimum(ante[2][active], cons[0]),
    ])

    single_out = np.array([Union.maximum(actv_cons)])

    output.append(fuzz.defuzz(y, single_out, 'lom'))

    '''if (active%120) == 0:
    
        Graph.inline_plot(
            data=np.array([
            ante,
            cons,
            w,
            np.concatenate((actv_cons, single_out),axis=0)]),
            range=x,
            multi_range=[x,y,x,y],
            path_save=f"../images/mandani/100tests/teste{active}.png",
            show=False,
            active_legend=True,
            legend_size=13,
            title=f"Método de Mandani para o ponto: {active}",
            subtitle=['Antecedente', 'Consequente', 'Ativação do antecedente', 'Ativação do consequente'],
            label=[
                ['A1','A2','A3'],
                ['B1','B2','B3'],
                ['A1','A2','A3'],
                ['B1','B2','B3',f'out: {output[active].round(2)}']
            ],
            fill=[
                [False,False,False,],
                [False,False,False,],
                [False,False,False,],
                [False,False,False,True],]) '''

plt.title("Relação de entrada saída",fontsize=22, fontweight ="bold")
plt.plot(x,x,'--', label="input",linewidth='3')
plt.plot(x,output, label="output", linewidth='3')
plt.legend()
plt.savefig("../images/mandani/defuzz.png")
plt.show()