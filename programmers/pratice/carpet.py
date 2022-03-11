def solution(brown, yellow):
    answer = []
    hap = brown + yellow
    
    for i in range(hap):
        for j in range(hap):
            if i * j == hap and i >= j:
                answer.append([i, j])
    
    print(answer)
    return answer # 가로, 세로

solution(8, 1)