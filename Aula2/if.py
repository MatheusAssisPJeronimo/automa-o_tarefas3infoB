print('Digite sua idade: ')
idade = int(input())

if idade <= 12:
    print('você é uma criança')
elif idade < 18:
    print('você é um adolecente')
elif idade > 18:
    print('você é um Adulto')

idade = idade + 1
print("No ano que vem sua idade será", idade)