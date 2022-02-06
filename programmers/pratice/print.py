from collections import deque

def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    answer = 0
    maximum = max(priorities)
    print("max는 %d" %maximum)

    while True:
        index = index_list.popleft() #왼쪽 끝 index 값 삭제, 그 값 index에 저장
        if priorities[index] < maximum: #priorities의 max값 대비 작으면 실행
            index_list.append(index) #index값 마지막으로 미룸
            print(index)
        else: # 우선순위가 높을 시 실행
            answer += 1 # 몇번째 로 출력하는지 카운트 하는 용도
            priorities[index] = 0 #maximum값 0으로 치환
            maximum = max(priorities) #새로운 maximum값 대입
            print("max는 %d" %maximum)
            if index == location: # 선택한 위치가 가장 높은 값이면 바로 answer 출력
                print(answer)
                return answer


solution([10, 11, 12, 1, 2], 4)