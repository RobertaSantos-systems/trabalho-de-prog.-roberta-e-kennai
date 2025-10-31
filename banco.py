from contas import *
import json


class Banco:
    def __init__(self, arquivo="banco.json"):  
        self.arquivo = arquivo
        self.contas = self._carregar()

    def _carregar(self):
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
        contas = []
        for c in dados:
            tipo = c.get("tipo")
            if tipo == "ContaCorrente":
                contas.append(ContaCorrente(c["numero"], c["titular"], c["saldo"]))
            elif tipo == "ContaPoupanca":
                contas.append(ContaPoupanca(c["numero"], c["titular"], c["saldo"]))
        return contas

    def _salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contas], f, ensure_ascii=False, indent=4)

    def criar_conta(self, conta):
        self.contas.append(conta)
        self._salvar()
        print("Conta criada com sucesso!")

    def buscar_conta(self, numero):
        for c in self.contas:
            if c.numero == numero:
                return c
        return None

