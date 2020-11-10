class Computador:
    def __init__(self, placa_mae, processador, memoria):
        self.placa_mae = placa_mae
        self.processador = processador
        self.memoria = memoria

    def bench(self):
        print("O total de pontos que esse computador fez foi: 1360")
    
if __name__ == "__main__":
    pc_intel = Computador("asus", "i5", "hyperx")
    print(pc_intel)

    print(isinstance(pc_intel, Computador))
    pc_intel.bench()