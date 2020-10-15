from cadastrando_pessoas import cadastrar_pessoas,pessoas
from cadastrando_endereco import cadastrar_enderecos,enderecos
from listar_pessoas import listar_pessoas_cadastradas,escolha
from listar_enderecos import listar_enderecos_cadastrados,escolha_endereco


def salvar_cadastros(nome, sobrenome, idade, i_d, rua, numero, complemento, bairro, cidade, estado):
    arquivo = open('cadastros.txt','a')
    arquivo.write(f"""{pessoas['nome']};{pessoas['sobrenome']};{pessoa['idade']};{pessoa['i_d']}/n
    {endereco['rua']};{endereco['complemento']};{endereco['bairro']}; {endereco['cidade']};{endereco['estado' ]};{endereco['i_d']}
    """)
    arquivo.close()

    arquivo = open('cadastros.txt','r')
    for linha in arquivo:
        linha_limpa = linha.strip() 
        lista_dados = linha_limpa.split(';')
        arquivo.close()

salvar_cadastros()
    
