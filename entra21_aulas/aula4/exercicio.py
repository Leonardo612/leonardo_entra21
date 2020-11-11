# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} {self.idade} {self.cpf}"



passageiros = []
leonardo = Pessoa("Leonardo", "17", "12345678")
pedro = Pessoa("Pedro", "20", "87654321")
maria = Pessoa("Maria","21","12345321")


passageiros.append(leonardo)
passageiros.append(pedro)
passageiros.append(maria)


class Veiculo:
    def __init__(self, numero_de_portas, modelo, tipo, cor, marca):
        self.modelo = modelo
        self.numero_de_portas = numero_de_portas
        self.tipo = tipo
        self.cor = cor
        self.marca = marca
    
    

def adicionar_passageiros():
    print("""
    1) Adicionar passageiro
    2) sair
    """)
    escolha_1 = int(input("Escolha umas das opções: "))
    if escolha_1 == 1:
        nome_adicionar = "LEO"
        idade_adicionar = 34
        cpf_adicionar = 648309
        
        nome_adicionar = (input("Digite o nome da pessoa: "))
        idade_adicionar = int(input("Digite a idade da pessoa: "))
        cpf_adicionar = int(input("Digite o cpf da pessoa: "))
        pessoa_a_adicionar = Pessoa(nome_adicionar, idade_adicionar, cpf_adicionar)
        passageiros.append(pessoa_a_adicionar)
    elif escolha_1 == 2:
        exit
    else:
        print("opção não disponivél")
    
def remover_passageiros():
    print(*passageiros)
    nome_remover = (input("Digite o nome da pessoa para removela: "))
    idade_remover = int(input("Digite a idade da pessoa para removela: "))
    cpf_remover = int(input("Digite o cpf da pessoa para removela: "))
    for i in passageiros:
        if i.nome == nome_remover:
            passageiros.remove(i)
        if i.idade == idade_remover:
            passageiros.remove(i)
        if i.cpf == cpf_remover:
            passageiros.remove(i)
        
    def __str__(self):
        return f''

    def limite_de_velo(self):
        return "indeterminado"
    
    def painel(self):
        return "indeterminado"
    
    def autonomia(self):
        return "indeterminado" 

class Carro(Veiculo):
    def __init__(self, numero_de_portas, modelo, tipo, cor, marca):
        super().__init__(numero_de_portas, modelo, tipo, cor, marca)
    
    def limite_de_velo(self):
        return "220km/h"
    
    def painel(self):
        return "Analogico/digital"

    def autonomia(self):
        return "11km por litro"
class Moto(Veiculo):
    def __init__(self, modelo, tipo, cor, marca):
        super().__init__(None, modelo, tipo, cor, marca)
    
    def limite_de_velo(self):
        return "180km/h"

    def painel(self):
        return "Analogico"
    
    def autonomia(self):
        return "16km por litro"

class Caminhao(Veiculo):
    def __init__(self, numero_de_portas, modelo, tipo, cor, marca):
        super().__init__(numero_de_portas, modelo, tipo, cor, marca)

    def limite_de_velo(self):
        return "160km/h"

    def painel(self):
        return "Analogico"
    
    def autonomia(self):
        return "9km por litro"





ford_focus = Carro(4, "ford focus", "flex", "branca", "Ford")
print(f'{ford_focus.modelo} é {ford_focus.tipo} tem a cor {ford_focus.cor} e a marca e {ford_focus.marca}')

cb_150 = Moto( "cb 150", "gasolina", "vermelha", "honda")
print(f'{cb_150.modelo} usa {cb_150.tipo} tem a cor {cb_150.cor} e a marca e {cb_150.marca}')

fh_460 = Caminhao(2, "FH 460", "disel", "Azul", "Volvo")
print(f'{fh_460.modelo} usa {fh_460.tipo} tem a cor {fh_460.cor} e a marca e {fh_460.marca}')

print("""
1) Adicionar pessoas
2) Remover pessoas 
""")
escolha_3 = int(input("Digite a opção selecionada "))

if escolha_3 == 1:
    adicionar_passageiros()
elif escolha_3 == 2:
    remover_passageiros()
else:
    print("Opção invalida")

print(*passageiros)