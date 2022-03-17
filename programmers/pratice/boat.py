def solution(people, limit):
    answer = 0
    people.sort()
    
    # people 리스트를 사용하기 위한 변수
    i = 0 
    j = len(people)-1 # people list에 남아 있는 사람의 수
    
    # people이 0이 될때까지 반복
    while i <= j:
        print(i, j, answer)
        print(people[i], people[j])
        answer += 1 # 구명 보트 수 + 1
        # 가장 무거운사람과 가벼운 사람의 무게가 limit을 초과 하지 않는다면 가벼운사람과 무거운 사람 모두 list에서 빠져야함
        if people[j] + people[i] <= limit: # people[j] = 가장 무거운 사람 people[i] = 가장 가벼운 사람
            i += 1
            print("여기 어떻게 돌지?", i)
        # 아니라면 무거운 사람만 보트에 탐
        j -= 1
    print(answer)
    return answer

solution([70, 50, 80, 50], 500)

# POP, REMOVE 등 리스트 관련 함수 사용 시 효율성 떨어짐