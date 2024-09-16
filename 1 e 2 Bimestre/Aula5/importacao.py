"""
Para ultilozarmos as funções criadas em outros arquivos de codigo
fonte devemos importa-las, para isso ultilizamos o comando importe ou
from import

Exemplo: Impostar todas as funções do arquivo funções 
como mostrado abaixo ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
"""
import Funcoes

base = float(input("digite a base do triângulo:"))
altura = float(input("digite a altura do triângulo:"))

area = Funcoes.calcularAreaTriangulo(base, altura)
print("a Área do triângulo é", area)


