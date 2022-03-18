def solution(N, number):
    answer = -1
    
    if number == N:
        return 1 # N을 한번만 사용해도 구할 수 있는 최솟값이기 때문에 1 반환
    
    # 큰 문제를 여러개의 작은 문제들로 쪼개어 접근하는 방식
    _li = [set() for i in range(8)] # set 자료구조를 8개 초기화
    # _li = [set()]*8 -> 8개의 set 모두 같은 메모리를 가르키므로 사용하면 안됨
    
    # _li
    # set() set() set() ... set() 8개
    # 5를 한번 썻을때 발생할 수 있는걸 첫번째 set에, 5를 두번 썻을때 발생할 우 있는걸 두번째 set에
    for i in range(len(_li)):
        _li[i].add(int(str(N)*(i+1))) # set() 하나를 의미하고 N(5) 을 0,1,2,3, ..8 까지 넣어줌
    
    # 동일한 연산을 하지 않기 때문에 동적계획법임
    for i in range(1, 8): # 0번째 index는 무시 -> 5하나만 사용하는곳은 연산이 못들어감 ??
        for j in range(i):
            for op1 in _li[j]:
                for op2 in _li[i-j-1]:
                    _li[i].add(op1+op2)
                    _li[i].add(op1-op2)
                    _li[i].add(op1*op2)
                    if op2 != 0:
                        _li[i].add(op1//op2) # 나머지는 무시하기 때문에 몫만 사용
        if number in _li[i]:
            answer = i+1
            break # 최솟값만 필요하기 때문에
          
    
    
    # 5를 1번 2번 3번 ... 8번 사용할때
    # 5, 55, 555, 5555...., 55555555
    
    
    return answer

solution(5, 12)