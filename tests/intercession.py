import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from fuzzy.membership_function import Membership_Function as MF
from fuzzy.operators import Intercession
from utils.graphs import Graph

range, inputs = MF.test_functions(9)

minimum = np.array([Intercession.minimum(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    minimum,
    np.concatenate((minimum,inputs), axis=0)
  ]),
  title="Testes de interseção mínima",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/intercession_min.png",
  label=[
    ['Tri', 'Gaus'],
    ['min'],
    ['min','Tri', 'Gaus']
  ],
  fill=[
    [False,False],
    [True],
    [True,False,False],
  ]
)

product = np.array([Intercession.product(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    product,
    np.concatenate((product,inputs), axis=0)
  ]),
  title="Testes de interseção de produtos",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/intercession_prod.png",
  label=[
    ['Tri', 'Gaus'],
    ['prod'],
    ['prod','Tri', 'Gaus']
  ],
  fill=[
    [False,False],
    [True],
    [True,False,False],
  ]
)

limited_product = np.array([Intercession.limited_product(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    limited_product,
    np.concatenate((limited_product,inputs), axis=0)
  ]),
  title="Testes de interseção de produto limitado",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/intercession_lim_prod.png",
  label=[
    ['Tri', 'Gaus'],
    ['lim_prod'],
    ['lim_prod','Tri', 'Gaus']
  ],
  fill=[
    [False,False],
    [True],
    [True,False,False],
  ]
)

drastic_product = np.array([Intercession.drastic_product(inputs)])

Graph.inline_plot(
  data= np.array([
    inputs,
    drastic_product,
    np.concatenate((drastic_product,inputs), axis=0)
  ]),
  title="Testes de interseção de produto drástico",
  range=range,
  active_legend=True,
  subtitle=['Entradas', 'Saídas', 'Entradas X Saídas'],
  path_save="../images/intercession_dra_prod.png",
  show=True,  
  label=[
    ['Tri', 'Gaus'],
    ['dra_prod'],
    ['dra_prod','Tri', 'Gaus']
  ],
  fill=[
    [False,False],
    [True],
    [True,False,False],
  ]
)