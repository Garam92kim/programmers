import pyautogui

# img = pyautogui.screenshot() # 현재 화면 스크린샷찍기
# img.save("screenshot.png")

# pyautogui.mouseInfo()

# 84,316 103,153,184 #6799B8

pixel = pyautogui.pixel(84, 316)
print(pixel)

print(pyautogui.pixelMatchesColor(84, 316, (103,153,184))) # 픽셀 값이 같으면 True, 다르면 False