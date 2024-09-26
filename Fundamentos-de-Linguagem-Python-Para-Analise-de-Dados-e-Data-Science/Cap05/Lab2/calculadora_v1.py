# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n****************** Calculadora em Python *******************")
print('***                                                      ***')
print('***          Selecione o código do operador              ***')
print('***          1 - Para Adição ( + )                       ***')
print('***          2 - Para Subtração ( - )                    ***')
print('***          3 - Para Multiplicação ( x )                ***')
print('***          4 - Para Divisão ( / )                      ***')
print('***          0 - Para SAIR                               ***')
print('***                                                      ***')
print(60 * "*")

def operacoes(operador, num1, num2):
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        return num1 / num2
    else:
        return 'Operador invalido'

while True:
    operador = int(input('***   Selecione o código do operador: '))
    if operador == 0:
        print('***   Desligando calculadora ...')
        break
    elif operador < 0 or operador > 4:
        print('***   Opção invalida')

    while operador == 1:
        print('***                                                      ***')
        print(60 * "*")
        print('***                                                      ***')

        print('***  Você selecionou 1 - Para Adição ( + )')
        num1 = float(input('***  Digite o primeiro número: '))
        num2 = float(input('***  Digite o segundo número: '))
        resultado = operacoes(operador, num1, num2)
        print(f'***  RESULTADO:  {num1} + {num2} = {resultado}')
        continuar = int(input('***  Deseja continuar? (1-SIM | 0-NÃO) '))
        if continuar == 0:
            print('***                                                      ***')
            print(60 * "*")
            print('***                                                      ***')
            break
        elif continuar == 1:
            pass
        else:
            print('***   Opção invalida')

    while operador == 2:
        print('***                                                      ***')
        print(60 * "*")
        print('***                                                      ***')

        print('***  Você selecionou 2 - Para Subtração ( - )')
        num1 = float(input('***  Digite o primeiro número: '))
        num2 = float(input('***  Digite o segundo número: '))
        resultado = operacoes(operador, num1, num2)
        print(f'***  RESULTADO:  {num1} - {num2} = {resultado}')
        continuar = int(input('***  Deseja continuar? (1-SIM | 0-NÃO) '))
        if continuar == 0:
            print('***                                                      ***')
            print(60 * "*")
            print('***                                                      ***')
            break
        elif continuar == 1:
            pass
        else:
            print('***   Opção invalida')

    while operador == 3:
        print('***                                                      ***')
        print(60 * "*")
        print('***                                                      ***')

        print('***  Você selecionou 3 - Para Multiplicação ( x )')
        num1 = float(input('***  Digite o primeiro número: '))
        num2 = float(input('***  Digite o segundo número: '))
        resultado = operacoes(operador, num1, num2)
        print(f'***  RESULTADO:  {num1} * {num2} = {resultado:.0f}')
        continuar = int(input('***  Deseja continuar? (1-SIM | 0-NÃO) '))
        if continuar == 0:
            print('***                                                      ***')
            print(60 * "*")
            print('***                                                      ***')
            break
        elif continuar == 1:
            pass
        else:
            print('***   Opção invalida')

    while operador == 4:
        print('***                                                      ***')
        print(60 * "*")
        print('***                                                      ***')

        print('***  Você selecionou 4 - Para Divisão ( / )')
        num1 = float(input('***  Digite o primeiro número: '))
        num2 = float(input('***  Digite o segundo número: '))
        resultado = operacoes(operador, num1, num2)
        print(f'***  RESULTADO:  {num1} / {num2} = {resultado}')
        continuar = int(input('***  Deseja continuar? (1-SIM | 0-NÃO) '))
        if continuar == 0:
            print('***                                                      ***')
            print(60 * "*")
            print('***                                                      ***')
            break
        elif continuar == 1:
            pass
        else:
            print('***   Opção invalida')
        


            
