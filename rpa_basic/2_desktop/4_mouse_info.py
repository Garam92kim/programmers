import pyautogui
# pyautogui.FAILSAFE = False # 네 모퉁이에 가져다 둬도 멈추지 않음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용됨
# pyautogui.mouseInfo() # mouse의 정보를 나타내주는 tool

# 마우스를 네 모퉁이로 가져다 두면 멈춤
for i in range(10): 
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)