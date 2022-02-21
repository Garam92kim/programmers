import threading
from datetime import datetime
import serial
import Auto_DB
import Auto_Excel

count = 0 # Timer thread 동작을 위함
port = "COM3"
baud = 115200
ser = serial.Serial(port, baud)
aging_start_time = datetime.today()
execution_count = 0

if ser.isOpen() == False:
    ser.open()

def time_thread(): #Timer thread 동작을 위한 함수
    global count
    timer = threading.Timer(1, time_thread)
    timer.start()
    count += 1
    print(count)
    if count > 130: #130초 경과 시 종료
        aging_end_time = datetime.today()
        execution_time = aging_end_time - aging_start_time
        Auto_Excel.Update_data(aging_start_time, aging_end_time, execution_time, execution_count)
        print("Total test time : ", execution_time)
        print("Number of execution : %d" %execution_count)
        timer.cancel()
        ser.close()      
time_thread()

while True:
    try:
         if ser.readable() == True and ser.isOpen() == True:
            res = ser.readline()
            try:
                res_str = res.decode("UTF-8")
                Auto_DB.Update_DB(datetime.today(), res_str)
                if "SW_NUMBER" in res_str:
                    count = 0
                    execution_count += 1
                    print(res_str)
                    print("PASS, Count init,", "Number of execution : %d" %execution_count)
            except UnicodeDecodeError as f:
                print(f)
                continue
    except AttributeError as e:
        print(e)
        break