""" 
--- Exercício 3  - Funções
--- Escreva uma função para listar pessoas cadastradas:
---    a função deve retornar todas as pessoas cadastradas na função do ex1
--- Escreva uma função para exibi uma pessoa específica:
        a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id 
"""

from cadastrando_pessoas import pessoas

def listar_pessoas_cadastradas(pessoas):
    print(f'Quanditade de pessoas cadastradas: {len(pessoas)}')
    return pessoas
    
listar_pessoas_cadastradas(pessoas)

def escolha(id_pessoa):
    for pessoa in pessoas:
        if pessoa['i_d'] == id_pessoa:
            print(pessoa)

