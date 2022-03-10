def solution(citations):
    answer = 0
    citations.sort()
    # 3번 이상 인용된게 3개 이상 -> 끝에서 3번째 같이 3보다 크면 됨
    # 길이, 개수, 횟수 index의 최소값이 마지막값보다 
    
    for i in range(1, len(citations)+1): # index로 처리하기 위해 1부터 시작
        min_num = citations[-i] # 끝에서부터 
        if min_num >= i:
            answer = i # i가 index라고 생각하면 됨
    
solution([1, 2, 3, 10, 0, 3, 12])