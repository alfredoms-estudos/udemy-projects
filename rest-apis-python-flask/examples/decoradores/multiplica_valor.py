# definição de decorator para calcular duração entre inicio e final da função
def multiplica_valor(valor):
    def internal(funcao):
        def wrapper(*args, **kwargs):
            return funcao(*args, *kwargs) * valor
        
        return wrapper

    return internal