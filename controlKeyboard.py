import pyautogui

print(pyautogui.KEYBOARD_KEYS)

pyautogui.click(2500, 1000)
pyautogui.typewrite(['enter', 'enter'])
pyautogui.typewrite('Hello world!', interval=0.1)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.5)
pyautogui.typewrite(['backspace'])
pyautogui.hotkey('ctrl', 'o')