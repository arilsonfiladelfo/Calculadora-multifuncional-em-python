def tabuada():
    multiplicando = int(input('Escolha um número para ter a tabuada do 0 ao 10: '))
    for i in range(11):
        print(f'{multiplicando} x {i} = {multiplicando * i}')

def somar():
    n1 = float(input('Escolha o número que quer somar: '))
    n2 = float(input('Escolha o outro número para soma-lo: '))
    print(f'{n1} + {n2} = {n1 + n2:.2f}')

def subtracao():
    n1 = float(input('Escolha o número para subtrair: '))
    n2 = float(input('Escolha o outro número para subtraí-lo: '))
    print(f'{n1} - {n2} = {n1 - n2:.2f}')

def multiplicacao():
    n1 = float(input('Escolha o número que quer multiplicar: '))
    n2 = float(input('Escolha o outro número para multiplicá-lo: '))
    print(f'{n1} * {n2} = {n1 * n2:.2f}')

def divisao():
    n1 = float(input('Escolha o número que quer dividir: '))
    n2 = float(input('Escolha o outro número para dividi-lo: '))
    while n2 == 0:
        print('Não existe divisão por 0!')
        n2 = float(input('Escolha outro número para o divisor: '))
    print(f'{n1} / {n2} = {n1 / n2:.2f}')

def converter_c_to_f():
    celsius = float(input('Qual a temperatura em °C que deseja converter em Fahrenheit? '))
    fahrenheit = (celsius * 1.8) + 32
    print(f'{celsius}°C convertidos para Fahrenheit é {fahrenheit:.2f}°F')

def converter_f_to_C():
    fahrenheit = float(input('Qual a temperatura em °F que deseja converter em Celsius? '))
    celsius = (fahrenheit - 32) / 1.8
    print(f'{fahrenheit}°F convertidos para Celsius é {celsius:.2f}°C')

while True:
    print('Bem vindo à calculadora')
    print('1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Converter Celsius para Fahrenheit\n6. Converter Fahrenheit para Celsius\n7. Sair')
    escolha = int(input('Escolha a operação desejada: '))

    if escolha == 1:
        somar()
    elif escolha == 2:
        subtracao()
    elif escolha == 3:
        multiplicacao()
    elif escolha == 4:
        divisao()
    elif escolha == 5:
        converter_c_to_f()
    elif escolha == 6:
        converter_f_to_C()
    elif escolha == 7:
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida, tente novamente.')
