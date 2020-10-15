""" --- Exercício 5  - Funções
--- Escreva um programa para cadastro de pessoas e endereços:
---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
---       o programa deve solicitar os dados de endereços utilizados na função do ex2
---       o programa deve passar o id obtido na função do ex1 para a função do ex2
---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
                com seus respectivos endereços utilizando as funções do ex3 e ex4 
"""

from cadastrando_pessoas import cadastrar_pessoas
from cadastrando_endereco import cadastrar_enderecos,enderecos
from listar_pessoas import listar_pessoas_cadastradas,escolha
from listar_enderecos import listar_enderecos_cadastrados,escolha_endereco
from lista_de_cadastros import salvar_cadastros

print('Cadastrando pessoas: ')
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

cadrastros = cadastrar_pessoas(nome, sobrenome, idade)


print('Cadastando endereços: ')
i_d = len(cadrastros) 
rua = input('Digite sua rua: ')
numero = input('Digite seu numero: ')
complemento = input('Digite o complemento: ')
bairro = input('Digite o seu bairro: ')
cidade = input('Digite a sua cidade: ')
estado = input('Digite seu Estado: ')



cadastrar_enderecos(i_d, rua, numero, complemento, bairro, cidade, estado)



id_pessoa = int(input("Digite o id: "))
escolha(id_pessoa)
escolha_endereco(id_pessoa)



