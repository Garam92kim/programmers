def solution(genres, plays):
    answer = []
    hash_map = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in hash_map:
            hash_map[genre]['plays'][i] = play
            hash_map[genre]['total_play'] += play            
        else:
            hash_map[genre] = {'plays' : {i : play}, 'total_play' : play}
        
    temp = sorted(hash_map.items(), key = lambda x : -x[1]['total_play'])
    
    for item in temp:
        target = item[1]['plays']
        item[1]['plays'] = sorted(target.items(), key = lambda x : (-x[1], x[0]))
        
    temp = dict(temp)
    for key in temp:
        try:
            answer += [temp[key]['plays'][0][0], temp[key]['plays'][1][0]]
        except:
            answer += [temp[key]['plays'][0][0]]
            
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])