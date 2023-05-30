'''
Esse código realiza testes com os complementos de Zadeh, Sugeno e Yager 
para funções de pertinência. Ele cria gráficos que mostram as entradas, 
as saídas e a combinação das entradas e saídas para cada tipo de complemento. 
Os gráficos são salvos em arquivos de imagem.
'''

import numpy as np
import matplotlib.pyplot as plt 
from fuzzy.membership_function import Membership_Function as MF
from fuzzy.operators import Complement
from utils.graphs import Graph
 
range, input = MF.test_functions(0)

# Fazendo testes com o complmento de Zadeh
zadeh = np.array([
    Complement.zadeh(input[0]),
    Complement.zadeh(input[1]),
    Complement.zadeh(input[2])])

Graph.inline_plot(
  data= np.array([
    input,
    zadeh,
    np.concatenate((input, zadeh), axis=0)
  ]),
  title="Testes com complemento de Zadeh",
  range=range,
  doted=3,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="images/complement_zadeh.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['Zadeh(Tri)', 'Zadeh(Tra)', 'Zadeh(Gaus)'],
    ['Tri', 'Tra', 'Gaus','Zadeh(Tri)', 'Zadeh(Tra)', 'Zadeh(Gaus)']
  ]
)


# Fazendo testes com o complmento de Sugeno
sugeno = np.array([
    Complement.sugeno(input[0],3),
    Complement.sugeno(input[1],4),
    Complement.sugeno(input[2],5)])

Graph.inline_plot(
  data= np.array([
    input,
    sugeno,
    np.concatenate((input, sugeno), axis=0)
  ]),
  title="Testes com complemento de Sugeno",
  range=range,
  doted=3,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="images/complement_sugeno.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['Sugeno(Tri,3)', 'Sugeno(Tra,4)', 'Sugeno(Gaus,5)'],
    ['Tri', 'Tra', 'Gaus','Sugeno(Tri,3)', 'Sugeno(Tra,4)', 'Sugeno(Gaus,5)']
  ]
)


# Fazendo testes com o complmento de Yager
yager = np.array([
    Complement.yager(input[0],3),
    Complement.yager(input[1],4),
    Complement.yager(input[2],5)])

Graph.inline_plot(
  data= np.array([
    input,
    yager,
    np.concatenate((input, yager), axis=0)
  ]),
  title="Testes com complemento de Yager",
  range=range,
  doted=3,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="images/complement_yager.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['Yager(Tri,3)', 'Yager(Tra,4)', 'Yager(Gaus,5)'],
    ['Tri', 'Tra', 'Gaus','Yager(Tri,3)', 'Yager(Tra,4)', 'Yager(Gaus,5)']
  ]
)
