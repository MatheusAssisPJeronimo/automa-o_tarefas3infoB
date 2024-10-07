from selenium import webdriver

#cria um objeto do webdriver que vai manipular o chrome 
Chrome = webdriver.Chrome()
# - Edge = webdriver.Edge()

#abre um endereço no navegador = get
Chrome.get('http://www.google.com') 
# - Edge.get('http://www.google.com')

#esperar digitar algo para fechar o navegador 
input('Aperte enter para terminar')