from collections import deque

def solution(prices):
    prices_deque = deque(prices)
    answer_deque = deque([0 for _ in range (len(prices))])
    prices_deque.append(0)
    count = 0
    answer = []

    for i in range (0, len(prices)):   #i 부터 배열 숫자까지 반복
        count = 0
        count1 = prices_deque[i]
        print ("               첫번째 기준값 %d" %count1)
        for j in range (0, len(prices)): #j부터 배열 숫자까지 반복
            count2 = prices_deque[j]
            print ("    비교값 %d" %count2)
            if (j) <= (i): #j랑 i가 같으면 skip
                print("스킵!!!")
                continue
            if prices_deque[i] <= prices_deque[j]: # i가 i+j보다 낮으면 실행
                print("count 할게!!")
                count += 1
                print ("현재 Count 수는 %d" %count)
                print(answer_deque)
            else:
                print("여기 언제 오는거지")
                break
        answer_deque.popleft()
        answer_deque.append(count)
        print(answer_deque)

    for i in range (0, len(prices_deque)-1):
        temp = answer_deque[i]
        answer.append(temp)

    print(answer)
    return answer

solution([100, 9, 3, 11, 123, 15235, 213])