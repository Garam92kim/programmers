import pyautogui

pyautogui.sleep(2)
# print(pyautogui.position())

# pyautogui.click(60, 10) # 60, 10 좌표 클릭
# pyautogui.click(clicks=2) # 2번 클릭하도록 함
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# # pyautogui.click(clicks=500)

# pyautogui.moveTo(300, 300)
# pyautogui.mouseDown()
# pyautogui.moveTo(500, 500)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(852, 142)
# # pyautogui.drag(100, 0, duration=0.25) # 현재 위치 기준으로 100, 0 으로 이동, 너무 빨라서 동작이 제대로 안되면 Duration 사용하면됨
# pyautogui.dragTo(852,500, duration=0.25) # 절대좌표로 이동

pyautogui.scroll(-300) # 위 방향으로 300만큼 스크롤함, -300이면 아래 방향으로 300만큼 스크롤 (양수이면 위, 음수이면 아래)
