from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights) #pop을 편하게 하기 위해 deque 사용
    print(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)]) #다리 위 Truck 확인 위한 배열
    bridge_weight = 0 # 현재 다리 위 무게
    time = 0 # 통과 시간 확인
    
    while len(bridge) != 0: # 다리위에 아무 것도 없을때 까지 실행
        out = bridge.popleft() # 다리위에서 나오면 pop 실행
        bridge_weight -= out # 다리위 무게 감소
        time += 1 # 다리위에 차 있으면 시간 계속 증가
        if truck_weights: # truck_weight가 존재하면
            if  bridge_weight + truck_weights[0] <= weight:
                # pop했기 때문에 항상 0번째 값만 비교해도 됨
                temp = truck_weights.popleft()
                bridge_weight += temp
                bridge.append(temp)
                #print ("여기", bridge)
            else:
                bridge.append(0)
               # print(bridge)
               # print ("else", bridge)
    print (time)
    return time

solution (2, 10, [7, 4, 5, 6])