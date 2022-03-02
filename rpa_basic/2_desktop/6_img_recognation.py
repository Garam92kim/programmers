import pyautogui
import time
import sys


# file_menu = pyautogui.locateOnScreen("file_menu.png") # 현재 화면 내에서 해당 파일의 위치를 찾아서 정보를 반환함
# print(file_menu)
# pyautogui.click(file_menu)

# add_icon = pyautogui.locateOnScreen("add.png")
# pyautogui.moveTo(add_icon) # 전체 화면에서 찾아서 시간이 좀 오래 걸림 # 이미지를 못찾으면 None으로 출력됨

# for i in pyautogui.locateAllOnScreen("check_box.png"): # 모든 정보를 다 가져옴, 여러개이기 때문에 for 사용 # 같은 이미지 모두 클릭함
#     print(i)
#     pyautogui.click(i)

# checkbox = pyautogui.locateOnScreen("check_box.png") # 처음 발견하는 같은 이미지를 클릭 한 후 끝냄
# pyautogui.click(checkbox)


# 속도 개선을 위한 방법
# 1. GrayScale : 흑백으로 전환 후 찾기 때문에 공식 문서상 30% 정도 개선된 속도로 찾을 수 있음, 정확도가 조금 떨어질 가능성 있음
# add_icon = pyautogui.locateOnScreen("add.png", grayscale=True)
# pyautogui.moveTo(add_icon)

# # 2. 범위 지정 region(x, y, withe, height)
# add_icon = pyautogui.locateOnScreen("add.png", region=(1120, 796, 200, 200))
# pyautogui.moveTo(add_icon)

# 3. 정확도 조정
# add_icon = pyautogui.locateOnScreen("add.png", confidence = 0.9) # 0.9 = 90% 이상 일치 시 같은 이미지로 판단
# pyautogui.moveTo(add_icon)

# 자동화 대상 이미지가 바로 보여지지 않는 경우 (로딩등의 딜레이가 필요한 경우)
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# while file_menu_notepad is None: # while문을 통해 기다리다가 img 발견 시 넘어가게 됨
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
    
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (Timeout)
timeout = 10 # 10초 대기하도록 
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초 초과시
#         print("시간 종료")
#         sys.exit()
# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target # while문 나올때 target이 none일수도 아닐수도 있음
    
def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[timeout {timeout}s] Target not fount ({img_file}). Terminate programm")
        sys.exit()
        
my_click("file_menu_notepad.png", 10)