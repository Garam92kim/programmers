import heapq #제일 작은게 반환됨

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        scoville_min = heapq.heappop(scoville) # 제일 맵지 않은 음식
        if scoville_min < K: # 원하는 스코빌 지수보다 작을때 섞어줌
            scoville_min_2 = heapq.heappop(scoville)
            new = scoville_min + (scoville_min_2*2)
            print(scoville)
            heapq.heappush(scoville, new)
            print(new, scoville)
            answer += 1
            
        else:
            return answer
    
    return answer

solution([1, 2, 3, 9, 10, 12], 7)