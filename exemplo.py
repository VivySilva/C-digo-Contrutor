from abc import ABC, abstractmethod

# Product


class Casa:
    def __init__(self):
        self._parede = None
        self._piso = None
        self._teto = None
        self._porta = None
        self._janela = None
        self._piscina = None
        self._jardim = None
        self._area_gourmet = None
        self._garagem = None

    def __str__(self):
        return (f"\n{self._parede}, {self._piso}, {self._teto}, "
                f"\n{self._porta}, {self._janela}, "
                f"{'\nPiscina' if self._piscina else '\nSem piscina'}, "
                f"{'\nJardim' if self._jardim else '\nSem jardim'}, "
                f"{'\nÁrea Gourmet' if self._area_gourmet else '\nSem área gourmet'}, "
                f"{'\nGaragem' if self._garagem else '\nSem garagem'}")

    # o @property e .setter de todos os atributos
    @property
    def parede(self):
        return self._parede

    @parede.setter
    def parede(self, value):
        self._parede = value

    @property
    def piso(self):
        return self._piso

    @piso.setter
    def piso(self, value):
        self._piso = value

    @property
    def teto(self):
        return self._teto

    @teto.setter
    def teto(self, value):
        self._teto = value

    @property
    def porta(self):
        return self._porta

    @porta.setter
    def porta(self, value):
        self._porta = value

    @property
    def janela(self):
        return self._janela

    @janela.setter
    def janela(self, value):
        self._janela = value

    @property
    def piscina(self):
        return self._piscina

    @piscina.setter
    def piscina(self, value):
        self._piscina = value

    @property
    def jardim(self):
        return self._jardim

    @jardim.setter
    def jardim(self, value):
        self._jardim = value

    @property
    def area_gourmet(self):
        return self._area_gourmet

    @area_gourmet.setter
    def area_gourmet(self, value):
        self._area_gourmet = value

    @property
    def garagem(self):
        return self._garagem

    @garagem.setter
    def garagem(self, value):
        self._garagem = value

# Abstract Builder


class Builder(ABC):
    @abstractmethod
    def set_parede(self, parede):
        pass

    @abstractmethod
    def set_piso(self, piso):
        pass

    @abstractmethod
    def set_teto(self, teto):
        pass

    @abstractmethod
    def set_porta(self, porta):
        pass

    @abstractmethod
    def set_janela(self, janela):
        pass

    @abstractmethod
    def set_piscina(self, piscina):
        pass

    @abstractmethod
    def set_jardim(self, jardim):
        pass

    @abstractmethod
    def set_area_gourmet(self, area_gourmet):
        pass

    @abstractmethod
    def set_garagem(self, garagem):
        pass

    @abstractmethod
    def build(self):
        pass

# Concrete Builder


class CasaBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._casa = Casa()

    def set_parede(self, parede):
        self._casa.parede = parede
        return self

    def set_piso(self, piso):
        self._casa.piso = piso
        return self

    def set_teto(self, teto):
        self._casa.teto = teto
        return self

    def set_porta(self, porta):
        self._casa.porta = porta
        return self

    def set_janela(self, janela):
        self._casa.janela = janela
        return self

    def set_piscina(self, piscina):
        self._casa.piscina = piscina
        return self

    def set_jardim(self, jardim):
        self._casa.jardim = jardim
        return self

    def set_area_gourmet(self, area_gourmet):
        self._casa.area_gourmet = area_gourmet
        return self

    def set_garagem(self, garagem):
        self._casa.garagem = garagem
        return self

    def build(self):
        casa = self._casa
        self.reset()
        return casa

# Director


class Diretor:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder: Builder):
        self._builder = builder

    def construir_casa_simples(self):
        if self._builder:
            return (self._builder
                    .set_parede("Parede de alvenaria")
                    .set_piso("Piso de cerâmica")
                    .set_teto("Teto de gesso")
                    .set_porta("Porta de madeira")
                    .set_janela("Janela de vidro")
                    .build())
        else:
            raise ValueError("Builder não foi definido")

    def construir_casa_luxuosa(self):
        if self._builder:
            return (self._builder
                    .set_parede("Parede de alvenaria reforçada")
                    .set_piso("Piso de mármore")
                    .set_teto("Teto de gesso com iluminação embutida")
                    .set_porta("Porta de madeira maciça")
                    .set_janela("Janela de vidro temperado")
                    .set_piscina("Piscina aquecida")
                    .set_jardim("Jardim paisagístico")
                    .set_area_gourmet("Área gourmet completa")
                    .set_garagem("Garagem para 4 carros")
                    .build())
        else:
            raise ValueError("Builder não foi definido")


# Client code
diretor = Diretor()

# Construindo uma casa simples
builder_simples = CasaBuilder()
diretor.set_builder(builder_simples)
casa_simples = diretor.construir_casa_simples()
print(casa_simples)

# Construindo uma casa luxuosa
builder_luxuosa = CasaBuilder()
diretor.set_builder(builder_luxuosa)
casa_luxuosa = diretor.construir_casa_luxuosa()
print(casa_luxuosa)
