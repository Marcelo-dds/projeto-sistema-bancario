menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: {valor:2f}\n" 

        else:
            print("Operação rejeitada! O valor informado é invalido! ")
    
    elif opcao == "s":
        print("Saque")
    elif opcao == "e":
        print("Extrato")
        break
    
    else:
        print("Operação inválida, por favor selicione novamente a operação desejada.")