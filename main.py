from abc import ABC, abstractmethod
class Item_biblioteca(ABC):
    def __init__(self, titulo, ano, disponivel):
        self.titulo = titulo
        self.ano = ano
        self.disponivel = disponivel

    @abstractmethod
    def info():
        pass

class Livro(Item_biblioteca):
    pass
class Revista(Item_biblioteca):
    pass
class DVD(Item_biblioteca):
    pass