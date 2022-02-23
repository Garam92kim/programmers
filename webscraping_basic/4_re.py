import re

p = re.compile("ca.e") # 원하는 정규식 (형태)
# . : 하나의 문자를 의미 ca.e -> cave, case, cafe
# ^ : 문자열 시작 부분 (^de) desk, destination  
# $ : 이 문자로 끝나는것 (se$) case, base


def print_match(m):
    if m:
        print("m.group() :", m.group()) # 일치하는 문자열 반환
        print("m.string :", m.string) # 입력받은 문자열 그대로 출력
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 index (-1 까지)
        print("m.spam() :", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭 x")

# m = p.match("cafeless") # 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# list = p.findall("good care cafe") # 일치하는 모든 것을 리스트 형태로 반환
# print(list)

# w3school 사이트 learn python 에서 regular expension 에서 더 공부 가능
# python re 검색 docs에서 공부 가능 (python 공식 문서)