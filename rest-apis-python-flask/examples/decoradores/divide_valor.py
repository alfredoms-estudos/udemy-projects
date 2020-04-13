class DivideValor:
  
    def __init__(self, valor): 
        self.valor = valor
  
    def __call__(self, function):

        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs) / self.valor
            return result

        return wrapper