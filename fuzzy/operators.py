import numpy as np

class Complement:
    @staticmethod
    def zadeh(function):
        y = np.zeros(function.shape[0])
        y = 1 - function
        return y
    
    @staticmethod
    def sugeno(function, s):
        if(s < -1):
            print("Valor de S não aceitável, tente um valor maior ou igual a -1")
            return
        y = np.zeros(function.shape[0])
        y = (1 - function) / (1+(s*function))
        return y
    
    @staticmethod
    def yager(function, w):
        y = np.zeros(function.shape[0])
        y = (1 - (function**w))**(1/w)
        return y

class Union:
    #Definindo funções de máximo
    @staticmethod
    def maximum(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Parâmetros incorretos ou insuficiente!\n\n")
                return
        a = args[0][0]
        if(len(args) == 1):    
            for index, b in enumerate(args[0]):
                if index == 0: continue
                a = np.maximum(a, b)
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = np.maximum(a, b)
        return a
    
    # Definindo a soma probabilística
    @staticmethod
    def probabilistic_sum(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Não há parâmetros suficientes para operação!\n\n")
                return
        if(isinstance(args[0], (np.ndarray, np.generic))):    
            a = args[0][0]
            for index, b in enumerate(args[0]):
                if index == 0: continue
                a = a + b - (a*b)
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = a + b - (a*b)
        return a
    
    #Definindo a soma limitada
    @staticmethod
    def limited_sum(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Não há parâmetros suficientes para operação!\n\n")
                return
        if(isinstance(args[0], (np.ndarray, np.generic))):    
            a = args[0][0]
            for b in args[0]:
                a = np.minimum(1,(a + b))
            return a
        a = args[0]
        for b in args:
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = np.minimum(1,(a + b))
        return a

    #Definindo a soma Drástica 
    @staticmethod
    def drastic_sum(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Não há parâmetros suficientes para operação!\n\n")
                return
        if(isinstance(args[0], (np.ndarray, np.generic))):    
            a = args[0][0]
            for index, b in enumerate(args[0]):
                if index == 0: continue
                aux = np.zeros(a.shape[0])
                first_verification = np.logical_and(a != 0, b != 0)
                aux[first_verification] = 1
                second_verification =  np.logical_and(a == 0, True)
                aux[second_verification] = b[second_verification]
                third_verification =  np.logical_and(b == 0, True)
                aux[third_verification] = a[third_verification]
                a = aux
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            aux = np.zeros(a.shape[0])
            first_verification = np.logical_and(a != 0, b != 0)
            aux[first_verification] = 1
            second_verification =  np.logical_and(a == 0, True)
            aux[second_verification] = b
            third_verification =  np.logical_and(b == 0, True)
            aux[third_verification] = a
            a = aux
            return a
        
class Intercession:

    #Definindo funções de mínimo
    @staticmethod
    def minimum(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Parâmetros incorretos ou insuficiente!\n\n")
                return
        a = args[0][0]
        if(len(args) == 1):    
            for index, b in enumerate(args[0]):
                if index == 0: continue
                a = np.minimum(a, b)
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = np.minimum(a, b)
        return a
    
    #Definindo funções de produto
    @staticmethod
    def product(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Parâmetros incorretos ou insuficiente!\n\n")
                return
        a = args[0][0]
        if(len(args) == 1):    
            for index, b in enumerate(args[0]):
                if index == 0: continue
                a = a * b
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = a * b
        return a
    
    #Definindo funções de produto
    @staticmethod
    def limited_product(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Parâmetros incorretos ou insuficiente!\n\n")
                return
        a = args[0][0]
        if(len(args) == 1):    
            for index, b in enumerate(args[0]):
                if index == 0: continue
                a = np.maximum(0, (a + b - 1))
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
        a = np.maximum(0, (a + b - 1))
        return a

    #Definindo o produto Drástico 
    @staticmethod
    def drastic_product(*args):
        if(len(args) < 2):
            if(not isinstance(args[0], (np.ndarray, np.generic))  or args[0].shape[0] < 2 ):
                print("\n\n\nERRO: Não há parâmetros suficientes para operação!\n\n")
                return
        if(isinstance(args[0], (np.ndarray, np.generic))):    
            a = args[0][0]
            for index, b in enumerate(args[0]):
                if index == 0: continue
                aux = np.zeros(a.shape[0])
                first_verification =  np.logical_and(a == 1, True)
                aux[first_verification] = b[first_verification]
                second_verification =  np.logical_and(b == 1, True)
                aux[second_verification] = a[second_verification]
                a = aux
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0: continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            aux = np.zeros(a.shape[0])
            aux = np.zeros(a.shape[0])
            first_verification =  np.logical_and(a == 1, True)
            aux[first_verification] = b[first_verification]
            second_verification =  np.logical_and(b == 1, True)
            aux[second_verification] = a[second_verification]
            a = aux
            return a
        
