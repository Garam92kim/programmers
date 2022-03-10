def solution(answers):
    answer = []
    # 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo1_cnt = 0
    supo2_cnt = 0
    supo3_cnt = 0
    
    for i in range(len(answers)):
        if answers[i] == supo1[i%len(supo1)]:
            supo1_cnt += 1
        if answers[i] == supo2[i%len(supo2)]:
            supo2_cnt += 1
        if answers[i] == supo3[i%len(supo3)]:
            supo3_cnt += 1
            
    answer_temp = [supo1_cnt, supo2_cnt, supo3_cnt]

    # person = supo1에 해당, score = supo1_cnt에 해당 (index 개념이기 때문에)
    for person, score in enumerate(answer_temp): # 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
        if score == max(answer_temp):
            answer.append(person+1) # person (해당 점수에 해당하는 index +1)
    print(supo1_cnt, supo2_cnt, supo3_cnt)
    print(answer)
    return answer

solution([1,3,2,4,2]) # 정답이 순서대로 들은 배열