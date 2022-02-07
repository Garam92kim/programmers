def solution(prices):
    answer = []
    count = 0
    print (answer)

    for i in range (len(prices)):   #i 부터 배열 숫자까지 반복
        count = 0
        count1 = prices[i]
        print ("               첫번째 기준값 %d" %count1)
        for j in range (len(prices)): #j부터 배열 숫자까지 반복
            count2 = prices[j]
            print ("    비교값 %d" %count2)
            if j > i:
                if prices[i] <= prices[j]:
                    count += 1
                    print("Count")
                else:
                    count += 1
                    print("Count/Break")
                    break
        answer.append(count)

    print(answer)
    return answer

solution([1, 2, 3, 4, 5, 3, 4])