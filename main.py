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
    
    def retirar(self):
        if self.disponivel == True:
            self.disponivel = False
            return f'O livro {self.titulo} foi retirado.'
        else:
            return f'O livro {self.titulo} não está disponível.'
    
    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            return f'O livro {self.titulo} foi devolvido.'
        else:
            return f'O livro {self.titulo} já foi devolvido.'

class Revista(Item_biblioteca):
    def __init__(self, titulo, ano, disponivel, edicao, editora):
        super().__init__(titulo, ano, disponivel)
        self.edicao = edicao
        self.editora = editora
    
    def info(self):
        return f"""Título: {self.titulo}
        Ano: {self.ano}
        Disponibilidade: {self.disponivel}
        Edição: {self.edicao}
        Editora: {self.editora}"""
    
    def retirar(self):
        if self.disponivel == True:
            self.disponivel = False
            return f'A revista {self.titulo} foi retirada.'
        else:
            return f'A revista {self.titulo} não está disponível.'
    
    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            return f'A revista {self.titulo} foi devolvida.'
        else:
            return f'A revista {self.titulo} já foi devolvida.'

class DVD(Item_biblioteca):
    def __init__(self, titulo, ano, disponivel, diretor, duracao_mins):
        super().__init__(titulo, ano, disponivel)
        self.diretor = diretor
        self.duracao_mins = duracao_mins
    
    def info(self):
        return f"""Título: {self.titulo}
        Ano: {self.ano}
        Disponibilidade: {self.disponivel}
        Diretor: {self.diretor}
        Duração em minutos: {self.duracao_mins}"""
    
    def retirar(self):
        if self.disponivel == True:
            self.disponivel = False
            return f'O DVD {self.titulo} foi retirado.'
        else:
            return f'O DVD {self.titulo} não está disponível.'
    
    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            return f'O DVD {self.titulo} foi devolvido.'
        else:
            return f'O DVD {self.titulo} já foi devolvido.'