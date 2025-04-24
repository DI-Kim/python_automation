# pip install pyautogui
import pyautogui

width , height = pyautogui.size()

pyautogui.position() # 마우스의 포지션을 알려줌 (x, y)

# pyautogui.moveTo(10, 10, duration=1.2)
pyautogui.moveRel(0, 100)
pyautogui.moveRel(-100, -100, duration=0.5)

# pyautogui.click()
# pyautogui.click(100, 200)
# pyautogui.doubleclick(100, 100)
# pyautogui.dragRel(100, 0, duration=0.3)

# error: PyScreeze is not defined >> pip install --upgrade Pillow
pyautogui.displayMousePosition()