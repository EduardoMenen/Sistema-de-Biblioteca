from main import Livro, Revista, DVD

itens = [
    Livro('Capitães da Areia', 1937, True, 'Jorge Amado', 280),
    Livro('Dom Casmurro', 1899, False, 'Machado de Assis', 256),
    Revista('National Geographic', 2024, True, 'Edição 305', 'National Geographic Society'),
    Revista('Superinteressante', 2023, True, 'Edição 412', 'Editora Abril'),
    DVD('Interestelar', 2014, True, 'Christopher Nolan', 169),
    DVD('O Senhor dos Anéis: A Sociedade do Anel', 2001, False, 'Peter Jackson', 178)
]

for item in itens:
    print(item.info())
    print('-' * 40)

for item in itens:
    print(item.retirar())
    print(item.devolver())
    print('-' * 40)
