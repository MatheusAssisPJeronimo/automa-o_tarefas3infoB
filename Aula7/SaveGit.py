import pyautogui

btnXY = pyautogui.locateCenterOnScreen('./aula7/git_btn.png')
pyautogui.click(btnXY, duration=.2)
btnXY = pyautogui.locateCenterOnScreen('./aula7/pesquisa.png')
pyautogui.click(btnXY, duration=.2)