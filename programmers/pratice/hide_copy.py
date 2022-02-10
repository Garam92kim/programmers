def solution(clothes):
    hash_map = {} #이름과 카테고리로 정리할 딕셔너리
    answer = 1
    
    for cloth in clothes: # clothes를 돌며 각 항목을 정리
        name = cloth[0]
        category = cloth[1]
        print("name", name)
        print("category", category)
        print("hash_map", hash_map)
        if category in hash_map: #카테고리가 있는경우 이름을 추가
            hash_map[category].append(name) # 이미 있으면 배열로 만듦
        else:
            hash_map[category] = [name] # 없으면 요소가 하나인 형태로
            
    for key in hash_map:
        answer *= (len(hash_map[key])+1)
    return answer-1

solution ([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
