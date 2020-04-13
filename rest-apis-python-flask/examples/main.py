from classes.casa import Casa
from classes.funcionario import Funcionario
from classes.admin import Admin

from decoradores.calcula_duracao import calcula_duracao
from decoradores.multiplica_valor import multiplica_valor
from decoradores.divide_valor import DivideValor

print(" ================= Classes ================= ")

casa1 = Casa("Av. João Dias", 100)
print(f"Endereço completo: {casa1.enderecoCompleto()}")
print(casa1._Casa__numero)

print("\n# Uso de instâncias de classes com herança")
admin = Admin("Joao", 2000)
funcionario1 = Funcionario("Guilherme", 1000)
funcionario2 = Funcionario.comSalarioPadrao("Carlos")

# atualiza dados de todos os funcionários
Funcionario.definirNovoAumento(1.10)

admin.atualizarSalario(2100)
print("Dados do admin: ")
print(admin.dados())

# funcionario.atualizarSalario(2100) ==> funcionario não possui esse método
funcionario1.aplicarAumento()
print("Dados do funcionario #01: ")
print(funcionario1.dados())

funcionario2.aplicarAumento()
print("Dados do funcionario #02: ")
print(funcionario2.dados())

print("\n\n =============== Decoradores =============== ")

@calcula_duracao
def soma(num1, num2):
    print(f"Soma de números: {num1+num2}")

soma(1,2)

@multiplica_valor(2)
def soma2(num1, num2):
    return num1+num2

print(f"Soma de números (x2): {soma2(1,2)}")

@DivideValor(2)
def soma3(num1, num2):
    return num1+num2

print(f"Soma de números (/2): {soma3(2,4)}")
