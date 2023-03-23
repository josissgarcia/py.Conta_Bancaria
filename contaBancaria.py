class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    
    def depositar(self, valor):
        self.saldo += valor
        
    
    def sacar(self, valor):
        if(valor <= self.saldo):
            self.saldo -= valor
        else:
            print("Seu saque não será realizado, Saldo insuficiente!")

    def consultarSaldo(self):
        print(f"O seu Saldo atual sr(a) {self.titular} é: R$ {self.saldo:.2f}")
        
