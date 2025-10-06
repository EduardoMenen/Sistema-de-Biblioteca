# 📚 Sistema de Biblioteca — Programação Orientada a Objetos (POO)

Este projeto demonstra os principais conceitos de **Programação Orientada a Objetos (POO)** em Python através da modelagem de uma **biblioteca**, contendo diferentes tipos de itens: **livros**, **revistas** e **DVDs**.

## 🚀 Objetivo

Aplicar os fundamentos da POO — **abstração**, **herança**, **polimorfismo** e **encapsulamento** — na criação de classes que representam itens de uma biblioteca e seus respectivos comportamentos, como **empréstimo** e **devolução**.

## 🧩 Estrutura das Classes

### 🔸 Classe Abstrata: `Item_biblioteca`
Classe base que define os atributos e métodos comuns a todos os itens.

**Atributos:**
- `titulo`: título do item
- `ano`: ano de publicação
- `disponivel`: status de disponibilidade (True/False)

**Método abstrato:**
- `info()`: deve ser implementado por todas as subclasses, retornando as informações completas do item.

### 🔸 Subclasses

#### `Livro`
Atributos adicionais:
- `autor`
- `n_paginas`

Métodos:
- `info()` → Exibe informações do livro  
- `retirar()` → Marca o livro como retirado  
- `devolver()` → Marca o livro como devolvido  

#### `Revista`
Atributos adicionais:
- `edicao`
- `editora`

Métodos:
- `info()`
- `retirar()`
- `devolver()`

#### `DVD`
Atributos adicionais:
- `diretor`
- `duracao_mins`

Métodos:
- `info()`
- `retirar()`
- `devolver()`

# Conceitos Aplicados

- Abstração: A classe Item_biblioteca define a estrutura base comum.

- Herança: As classes Livro, Revista e DVD herdam da classe abstrata.

- Polimorfismo: Cada classe implementa seu próprio método info() e comportamentos de retirar() e devolver().

- Encapsulamento: Atributos e métodos organizados por classe, protegendo a lógica interna.

# Estrutura do Projeto

# 📦 mini-projeto-biblioteca
├── biblioteca.py        # Código principal com as classes
├── exemplo_de_uso.py    # Arquivo de testes e exemplos
└── README.md            # Documentação do projeto

# Observações

- O projeto é totalmente orientado a objetos.

- Pode ser expandido facilmente para incluir novas mídias, como audiobooks ou ebooks.

- Ideal para fins didáticos e prática de POO em Python.
