from http.client import PAYMENT_REQUIRED
import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoeCoding", interval=1) # interval을 통해 글자 당 딜레이를 줄 수 있음
# pyautogui.write("나도코딩") # 영문과 숫자만 입력 가능 (한글만 입력시 입력 안됨)

# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25) # 왼쪽, 왼쪽, 오른쪽, 엔터 # automate the boring stuff with python 사이트에서 chapter20, keyboard attribute 에서 확인 가능

# 특수 문자
# shift 4 -> $
pyautogui.keyDown("shift") # shift 키를 누른 상태에서
pyautogui.press("4") # 4를 입력하고
pyautogui.keyUp("shift") # shift키를 뗀다

# 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl") # cral + a

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a") # ctl > alt > shift > a 누르고 나서 > a떼고 > shift 뗴고 > alt 뗴고 > ctrl 뗌
# pyautogui.hotkey("ctrl", "a")

# # 한글 처리 방법 (클립보드 활용)
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    
my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del