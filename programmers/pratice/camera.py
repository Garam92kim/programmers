def solution(routes):
    answer = 1
    
    routes = [(i, j) for i, j in routes]
    routes.sort()
    
    start, end = routes[0][0], routes[0][1]
    print(routes)
    
    for rs, re in routes[1:]:
        if rs <= end: # 시작 지점이 끝나는 지점보다작으면 구간이 겹침
            print(rs, start, re, end)
            start = max(rs, start)
            end = min(re, end)
        else: # 겹치는 구간이 없으므로 카메라 한 대 설치 필요
            start, end = rs, re
            answer += 1
            
    
    print(answer)
    
    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])