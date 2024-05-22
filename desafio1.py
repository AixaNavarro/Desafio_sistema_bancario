menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo =  0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        valor = float(input('Qual valor deseja depositar? '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}" 
       

        else:
            print('Operação inválida')


    elif opcao =='s':
        valor = float(input('Qual valor deseja sacar? '))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('Operação falhou! Você é pobre')
        elif excedeu_limite:
            print('Operação falhou! Excedeu limite')
        elif excedeu_saques:
            print('Operação falhou! Muitos saques')    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')



    elif opcao == 'e':
        print('========Extrato========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')

