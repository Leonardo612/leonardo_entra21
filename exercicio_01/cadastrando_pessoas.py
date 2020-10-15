""" 
--- Exercício 1  - Funções
--- Escreva uma função para cadastro de pessoa:
---       a função deve receber três parâmetros, nome, sobrenome e idade
---       a função deve salvar os dados da pessoa em uma lista com escopo global
---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
---       A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada 
"""

#=== escopo global
pessoas = []

def cadastrar_pessoas(nome, sobrenome, idade):
    
    if idade < 18:
        print("Idade não permitida!")
       
    else:
        pessoa = {'nome': nome,'sobrenome': sobrenome,'idade': idade}
        pessoa['i_d'] = len(pessoas) + 1
        pessoas.append(pessoa)
        print("Pessoa cadrastrada!")
        return pessoas



