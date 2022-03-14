def solution(n, lost, reserve):
    answer = 0
    # reserve 에서 pop 하면 될듯?
    suit_student = n - len(lost)
    print(suit_student)
    
    while True:
        if lost and reserve:
            suit_student += 1
            reserve.pop()
            lost.pop()
            if len(lost) == len(reserve):
                suit_student -= 1
        else:
            break
        
     
    print(lost, reserve, suit_student)   
    
    return suit_student

solution(3, [1], [])