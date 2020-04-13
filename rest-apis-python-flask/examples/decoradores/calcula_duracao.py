import time

# definição de decorator para calcular duração entre inicio e final da função
def calcula_duracao(funcao):
    def wrapper(*args, **kwargs):
        tempo_inicial = time.time()
        funcao(*args, *kwargs)
        tempo_final = time.time()
        tempo_execucao = tempo_final - tempo_inicial

        print(f"[{funcao.__name__}] Tempo de execução: {tempo_execucao}")

    return wrapper