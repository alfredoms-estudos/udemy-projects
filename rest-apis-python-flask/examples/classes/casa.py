class Casa:
    def __init__(self, rua, numero):
        self.__rua = rua
        self.__numero = numero

    def enderecoCompleto(self):
        return f"{self.__rua}, {str(self.__numero)}"