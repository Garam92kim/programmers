def solution(numbers):
    answer = ''
    answer_2 = []
    temp = []
    temp_temp_len = 0
    new_list = []
    temp_num = []
    # 첫번째 자리 
    
    # 인수 최대 길이 구하기
    for i in range(len(numbers)):
        temp.append(str(numbers[i]))
        temp_len = len(temp[i])
        if temp_len > temp_temp_len:
            temp_temp_len = temp_len
    
    # 자릿수 맞추기
    for i in range(len(numbers)):
        if len(temp[i]) < temp_temp_len:
            new_list.append(temp[i]+'0'*(temp_temp_len-1))
        else:
            new_list.append(temp[i])
    print("자리수 맞춘 new_list = ", new_list)
    
    tmp = max(new_list)
    index = new_list.index(tmp) # 원래 값 위치 확인용
    print(index)
    nemp_num = sorted(new_list)
    print(nemp_num)
    print(nemp_num[index])
    
    for i in range(len(new_list)):
        if new_list[i][0] > max(new_list):
            
    
    print(numbers[index])
    # 첫번째 자리 먼저 비교하고
    # 두번째 부터 마지막 자리까지 순차 비교하여 정렬
    
    
    
    
    # for i in range(len(new_list)):
    #     for j in range(len(new_list)):
    #         print(f"new_list[i] = {new_list[i]}, new_list[j] = {new_list[j]}, i = {i}, j = {j}")
    #         if new_list[i][0] > new_list[j][0]:
    #             temp = new_list[i]
    #             print("한바퀴 끝 ", temp)
    #         else:
    #             for k in range(temp_temp_len):
    #                 if new_list[i][k] > new_list[j][k]:
    #                     temp_list = new_list[i]
        # answer_2.append(temp)
                    # else:
                    #     answer_2.append(temp_list[i])
        # else:
        #     for k in range(temp_temp_len):
        #         if new_list[i][k] > new_list[j][k]:
        #             temp_list = new_list[i]
        # answer_2.append(temp)
                    # else:
                    #     answer_2.append(temp_list[i])                   
                        
                    # print(f"temp = {new_list[i][k]}, {new_list[j][k]}, i = {i}, j = {j}, k = {k}")
            
            # for k in range(temp_temp_len):
            #     if new_list[i][k] > new_list[j][k]:
            #         print(f"temp = {new_list[i][k]}, {new_list[j][k]}, i = {i}, j = {j}, k = {k}")
                
    return answer

solution([6, 10, 2])