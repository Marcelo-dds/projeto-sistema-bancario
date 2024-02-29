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
            extrato += f"Depósito: {valor:.2f}\n" 

        else:
            print("Operação rejeitada! O valor informado é invalido! ")
    
    elif opcao == "s":
        valor = float(input("Informe o valor de saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:

            print("Operação falhou! Você não tem saldo suficiente." )

        elif excedeu_limite:

            print("Operação falhou! o valor do saque execede o limite.")

        elif excedeu_saques:

            print("Operação falhou! Número máximo de saques execedeu o limite. ")
        
        elif valor > 0 :
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saques += 1
            
    elif opcao == "e":
        print("Extrato")
        break
    
    else:
        print("Operação inválida, por favor selicione novamente a operação desejada.")