import threading

log_file = open("d:\Python\programmers\pratice\AutomationforWCBS.txt", 'r') # Log 저장 위치
count = 0 # Timer thread 동작을 위함

def startTimer(): #Timer thread 동작을 위한 함수
    global count
    timer = threading.Timer(10, startTimer)
    timer.start()
    count += 1
    print(count)
    if count > 3: #80초 경과 시 종료
        timer.cancel()
        log_file.close()
startTimer()

while True:
    try:
        lines = log_file.readlines() # Log 문자열 저장
        for i in range(0, len(lines)): # SW NUMBER 포함된 문자열 있으면 pass
            if "SW_NUMBER" in lines[i]:
                count = 0 # WCBS Init 되는 정보가 오면 Count 초기화
                print("PASS")
    except ValueError as e:
        print(e)
        break