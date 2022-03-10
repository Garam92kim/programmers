def solution(numbers):
    print(numbers)
    numbers = list(map(str, numbers)) # numbers배열을 str으로 변환, 매핑, 배열로리턴
    print(numbers)
    # 문자열에 3을 곱하여 xxx 의 형태로 나오게 함
    # *** 문자열의 sorthing은 앞글자부터 순서대로 큰 것을 정렬해줌 !!!!!!!!!!
    # lamda 매개변수 : 표현식
    numbers.sort(key = lambda x: x*3, reverse=True)
    print(str(int(''.join(numbers))))
    # join : 배열을 특정 문자로 구분하여 문자열로 변환해주는 함수
    return str(int(''.join(numbers)))

solution([6, 10, 2])