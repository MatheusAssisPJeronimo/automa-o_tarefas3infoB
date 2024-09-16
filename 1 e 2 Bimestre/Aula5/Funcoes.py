"""
As funções são ultilizadas para modularizar o código, ou seja, dividi-lo
em partes menores, que podem ser reutilizadas.

ESTRUTURA:

def name_função(param1, param2):
    faz algo
    return valor
"""
#Exemplos:
#ex1:
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

#ex2:
def login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False
"""
#chamar a função
print(login("Matheus", "123"))

area2 = calcularAreaTriangulo(100, 50)
print("a Area do triangulo é", area2)

"""