def solution(genres, plays):
    answer = []
    hash_map = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in hash_map:
            hash_map[genre]['plays'][i] = play
            hash_map[genre]['total_play'] += play
        else: # 각각 플레이수와 총 플레이수 확인을 위한 dic 추가
            hash_map[genre] = {'plays' : {i : play}, 'total_play' : play} 
            # 장르별 sorting 완료
        
    temp = sorted(hash_map.items(), key=lambda x : -x[1]['total_play']) # 1번의 dic중 total play를 가져옴
    # 각 곡별 sorting 완료
    print(hash_map.items())
    print("temp:", temp)
    
    for item in temp:
        target = item[1]['plays']
        item[1]['plays'] = sorted(target.items(), key=lambda x:(-x[1], x[0]))
     
    print(temp)                           

    temp = dict(temp)
    print(temp)
    
    for key in temp:
        try:
            answer += [temp[key]['plays'][0][0], temp[key]['plays'][1][0]]
        except:
            answer += [temp[key]['plays'][0][0]]

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])