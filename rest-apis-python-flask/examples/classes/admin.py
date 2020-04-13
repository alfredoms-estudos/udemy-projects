from .funcionario import Funcionario

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizarSalario(self, salario):
        self._salario=salario

    def atualizarNome(self, nome):
        self._nome=nome