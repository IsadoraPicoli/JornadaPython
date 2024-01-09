import pyautogui
import time

# Esperar 5 segundos para colocar o mouse na posição desejada
time.sleep(5)

# Mostrar a posição (x,y) do mouse.
print(pyautogui.position())