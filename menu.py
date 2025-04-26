from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('''    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos valores
    [5] sair do programa''')
    opção = int(input('>>>>>Qual é a sua opção? '))
    if opção == 1:
        soma = n1+n2
        print(f'A soma entre {n1} + {n2} é {soma}!')
    elif opção == 2:
        produto = n1*n2
        print(f'A multiplicação entre {n1} * {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
    elif opção == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa')
