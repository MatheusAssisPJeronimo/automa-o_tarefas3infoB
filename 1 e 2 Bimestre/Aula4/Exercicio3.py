"""
Criar um programa que execute repetidamente o programa do exercicio 2.
Após a apresentação do resultado o programa deve pergunar se o 
usuario deseja continuar a calcular, se a resposta for S(sim) o programa 
deve continuar, se a resposta for N(não) o programa deve terminar.
"""

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    operador = input("Digite o operador matemático (+, -, *, /): ")

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':

        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error Error Error Error Error... Divizões com zero não são permitidas")
            continue
    else:
        print("Operador inválido.")
        continue

    print("Resultado:", resultado)

    continuar = input("Deseja continuar calculando? (S/N): ").upper()
    while continuar not in ['S', 'N']:
        print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
        continuar = input("Deseja continuar calculando? (S/N): ").upper()

    if continuar == 'N':
        break