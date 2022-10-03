import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from fuzzy.membership_function import Membership_Function as MF
from utils.graphs import Graph

''' 
    Essa função tem como objetivo exibir o funcionamento das funções de pertinência definiadas acima
    ao fim da execução será gerado uma imagem que será armazenada em images/membership_example.png
'''
 
range, y_t1 = MF.test_functions(1)
range, y_t2 = MF.test_functions(2)

range, y_tr1 = MF.test_functions(3)
range, y_tr2 = MF.test_functions(4)

range, y_g1 = MF.test_functions(5)
range, y_g2 = MF.test_functions(6)

# Plot do gráfico

fig, axs = Graph.multi_column_plot(line=3,column=2)

axs[0,0].set_title("Triangular", fontsize=18, fontweight ="bold")
for index, function in enumerate(y_t1):
  axs[0,0].plot(range, function, label = 'y_t1' + str(index + 1 ))

axs[0,1].set_title("Triangular", fontsize=18, fontweight ="bold")
for index, function in enumerate(y_t2):
  axs[0,1].plot(range, function, label = 'y_t2' + str(index + 1 ))

axs[1,0].set_title("Trapezoidal", fontsize=18, fontweight ="bold")
for index, function in enumerate(y_tr1):
  axs[1,0].plot(range, function, label = 'y_tr1' + str(index + 1 ))

axs[1,1].set_title("Trapezoidal", fontsize=18, fontweight ="bold")
for index, function in enumerate(y_tr2):
  axs[1,1].plot(range, function, label = 'y_tr2' + str(index + 1 ))

axs[2,0].set_title("Gaussiana", fontsize=18, fontweight ="bold")
for index, function in enumerate(y_g1):
  axs[2,0].plot(range, function, label = 'y_g1' + str(index + 1 ))

axs[2,1].set_title("Gaussiana", fontsize=18, fontweight ="bold")
for index, function in enumerate(y_g2):
  axs[2,1].plot(range, function, label = 'y_g2' + str(index + 1 ))

Graph.format_multi_column_plot(
  axs=axs, 
  line=3,
  column=2, 
  active_legend=True, 
  yticks=np.arange(-0.2,1.01,0.2), 
  path_save="../images/membership_example.png")