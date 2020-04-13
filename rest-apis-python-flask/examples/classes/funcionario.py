class Funcionario:
    __aumento = 1.00
    __salarioPadrao = 1000

    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def dados(self):
            return {'nome': self._nome, 'salario': self._salario}

    def aplicarAumento(self):
        self._salario = self._salario * self.__aumento

    @classmethod
    def definirNovoAumento(cls, aumento):
        cls.__aumento = aumento

    @classmethod
    def comSalarioPadrao(cls, nome):
        return cls(nome, cls.__salarioPadrao)

    @staticmethod
    def soma(num1, num2):
        return num1+num2