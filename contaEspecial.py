from contaBancaria import ContaBancaria 

class ContaEspecial(ContaBancaria):         #Herança
    def bajularCliente(self):
        print("Gostaria de um café?")
        

clienteIndra = ContaEspecial("Indra", 1200.885) # Objeto
print(f"Nome do cliente: {clienteIndra.titular} Saldo:{clienteIndra.saldo:.2f}")

clienteIndra.depositar(30000.00)
clienteIndra.consultarSaldo()

clienteIndra.sacar(500.00)
clienteIndra.consultarSaldo()

clienteNormal = ContaBancaria("Pedro Guilherme", 5000)
print(f'Nome do cliente: {clienteNormal.titular} Saldo: {clienteNormal.saldo:.2f}')

clienteNormal.sacar(1200)
clienteNormal.consultarSaldo()