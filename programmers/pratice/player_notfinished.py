def solution(participant, completion):
    answer = ''
    dic = {} #hash 형태로 저장
    
    for person in completion: # 완주한 사람 dic에 저장, 동명이인은 +1 함
        if person in dic: # 같은 사람이 이미 있으면 동명이인
            dic[person] = dic[person] + 1 # hash + 1
            print(person)
        else:
            dic[person] = 1  # 아니면 1로 설정
            print(person)
    print("dic :", dic, "person :", person)
    
    for person in participant: #참가자 확인
        if person not in dic:   # 참가자 중 dic (완주한 사람 Hash 모음)에 없으면
            return person   # 해당 사람이 완주 못함
        if dic[person] == 0: # 동명잉인의 경우 값이 결국 0이 될수있음
            return person
        dic[person] = dic[person] - 1 # hash에서 +1 된 동명이인의 경우
        
        print(person, dic)
    print(answer)



    
    







    return answer

solution(["leo", "koko", "eden", "koko"], ["leo", "koko", "koko"])