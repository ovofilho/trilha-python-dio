
    
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def depositar(a_saldo, a_valor, a_extrato):
    
    if a_valor > 0:
        a_saldo += a_valor
        a_extrato += f"Depósito: R$ {a_valor:.2f} realizado\n"
        

    else:
        print("Operação falhou! O valor informado é inválido.")
        a_extrato += f"Depósito: R$ {a_valor:.2f} não realizado\n"
    return a_saldo, a_extrato
def sacar(*,a_saldo,a_valor, a_extrato, a_limite, a_numero_de_saques, a_limite_de_saques ):
    
    stotal = a_saldo + a_limite
    if (a_valor > stotal) or (a_numero_de_saques > a_limite_de_saques):
        print(f"Operação não realizada: {'Saldo insuficiente.' if a_valor > stotal else 'limites de saque alcançado'}")
        a_extrato += f"\n Tentativa de Saque de {a_valor} :"
        return a_limite, a_extrato, a_numero_de_saques, a_saldo

    elif a_valor > a_saldo:
        a_valor -=a_saldo
        a_saldo = 0
        a_limite -= a_valor
    
    else:
        a_saldo -= a_valor
    a_numero_de_saques += 1
    a_extrato += f"\n Saque de {a_valor} realizado com sucesso:"
    return a_limite, a_extrato, a_numero_de_saques, a_saldo

def emitir_extrato(saldo,extrato, numero_saques, limite_saques):
    print(extrato)
    print(f"O saldo é {saldo}")
    print(f"O limite de saques é {limite_saques - numero_saques}")

def criar_usuario():
    print("desenvolver criar usuario:")
    
def criar_conta_corrente():
    print("desevolver criar conta conrrente: e vincular com usuario")
    
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            limite, extrato, numero_saques, saldo = sacar(a_saldo=saldo,a_valor=valor,a_extrato=extrato,a_limite=limite,a_numero_de_saques=numero_saques,a_limite_de_saques=LIMITE_SAQUES)
        elif opcao == "e":
            if extrato == "":
                    
                print("\n================ EXTRATO ================")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================")
            else:
                print("\n================ EXTRATO ================")
                emitir_extrato(saldo, extrato, numero_saques, LIMITE_SAQUES)
                print("==========================================")
                
                

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()