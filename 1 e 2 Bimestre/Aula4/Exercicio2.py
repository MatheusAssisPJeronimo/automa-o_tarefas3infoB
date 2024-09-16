"""
Criar um programa que recebe 2 numeros reais como entrada e um operador
matematico. de acordo com o operador matemático fornecido. O programa 
deve calcular e arpesentar o resultado da operação.
EX de entrada...
1.2
2.3
+

EX de Saida...
o resultado da soma é 3.5
"""
num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
operador = input("Entre com um operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    print("Operador inválido")
    resultado = None

if resultado is not None:
    print(f"O resultado da {operador} entre {num1} e {num2} é {resultado}.")