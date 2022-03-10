from itertools import permutations

# set 집합 = 중복되는것을 제거하고 하나만 사용하고 싶을때 사용 ex. 1이 세개일때 11 만들수 있는 경우의수를 제외하기 위함




# loop 활용 solution
# def solution(numbers):
#     prime_set = set() 
    
#     # 1. 모든 숫자 조합을 만듦
#     for i in range(len(numbers)):
#         # list로 호출하면 string 하나씩 호출하여 불러냄
# 개수를 원하기 때문에 i + 1 을 함 (한개로 만든 리스트, 두개로 만든 리스트...)
#         numbers_permutation = permutations(list(numbers), i + 1)
# map 을 사용해서 string 형태를 int 형태로 바꾸어 줌
#         numbers_per_list = list(map(int, map("".join, numbers_permutation))) # string 형태를 int로 map 하여 저장
#         prime_set |= set(numbers_per_list) # 집합으로 prime_set에 저장
        
#     # 2. 소수가 아닌 수를 제외한다. (에라~ 체)
#     prime_set -= set(range(0,2))
#     lim = int(max(prime_set) ** 0.5) + 1 # 두번째 인자를 사용하기 위함, 가장 큰 값에 루트를 씌움
#     for i in range(2, lim):
#         prime_set -= set(range(i*2, max(prime_set) + 1, i))
    
#     return len(prime_set)

# 재귀 활용 # top-down으로 계속 어떤 역할을 할지 생각하면서 작성하기
prime_set = set()
def isPrime(number):
    # 5. 0과 1을 제외한다.
    if number in (0,1):
        return False
    
    # 6. 에레토스테네스의 채
    lim = int(number ** 0.5 + 1)
    for i in range(2, lim):
        if number % i == 0:
            return False
    return True

def recursive(combination, others):
    # 4. 탈출 조건 / 비교 조건 잘 확인하기
    if combination != "":
        if isPrime(int(combination)):
            prime_set.add(int(combination))
    
    # 3. 현재까지 만들어진 숫자에, 남아있는 숫자중 하나를 더한다
    for i in range(len(others)):
        recursive(combination + others[i], others[:i] + others[i+1:])

def solution(numbers):
    
    # 1. 모든 조합을 만드는 recursive를 수행
    
    recursive("", numbers)
    
    # 2. prime_set의 length를 반환
    
    
    return len(prime_set)

solution("17")