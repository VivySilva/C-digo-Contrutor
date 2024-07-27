class Personagem:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.habilidade = None
        self.frase = None

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Idade: {self.idade}\n"
                f"Habilidade: {self.habilidade}\n"
                f"Frase: {self.frase}\n")

class ConstrutorDePersonagem:
    def __init__(self):
        self.personagem = Personagem()

    def definir_nome(self, nome):
        self.personagem.nome = nome
        return self

    def definir_idade(self, idade):
        self.personagem.idade = idade
        return self

    def definir_habilidade(self, habilidade):
        self.personagem.habilidade = habilidade
        return self

    def definir_frase(self, frase):
        self.personagem.frase = frase
        return self

    def construir(self):
        return self.personagem


construtor_dio = ConstrutorDePersonagem()
dio = (
    construtor_dio.definir_nome("Dio Brando")
    .definir_idade(123)  
    .definir_habilidade("The World")
    .definir_frase("WRYYYYYYYY!")
    .construir()
)

construtor_jotaro = ConstrutorDePersonagem()
jotar = (
    construtor_jotaro.definir_nome("Jotaro Kujo")
    .definir_idade(43)  
    .definir_habilidade("Star Platinum")
    .definir_frase("Yare Yare Daze")
    .construir()
)


print(dio)
print(jotar)
