import math
 
def solution(n, costs): # costs : 간선 집합
    result = 0
    
    # 그리디 알고리즘
    # 크루스칼 알고리즘 : 최소비용으로 모든 노드를 연결하기 위함 (최소비용 신장트리)
    # 간선 숫자 = 노드숫자 - 1
    # cycle이 형성되면 안됨
    # 모든 간선을 거리 기준으로 오름차순 정렬 후 적은 비용을 기준으로 노드를 연결
    
    # 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
    # 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    # 2.1. 사이클이 발생하지 않는 경우에만 신장트리에 포함 (아니면 무시)
    # 3. 모든 간선에 대해 2번의 과정을 반복
    
    
    # 정렬했을 때 weight 가중치 작을수록 리스트 전면에 오도록 costs를 변경
    costs = [(cost, node1, node2) for node1, node2, cost in costs] # 기존 코스트 list를 (노드, 노드, 비용) 비용이 제일 앞에 오도록 바꿈
    costs.sort()
    
    # 이미 방문한 노드는 저장
    visited = set()
    
    # 가장 가중치 작은 것부터 연결
    cost, node1, node2 = costs[0]
    
    # 자기 자신을 연결하는 게 아니면, 첫 번째 노드 weight를 result에 저장
    if node1 != node2:
        result += cost
        
    # 두 노드가 연결되었으므로 두 노드를 visited에 저장 (노드 값 저장)
    visited.update([node1, node2])
    # -- 여기까지가 첫번째 가장 적은 cost의 노드를 이용하여 visited에 노드1과 노드2를 연결한 결과를 저장함
    
    # 모든 노드가 연결될 때까지 반복, n 이 노드의 개수
    while len(visited) != n:
        print(len(visited), n)
        # 연결할 수 있는 노드 weight의 최솟값을 찾기 ??
        _min = math.inf # 양의 무한대...?
        
        for cost, node1, node2 in costs:
            # from과 to 두 개의 노드 중 하나는 visited에 있어야 한다
            # -> 이미 연결된 노드들 중 하나여야 한다
            
            if node2 in visited or node1 in visited:
                
                # 이미 둘 다 visited에 있으면, 새로 들어온 weight는 기존에 연결된 두 노드의 weight보다 작을 수 없다
                # from과 to 가 같은 노드면 저장할 이유가 없음
                if (node1 in visited and node2 in visited) or node1 == node2:
                    continue
                
                # weight가 가장 작은 노드로 _min값을 업데이트
                if _min > cost:
                    _min = cost
                    frm, to = node1, node2
                    print("현재 최소 cost", _min)
                    
        # 최소 weight를 result 값에 더함
        result += _min
        # 새로 연결한 두 개의 노드를 visited에 업데이트
        visited.add(frm)
        visited.add(to)
        print(visited)
        
        # while문 빠져나오면 모든 노드는 연결된 상태, 각 노드를 연결하는 weight는 작은 순서대로 전부 찾은 상태
        
    
    print(result)
    return result

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])