import numpy as np

class Complement:
    @staticmethod
    def zadeh(function):
        """
        Calcula o complemento de Zadeh de uma função.

        Parâmetros:
        - function: np.ndarray ou np.generic
          A função ou array de valores de entrada.

        Retorno:
        - np.ndarray
          O complemento de Zadeh da função de entrada.
        """
        y = np.zeros(function.shape[0])
        y = 1 - function
        return y
    
    @staticmethod
    def sugeno(function, s):
        """
        Calcula o complemento de Sugeno de uma função.

        Parâmetros:
        - function: np.ndarray ou np.generic
          A função ou array de valores de entrada.
        - s: float
          O parâmetro s para o cálculo do complemento de Sugeno.

        Retorno:
        - np.ndarray
          O complemento de Sugeno da função de entrada.
        """
        if s < -1:
            print("Valor de s não aceitável, tente um valor maior ou igual a -1")
            return
        y = np.zeros(function.shape[0])
        y = (1 - function) / (1 + (s * function))
        return y
    
    @staticmethod
    def yager(function, w):
        """
        Calcula o complemento de Yager de uma função.

        Parâmetros:
        - function: np.ndarray ou np.generic
          A função ou array de valores de entrada.
        - w: float
          O parâmetro w para o cálculo do complemento de Yager.

        Retorno:
        - np.ndarray
          O complemento de Yager da função de entrada.
        """
        y = np.zeros(function.shape[0])
        y = (1 - (function ** w)) ** (1 / w)
        return y


class Union:
    @staticmethod
    def maximum(*args):
        """
        Calcula o máximo entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          O máximo entre as funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Parâmetros incorretos ou insuficientes!\n\n")
                return
        a = args[0][0]
        if len(args) == 1:
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                a = np.maximum(a, b)
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = np.maximum(a, b)
        return a
    
    @staticmethod
    def probabilistic_sum(*args):
        """
        Calcula a soma probabilística entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          A soma probabilística das funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Não há parâmetros suficientes para a operação!\n\n")
                return
        if isinstance(args[0], (np.ndarray, np.generic)):
            a = args[0][0]
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                a = a + b - (a * b)
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = a + b - (a * b)
        return a
    
    @staticmethod
    def limited_sum(*args):
        """
        Calcula a soma limitada entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          A soma limitada das funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Não há parâmetros suficientes para a operação!\n\n")
                return
        if isinstance(args[0], (np.ndarray, np.generic)):
            a = args[0][0]
            for b in args[0]:
                a = np.minimum(1, (a + b))
            return a
        a = args[0]
        for b in args:
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = np.minimum(1, (a + b))
        return a

    @staticmethod
    def drastic_sum(*args):
        """
        Calcula a soma drástica entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          A soma drástica das funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Não há parâmetros suficientes para a operação!\n\n")
                return
        if isinstance(args[0], (np.ndarray, np.generic)):
            a = args[0][0]
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                aux = np.zeros(a.shape[0])
                first_verification = np.logical_and(a != 0, b != 0)
                aux[first_verification] = 1
                second_verification = np.logical_and(a == 0, True)
                aux[second_verification] = b[second_verification]
                third_verification = np.logical_and(b == 0, True)
                aux[third_verification] = a[third_verification]
                a = aux
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            aux = np.zeros(a.shape[0])
            first_verification = np.logical_and(a != 0, b != 0)
            aux[first_verification] = 1
            second_verification = np.logical_and(a == 0, True)
            aux[second_verification] = b
            third_verification = np.logical_and(b == 0, True)
            aux[third_verification] = a
            a = aux
            return a
        
class Intercession:
    @staticmethod
    def minimum(*args):
        """
        Calcula o mínimo entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          O mínimo entre as funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Parâmetros incorretos ou insuficientes!\n\n")
                return
        a = args[0][0]
        if len(args) == 1:
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                a = np.minimum(a, b)
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = np.minimum(a, b)
        return a
    
    @staticmethod
    def product(*args):
        """
        Calcula o produto entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          O produto das funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Parâmetros incorretos ou insuficientes!\n\n")
                return
        a = args[0][0]
        if len(args) == 1:
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                a = a * b
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            a = a * b
        return a
    
    @staticmethod
    def limited_product(*args):
        """
        Calcula o produto limitado entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          O produto limitado das funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Parâmetros incorretos ou insuficientes!\n\n")
                return
        a = args[0][0]
        if len(args) == 1:
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                a = np.maximum(0, (a + b - 1))
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
        a = np.maximum(0, (a + b - 1))
        return a
    
    @staticmethod
    def drastic_product(*args):
        """
        Calcula o produto drástico entre várias funções ou arrays.

        Parâmetros:
        - args: np.ndarray, np.generic
          Uma ou mais funções ou arrays de valores de entrada.

        Retorno:
        - np.ndarray
          O produto drástico das funções ou arrays de entrada.
        """
        if len(args) < 2:
            if not isinstance(args[0], (np.ndarray, np.generic)) or args[0].shape[0] < 2:
                print("\n\n\nERRO: Não há parâmetros suficientes para a operação!\n\n")
                return
        if isinstance(args[0], (np.ndarray, np.generic)):
            a = args[0][0]
            for index, b in enumerate(args[0]):
                if index == 0:
                    continue
                aux = np.zeros(a.shape[0])
                first_verification = np.logical_and(a == 1, True)
                aux[first_verification] = b[first_verification]
                second_verification = np.logical_and(b == 1, True)
                aux[second_verification] = a[second_verification]
                a = aux
            return a
        a = args[0]
        for index, b in enumerate(args):
            if index == 0:
                continue
            if not isinstance(b, (np.ndarray, np.generic)):
                print(f"Erro: {b} não é um np.array")
            aux = np.zeros(a.shape[0])
            aux = np.zeros(a.shape[0])
            first_verification = np.logical_and(a == 1, True)
            aux[first_verification] = b[first_verification]
            second_verification = np.logical_and(b == 1, True)
            aux[second_verification] = a[second_verification]
            a = aux
            return a
