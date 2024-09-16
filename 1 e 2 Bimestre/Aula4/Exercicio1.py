"""
Crie um programa que recebe como entrada dois números reais.
O programa deve imprimir as quatros operações matemáticas entre os dois
números (soma, subtração, divisão e multiplicação)
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"A soma dos números é {soma}")
print(f"A subtração é {subtracao}.")
print(f"A multiplicação é {multiplicacao}.")
print(f"A divisão é {divisao}.")