""" 
--- Exercício 4  - Funções
--- Escreva uma função para listar endereços cadastrados:
---    a função deve retornar todos os endereços cadastrados na função do ex2
--- Escreva uma função para exibir um endereço específico:
        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
            id da pessoa 
"""

from cadastrando_endereco import enderecos

def listar_enderecos_cadastrados(enderecos):
    print('Endereços cadastrados')
    return enderecos
    
listar_enderecos_cadastrados(enderecos)

def escolha_endereco(id_pessoa):
    for endereco in enderecos:
        if endereco['i_d'] == id_pessoa:
            print(endereco)