def solution(prices):
    length_prices = len(prices)
    answer = []
    count = []

    for i in range(length_prices):
        for j in range(length_prices):
            while count and prices[i] > prices[j]:
                top = count.pop()
                answer[top] = i - top
            count.append(i) 



        answer.append(count)
        
    print(answer)
    return answer

solution([1, 2, 3, 2, 3])