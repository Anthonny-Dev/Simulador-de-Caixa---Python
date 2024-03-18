import math
cedulas = [1, 10, 20, 50]

ci = []
while True:
    print('='*30)
    print('  ','\033[1;36mBANCO DOS PROGRAMADORES\033[m')
    print('='*30)

    valor = int(input('\033[1;31mQual o valor a ser sacado?\033[m'))
    qcedulas = valor / 2
    qcedulasdez = valor // cedulas[1]
    qcedulasvint = valor // cedulas[2]
    qcedulascinq = valor // cedulas[3]

    #qcedulasdezs = valor[0] / cedulas[0]
    #qcedulasvints = valor[0] / cedulas[0]
    #qcedulascinqs = valor[0] / cedulas[0]
    
    '''if valor % 10 == 0:
        #valor - (math.trunc(qcedulasdez) * cedulas[1]) == ' '

        #cedulas[0] == ' ' '''

    print(f'\033[1mTotal de {math.trunc(qcedulasdez)} cédulas de R${cedulas[1]}\n{valor - (math.trunc(qcedulasdez) * cedulas[1])} cédulas de R${cedulas[0]}') 
    print('-' * 30)
    if valor - (math.trunc(qcedulasvint) * cedulas[2]) not in cedulas:
        ci = valor - (math.trunc(qcedulasvint) * cedulas[2])
        ci /10
        math.trunc(ci / 10)
        '''print( math.trunc(ci / 10))'''

    print(f'Total de {math.trunc(qcedulasvint)} cédulas de R${cedulas[2]}\n{math.trunc( ci / 10 )} cédulas de R${cedulas[1]}\n{ ci % 10} cédulas de R${cedulas[0]}')

    if valor - (math.trunc(qcedulascinq) * cedulas[3]) not in cedulas:
        ci = valor - (math.trunc(qcedulascinq) * cedulas[3])
        ci / 10
        math.trunc( ci / 10)
        '''print(math.trunc( ci / 10))'''


    print('-' *30)
    print(f'Total de {math.trunc(qcedulascinq)} cédulas de R${cedulas[3]}\n{math.trunc( ci / 10)} cédulas de R${cedulas[1]}\n{ ci % 10} cédulas de R${cedulas[0]}' )


    #if valor not in cedulas:
        #print(f'Total de {cedulas[0]} cédulas de', valor / cedulas[0])
        #print(f'Total de {cedulas[1]} cédulas de', valor / cedulas[1])



    if qcedulas in cedulas:
        print(f'Total de 2 cédulas de R${qcedulas:.0f}')
        
    if valor in cedulas:
        print(f'Total de 1 cédulas de R${valor}\033m')
 
       
    print('-'*30)

    dec = str(input('\033[1;31mQuer continuar?[S/N]:\033[m')).upper()[0]

    if dec == "N":
        print('\033[1;36mFINALIZANDO O PROGRAMA...\033[m')



    while dec != 'S' or dec != 'N':
        dec = str(input('\033[1;31mQuer continuar?[S/N]:\033[m')).upper()[0]

        break

print('-'*40)