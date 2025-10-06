from abc import ABC, abstractmethod
class Item_biblioteca(ABC):
    def __init__(self, titulo, ano, disponivel):
        self.titulo = titulo
        self.ano = ano
        self.disponivel = disponivel

    @abstractmethod
    def info(self):
        pass

class Livro(Item_biblioteca):
    def __init__(self, titulo, ano, disponivel, autor, n_paginas):
        super().__init__(titulo, ano, disponivel)
        self.autor = autor
        self.n_paginas = n_paginas
        
    def info(self):
        return f"""Título: {self.titulo}
        Ano: {self.ano}
        Disponibilidade: {self.disponivel}
        Autor: {self.autor}
        Número de páginas {self.n_paginas}"""

class Revista(Item_biblioteca):
    pass
class DVD(Item_biblioteca):
    pass

livro = Livro('Capitães da Areia', '1929', 'Ocupado', 'Jorge Amado', 232)
print(livro.info())