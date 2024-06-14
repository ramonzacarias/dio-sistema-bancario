menu = """
#### MENU ####

[d] - depositar
[s] - sacar
[e] - extrato
[q] - sair

"""


saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    print(menu)
    
    opcao = input("Digite a opção: ")
    
    if opcao == 'd':
        
        valor = float(input("Informe o valor do depósito R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Erro na operação. Informe um valor válido")
            
        
    elif opcao == 's':
        
        if numero_saques < LIMITE_SAQUES:
            
            valor = float(input("Informe o valor do saque R$ "))
            
            excedeu_saldo = valor > saldo
            
            excedeu_limite = valor > limite
            
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
        
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            
            else:
                print("Operação falhou! O valor informado é inválido.")
                
        
        else:
            print("Limite de saque atingido!")
    
    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == 'q':
        break
        print("Você saiu do sistema")
        
    else:
        print("Opção inválida. Por favor selecionar novamente a operação desejada.")
