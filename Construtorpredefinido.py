from abc import ABC, abstractmethod

# Product
class Edificio:
    def __init__(self):
        self._tipo = None
        self._tamanho = None
        self._andares = None

    def __str__(self):
        return f"Tipo: {self._tipo}, Tamanho: {self._tamanho} m², Andares: {self._andares}"

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, value):
        self._tamanho = value

    @property
    def andares(self):
        return self._andares

    @andares.setter
    def andares(self, value):
        self._andares = value

# Abstract Builder
class Builder(ABC):
    @abstractmethod
    def set_tipo(self, tipo):
        pass

    @abstractmethod
    def set_tamanho(self, tamanho):
        pass

    @abstractmethod
    def set_andares(self, andares):
        pass

    @abstractmethod
    def build(self):
        pass

# Concrete Builder
class EdificioBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._edificio = Edificio()

    def set_tipo(self, tipo):
        self._edificio.tipo = tipo
        return self

    def set_tamanho(self, tamanho):
        self._edificio.tamanho = tamanho
        return self

    def set_andares(self, andares):
        self._edificio.andares = andares
        return self

    def build(self):
        edificio = self._edificio
        self.reset()  # Reset builder after building
        return edificio

# Concrete Builder 1
class CasaBuilder(EdificioBuilder):
    def __init__(self):
        super().__init__()
        self.set_tipo("Casa").set_tamanho(120).set_andares(2)

# Concrete Builder 2
class CasteloBuilder(EdificioBuilder):
    def __init__(self):
        super().__init__()
        self.set_tipo("Castelo").set_tamanho(500).set_andares(10)

# Concrete Builder 3
class BarracoBuilder(EdificioBuilder):
    def __init__(self):
        super().__init__()
        self.set_tipo("Barraco").set_tamanho(30).set_andares(1)

# Director
class Diretor:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder: Builder):
        self._builder = builder

    def construir(self):
        if self._builder:
            return self._builder.build()
        else:
            raise ValueError("Builder não foi definido")

    def criar_edificio(self, tipo):
        builders = {
            "casa": CasaBuilder,
            "castelo": CasteloBuilder,
            "barraco": BarracoBuilder
        }
        builder_class = builders.get(tipo.lower())
        if builder_class:
            self.set_builder(builder_class())
            return self.construir()
        else:
            raise ValueError(f"Tipo de edifício '{tipo}' não reconhecido")

# Client code
diretor = Diretor()

# Construindo uma casa
casa = diretor.criar_edificio("casa")
print(casa)

# Construindo um castelo
castelo = diretor.criar_edificio("castelo")
print(castelo)

# Construindo um barraco
barraco = diretor.criar_edificio("barraco")
print(barraco)
