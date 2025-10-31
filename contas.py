import json
import os 

class Conta:
    def __init__(self, numero, titular, transferencia, saldo=0): 
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.transferencia = transferencia

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def transferencia_entre_contas(self, valor, conta_destino):
        # Verifica se o valor é positivo e não excede o saldo
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")

    def exibir_extrato(self):
        print(f"Saldo de {self.titular}: R${self.saldo}")

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__, 
            "numero": self.numero,
            "titular": self.titular,
            "saldo": self.saldo,
            "transferencia": self.transferencia
        }

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0):  
        super().__init__(numero, titular, saldo)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")
        else:
            print("Saldo insuficiente!")

    def to_dict(self):
        d = super().to_dict()
        return d


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0):  
        super().__init__(numero, titular, saldo)

    def to_dict(self):
        d = super().to_dict()
        return d
