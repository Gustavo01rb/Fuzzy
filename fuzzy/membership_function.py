import numpy as np
import matplotlib.pyplot as plt

class Membership_Function:
    @staticmethod
    def triangle(x,a,m,b):
        y = np.zeros(x.shape[0])                      # Definindo um array de saída do tamnho da entrada.
        first_half = np.logical_and(a < x, x<=m)      # Definindo o intervalo de 'subida' da função.
        y[first_half] = (x[first_half]-a) / (m-a)     # Definindo os valores da saída para o intervalo de 'subida'.
        second_half = np.logical_and(m <= x, x < b)   # Definindo o intervalo de 'descida' da função.
        y[second_half] = (b - x[second_half]) / (b-m) # Definindo os valores da saída para o intervalo de 'descida'.
        return y
    
    @staticmethod
    def trapezoidal(x,a,m,n,b):
        y = np.zeros(x.shape[0])                      # Definindo saída do tamaho da entrada.
        first_part = np.logical_and( a < x, x <= m )  # Definindo o intervalo de subida.
        y[first_part] = (x[first_part] - a) / (m-a)   # Definindo os valores da saída no intervalo de subida.
        second_part = np.logical_and(m < x, x < n)    # Definindo o intervalo entre subida e decida.
        y[second_part] = 1                            # Definindo o valor 1 para todo o intervalo entre subida e decida.
        third_part = np.logical_and(n <= x, x < b)    # Definindo o intervalo de decida.  
        y[third_part] = (b - x[third_part]) / (b-n)   # Defininido os valores de saída para o intervalo de saída.
        return y
    
    @staticmethod
    def gaussian(x,k,m):
        k = k/2
        expoent = (-1)*((x-m)**2)/(k**2)
        return np.exp( expoent )
    
    
    @staticmethod
    def test_functions(type): # Método que retorna várias funções variadas
        range = np.arange(0,100,0.1)
        
        if type == 0: # Retorna uma função de cada tipo de maneira sequêncial
            return range, np.array([
                Membership_Function.triangle(range, 5,15,25),
                Membership_Function.trapezoidal(range, 30,40,60,70),
                Membership_Function.gaussian(range, 10,85)
            ])
        if type == 1: # Retorna vários triângulos com 'm' iguais
            return range, np.array([
                Membership_Function.triangle(range,0 ,50,100 ),  
                Membership_Function.triangle(range,10,50,90  ),
                Membership_Function.triangle(range,20,50,80  ),
                Membership_Function.triangle(range,30,50,70  ),
                Membership_Function.triangle(range,40,50,60  )])
        if type == 2 : # Retorna vários triangulos complementares
            return range, np.array([
                Membership_Function.triangle(range,0,0,20    ),     
                Membership_Function.triangle(range,0,20,40   ),
                Membership_Function.triangle(range,20,40,60  ),
                Membership_Function.triangle(range,40,60,80  ),
                Membership_Function.triangle(range,60,80,100 ),
                Membership_Function.triangle(range,80,100,100),
            ])
        if type == 3: # Retorna vários trapézios com 'n' e 'm' iguais
            return range, np.array([
                Membership_Function.trapezoidal(range,0,40,60,100),
                Membership_Function.trapezoidal(range,10,40,60,90),
                Membership_Function.trapezoidal(range,20,40,60,80),
                Membership_Function.trapezoidal(range,30,40,60,70),
            ])
        if type == 4: # Retorna vários trapezios complementares
            return range, np.array([
                Membership_Function.trapezoidal(range,-1 ,0 ,5 ,15 ), 
                Membership_Function.trapezoidal(range,5 ,15,25,35  ),
                Membership_Function.trapezoidal(range,25,35,45,55  ),
                Membership_Function.trapezoidal(range,45,55,65,75  ),
                Membership_Function.trapezoidal(range,65,75,85,95  ),
                Membership_Function.trapezoidal(range,85,95,100,100)])
        if type == 5:# Retorna várias gaussianas com 'm' iguais
            return range, np.array([
                Membership_Function.gaussian(range,40,50 ),
                Membership_Function.gaussian(range,30,50 ),
                Membership_Function.gaussian(range,20,50 ),
                Membership_Function.gaussian(range,10,50 )])
        if type == 6: # Retorna várias gaussianas complementares
            return range, np.array([
                Membership_Function.gaussian(range,20, 20  ),
                Membership_Function.gaussian(range,20, 0   ),
                Membership_Function.gaussian(range,20, 40  ),
                Membership_Function.gaussian(range,20, 60  ),
                Membership_Function.gaussian(range,20, 80  ),
                Membership_Function.gaussian(range,20, 100 )])
        if type == 7: # Retorna testes para opração de união
            return range, np.array([
                Membership_Function.triangle(range, 5,15,25),
                Membership_Function.trapezoidal(range, 20,50,60,95),
                Membership_Function.gaussian(range, 10,80)
            ])
        if type == 8: # Retorna testes para opração de união
            return range, np.array([
                Membership_Function.triangle(range, 5,15,25),
                Membership_Function.gaussian(range, 10,30)
            ])
        if type == 9: # Retorna testes para opração de interseção
            return range, np.array([
                Membership_Function.trapezoidal(range, 5,20,40,60),
                Membership_Function.gaussian(range, 20,50)
            ])