menu = '''
[1] Depositar
[2] Sacar
[3]Extrato
[0] Sair

'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 1
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input('digite o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido')
        
    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_daques = numero_saques > LIMITE_DE_SAQUES

        if excedeu_saldo:
            print ('Opção falhou! Você nnão tem saldo em conta')
        elif excedeu_limite:
            print('Opção falhou! Você excedeu o limite por saque ')
        elif excedeu_limite_daques:
            print('Opção falhou! N~umero máximo de saques excedido')
        elif valor > 0:
            saldo -= valor
            extrato += f' Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! Valor informado é inválido')



    elif opcao == '3':
        print ('\n================Extrato=================')
        print( 'Não foram realizadas operações' if not extrato else extrato)
        print(f'\nSaldoo R$ {saldo:.2f}')


    elif opcao == '0':
        print ('Você saiu')
        break
    else:
        print ( 'Opção inválida \nPor favor digite novamente a opção desejada')