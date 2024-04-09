from Funcoes import login
while True:
    user = input("digite o nome do Usuário:")
    pwd = input("digite a senha do Usuário:")
    if login(user, pwd):
        break
    else:
        print("tente novamente")