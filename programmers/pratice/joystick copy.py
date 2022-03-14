def solution(name):
    answerArr = [0] * len(name)
    for i in range(len(name)):
        if name[i] != "A":
            if ord(name[i]) <= ord("M"): 
                answerArr[i] += ord(name[i]) - ord("A")
            else:
                answerArr[i] += ord("Z") - ord(name[i]) + 1
        else:
            answerArr[i] = 0

    currentIndex = 0
    rightMoveIndex = 0
    leftMoveIndex = 0
    answer = 0

    while True:
        rightCnt = 0
        leftCnt = 0

        if answerArr[currentIndex] != 0:
            answer += answerArr[currentIndex] # 위 아래 조작 횟수
            answerArr[currentIndex] = 0

        if sum(answerArr) == 0:
            break

        while True:
            rightMoveIndex += 1
            rightCnt += 1
            if answerArr[rightMoveIndex] != 0:
                break
       
        while True:
            leftMoveIndex -= 1
            leftCnt += 1
            if answerArr[leftMoveIndex] != 0:
                break

        if rightCnt < leftCnt or rightCnt == leftCnt:
            currentIndex = rightMoveIndex
            answer += rightCnt # 좌 우 이동 횟수
        else:
            currentIndex = leftMoveIndex
            answer += leftCnt # 좌 우 이동 횟수

        rightMoveIndex = currentIndex
        leftMoveIndex = currentIndex
    
    return answer