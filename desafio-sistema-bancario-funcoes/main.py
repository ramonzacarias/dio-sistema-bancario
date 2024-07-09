import textwrap

def menu():
    menu = """
    #### MENU ####

    [d] - depositar
    [s] - sacar
    [e] - extrato
    [nu] - novo usuario
    [nc] - criar conta
    [lc] - listar contas
    [q] - sair

    """
    
    return print(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Operação depósito realizado com sucesso!")

    else:
        print("Erro na operação. Informe um valor válido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    
    elif excedeu_saques:
        print("Limite de saque atingido!")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            AgÊncia:\t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def main():
    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    usuarios = []
    contas = []

    while True:

        menu()

        opcao = input("Digite a opção: ")

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito R$ "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )            

        elif opcao == 'e':
            mostrar_extrato(saldo, extrato=extrato)
            
        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == 'lc':
            listar_contas(contas)
                        
        elif opcao == 'q':
            break
            print("Você saiu do sistema")

        else:
            print("Opção inválida. Por favor selecionar novamente a operação desejada.")

main()
