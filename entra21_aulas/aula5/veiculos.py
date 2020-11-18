import sqlite3 

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Veiculo:
    __passageiros = []

    def __init__(self, marca, combustivel, max_passageiros, num_rodas):
        self.marca = marca
        self.combustivel = combustivel
        self.max_passageiros = max_passageiros
        self.num_rodas = num_rodas

    def adicionar_passageiro(self, pessoa:Pessoa):
        self.__passageiros.append(pessoa)
        
    def remover_passageiro(self, pessoa:Pessoa):
        pass

    def get_passageiros(self)-> list:
        return self.__passageiros

conn = sqlite3.connect('veiculo.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE a(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    marca TEXT NOT NULL,
    combustivel TEXT NOT NULL,
    max_passageiros INTEGER NOT NULL,
    num_rodas INTEGER NOT NULL
);
""")

print('Tabela criada com sucesso.')
# isso fecha a conexão
conn.close()

if __name__ == "__main__":
    p = Pessoa("Bruno", 29, "022.121.434-33")
    v = Veiculo("Volksvagem", "Gasolina", 5, 4)

    v.adicionar_passageiro(p)

    print(v.get_passageiros())


