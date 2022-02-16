import threading
import serial

count = 0 # Timer thread 동작을 위함
port = "COM3"
baud = 115200
ser = serial.Serial(port, baud)

def time_thread(): #Timer thread 동작을 위한 함수
    global count
    timer = threading.Timer(1, time_thread)
    timer.start()
    count += 1
    print(count)
    if count > 130: #80초 경과 시 종료
        timer.cancel()
        ser.close()
        
time_thread()

if ser.isOpen() == False:
    ser.open()

while True:
    if ser.readable():
        res = ser.readline()
        try:
            res_str = res.decode("UTF-8")
            if "SW_NUMBER" in res_str:
                count = 0 # WCBS Init 되는 정보가 오면 Count 초기화
                print("PASS, Count Init")

        except ValueError as e:
            print(e)
            continue