can_log_path = "" # can log 저장 위치
can_log_name = "" # can log 파일 이름
f = open(can_log_path + can_log_name, "r")

def tx_message(data):
    start_data = int(data.find('['))
    end_data = int(data.find(']'))
    print("-"*100)
    tx_id = data[start_data+2:end_data-1].replace(" ", "")
    print(f"ECU Identification ID : {tx_id}")

def rx_message(data, data_list):
    if "62 F" in data:
        start_data = int(data.find('['))
        end_data = int(data.find(']'))
        rx_data = data[start_data+2:end_data-1].replace(" ", "")

        seq_hap = ""
        for line in data_list:
            line = line.strip()
            if "CF Seq.Nr.:" in line:
                start_data = int(line.find('['))
                end_data = int(line.find(']'))
                seq = line[start_data+2:end_data-1].replace(" ", "")
                seq_hap += seq
        print(f"ECU Identification Data : {rx_data}{seq_hap}")
        print("-"*100)

# 파일 Log 출력
while True:
    data = f.readline()
    if "Tx  d 8 03 22 F" in data: # 03 22 f 로 시작하는 message read (Request message)
        tx_message(data)
    elif "62 F" in data: # 62 f로 시작하는 message read (Response message)
        data_list = f.readlines()
        rx_message(data, data_list)