import itertools

# 소수를 구하기 위한 에라토스테네스의 체
# def prime_list(n):
#     num = set(range(2, n+1))
    
#     for i in range(2, n+1):
#         if i in num:
#             num -= set(range(2*i, n+1, i))
    
#     return len(num)

# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우 
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]
    

def solution(numbers):
    answer = 0
    temp_number_array = []
    temp_number_combi = []
    # 문자열 분리
    for i in range(len(numbers)):
        temp_number_array.append(numbers[i])
    # 소수 : 자기 자신과 1로만 나누어 지는 수 -> 어떻게 찾지? 나머지가 1이 아니면 소수였나
    # 우선 문자열 합쳐서 나오는 숫자의 경우의 수를 만들어야 함
    temp_number_combi = list(map(''.join, itertools.permutations(temp_number_array))) # permutations 을 이용한 순열조합 만들기
    print(temp_number_combi)
    prime_list(temp_number_combi)
    
    return answer

solution("17") # 각 문자를 분리해서 값 비교 해야 할듯, string 형태니까 자릿수로 출력 가능