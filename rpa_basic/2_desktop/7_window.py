import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 정보를 가져옴 (vscode)
# print(fw.title) # 현재 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25, fw.top + 20) # fw의 크기가 달라져도 그 좌표를 기반으로 동작하기 때문에 같은위치로 움직임

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("제목 없음"): # 해당 제목의 파일 정보를 읽음
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate() # 해당 파일 제일 앞으로 가져옴 (활성화)


if w.isMaximized == False:
    w.maximize() # 최대화

# if w.isMinimize == False:
#     w.Minimize() # 최소화

w.restore() # 화면 원복

w.close() # 윈도우 닫기