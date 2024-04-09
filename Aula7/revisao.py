#instalar o pyautogui
#pip insltall pyautogui

import pyautogui

"""
mover a seta do mouse ate 
respectivamente as coordenadas (X, Y, e a velocidade)

#move de acordo com os paramentros da tela
pyautogui.moveTo(1112, 1052, duration=.5)
#move de acordo com o ponto do mouse levando ele como o ponto (0, 0)
pyautogui.moveRel(0, 100, duration=.5)
pyautogui.moveRel(100, 0, duration=.5)
"""
# salvar o Arquivo
#pyautogui.moveTo(746, 91, duration=.5)
#pyautogui.click(746, 91, duration=.2)
#pyautogui.moveTo(757, 415, duration=.5)
#pyautogui.click(757, 415, duration=.2)

"""
Localizar um item na tela
"""
#salva o codigo
btnXY = pyautogui.locateCenterOnScreen('./aula7/btn_edit.png')
pyautogui.click(btnXY, duration=.2)
btnXY = pyautogui.locateCenterOnScreen('./aula7/btnSave.png')
pyautogui.click(btnXY, duration=.2)