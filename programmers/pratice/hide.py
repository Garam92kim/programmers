def solution(clothes):
    hash_map_1 = []
    hash_map_2 = []
    dic_1 = {}
    dic_2 = {}
    count = 0
    
    # clother0,0 == clothse0,0 append
    # clothes1,0 == append

    for i in range(len(clothes)):
        if hash_map_1 not in clothes:
            hash_map_1.append(clothes[i][0])
        if hash_map_2 not in clothes:
            print(hash_map_2)
            hash_map_2.append(clothes[i][1])
        else:
            continue
    print("%d회차 hash_map1" %i, hash_map_1)
    print("%d회차 hash_map2" %i, hash_map_2)
    
    for ab in hash_map_1:
        if ab in dic_1:
            dic_1[ab] = dic_1[ab] + 1
    
    print(dic_1)
    
    for has2 in hash_map_2:
        for i in range(len(clothes)):
            if has2 in hash_map_2:
                hash_map_2.remove(hash_map_2[i])
            print("durldpdy!", hash_map_2)
    
    for hash1 in hash_map_1:
        for i in range(len(clothes)):
            if hash1 not in hash_map_2[i]:
                count += 1
                print(hash1, hash_map_2[i])
            else:
                count -= 1
    
    print(count)
    return count





solution ([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
