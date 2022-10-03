import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from fuzzy.membership_function import Membership_Function as MF
from fuzzy.operators import Union
from utils.graphs import Graph

range, inputs = MF.test_functions(7)

maximum = np.array([Union.maximum(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    maximum,
    np.concatenate((maximum,inputs), axis=0)
  ]),
  title="Testes de união máxima",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/union_max.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['max'],
    ['max','Tri', 'Tra', 'Gaus']
  ],
  fill=[
    [False,False,False,],
    [True],
    [True,False,False,False],
  ]
)

probabilistic_sum = np.array([Union.probabilistic_sum(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    probabilistic_sum,
    np.concatenate((probabilistic_sum,inputs), axis=0)
  ]),
  title="Testes de união soma probabilística",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/union_prob.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['prob_sum'],
    ['prob_sum','Tri', 'Tra', 'Gaus']
  ],
  fill=[
    [False,False,False,],
    [True],
    [True,False,False,False],
  ]
)

limited_sum = np.array([Union.limited_sum(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    limited_sum,
    np.concatenate((limited_sum,inputs), axis=0)
  ]),
  title="Testes de união soma limitada",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/union_lim.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['lim_sum'],
    ['lim_sum','Tri', 'Tra', 'Gaus']
  ],
  fill=[
    [False,False,False,],
    [True],
    [True,False,False,False],
  ]
)

range, inputs = MF.test_functions(8)
drastic_sum = np.array([Union.drastic_sum(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    drastic_sum,
    np.concatenate((drastic_sum,inputs), axis=0)
  ]),
  title="Testes de união soma drástica",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/union_dra.png",  
  label=[
    ['Tri', 'Tra', 'Gaus'],
    ['dra_sum'],
    ['dra_sum','Tri', 'Tra', 'Gaus']
  ],
  fill=[
    [False,False,False,],
    [True],
    [True,False,False,False],
  ]
)