from contas import *
from banco import *
banco = Banco()
senha_gerente = "1234"

def menu_cliente(conta):
    while True:
        print(f"\n===  MENU CLIENTE ({conta.titular}) ===")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            conta.consultar_saldo()
        elif opc == "2":
            valor = float(input("Valor do depósito: R$"))
            conta.depositar(valor)
            banco._salvar()
        elif opc == "3":
            valor = float(input("Valor do saque: R$"))
            conta.sacar(valor)
            banco._salvar()
            
        elif opc == "4":
            break
        else:
            print("Opção inválida!")

def menu_gerente():
    while True:
        print("\n=== MENU GERENTE ===")
        print("1 - Criar conta corrente")
        print("2 - Criar conta poupança")
        print("3 - Listar contas")
        print("4 - Voltar")
        opc = input("Escolha: ")

        if opc in ["1", "2"]:
            numero = input("Número da conta: ")
            titular = input("Nome do titular: ")
            saldo = float(input("Saldo inicial: R$"))

            if opc == "1":
                conta = ContaCorrente(numero, titular, saldo)
            else:
                conta = ContaPoupanca(numero, titular, saldo)

            banco.criar_conta(conta)
        elif opc == "3":
            print("\n=== CONTAS CADASTRADAS ===")
            for c in banco.contas:
                print(f"{c.numero} - {c.titular} - {c.__class__.__name__} - Saldo: R${c.saldo:.2f}")
        elif opc == "4":
            break
        else:
            print("Opção inválida!")

def login_cliente():
    numero = input("Número da conta: ")
    conta = banco.buscar_conta(numero)
    if conta:
        print(f"Bem-vindo(a), {conta.titular}!")
        menu_cliente(conta)
    else:
        print("Conta não encontrada.")

def main():
    while True:
        print("\n=== FAÇA LOGIN ===")
        print("1 - Login Cliente")
        print("2 - Acesso Gerente")
        print("3 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            login_cliente()
        elif opc == "2":
            senha = input("Digite a senha do gerente: ")
            if senha == senha_gerente:
                menu_gerente()
            else:
                print("Senha incorreta!")
        elif opc == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

main()
