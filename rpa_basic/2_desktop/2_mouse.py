import pyautogui

# 절대 좌표로 이동
# pyautogui.moveTo(200, 100) # 지정한 위치로 마우스를 이동 (x,y) 축 (왼쪽 제일 위가 0,0)
# pyautogui.moveTo(100, 200, duration=0.25) # 0.25초로 100,200로 이동

# 현재 커서가 있는 위치로부터 이동
# pyautogui.moveTo(100, 200, duration=0.25)
# print(pyautogui.position()) # 마우스 커서 위치 
# pyautogui.move(100, 200, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 200, duration=0.25)
# print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y) # 둘이 같음