def solution(number, k):
    answer = []
    min_number = 9
    sorted_number = []
    number_sort = list(number)
    print(number_sort)
    
    for i in range(len(number)):
        sorted_number.append(number[i])
    sorted_number.sort()
    print(sorted_number)
    
    for i in range(k):
        for j in range(len(number)):
            if int(number[j]) <= int(min_number):
                min_number = number[j]
                print(min_number, "최소값")
                answer.append(sorted_number[-1])
                
                sorted_number.pop()
    print(number, sorted_number)
    print(answer)
    
    return answer

solution("1924", 2)