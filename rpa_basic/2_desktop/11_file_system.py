# 파일 기본
import os
# print(os.getcwd()) # current working directory
# os.chdir("rpa_basic") # rpa_basic으로 작업공간 이동
# print(os.getcwd()) # current working directory
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd()) # current working directory
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd()) # current working directory
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd()) # current working directory

# # 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# # 파일 경로에서 폴더 정보 가져오기
# dirname_path = os.path.dirname(r"D:\use_python\rpa_basic\my_file.txt") # r : 문자 그대로 인식함
# print(dirname_path)

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜
# c_time = os.path.getctime("add.png")
# print(c_time)
# print(datetime.datetime.fromtimestamp(c_time).strftime("%Y%m%d %H:%M:%S")) # 날짜 정보를 strftime을 통해 포맷 변경 가능

# # 파일의 수정 날짜
# m_time = os.path.getmtime("add.png")
# print(datetime.datetime.fromtimestamp(m_time).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# a_time = os.path.getmtime("add.png")
# print(datetime.datetime.fromtimestamp(a_time).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize("add.png") # byte 단위로 파일 크기 가져오기
# print(size)

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("rpa_basic")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기 (폴더 정보만 가져옴)

# 파일 목록 가져오기 (폴더 기준으로, 하위 폴더 모두 포함)
result = os.walk("rpa_basic") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기 (".") -> 현재 파일 기준으로 모두
# print(result)

# for root, dirs, files in result: # dirs 와 files 이 없다면 [] 으로 반환
#     print(root, dirs, files)

# # 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []

# for root, dirs, files in os.walk(os.getcwd()):
#     # [a.txt, b.txt ...]
#     if name in files:
#         result.append(os.path.join(root, name)) # . 기준으로
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# # *.xlsx, *.txt, 자동화*.png 패턴을 정해서 찾을수도 있음
# import fnmatch
# pattern = "*.py" # .py로 끝나는 모든 파일
# result = []
# for root, dirs, files in os.walk(os.getcwd()):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
#             result.append(os.path.join(root, name))
            
# print(result)

# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("rpa_basic")) # rpa_basic이 폴더인가? -> true
# print(os.path.isfile("rpa_basic")) # rpa_basic이 파일인가? -> false

# # print(os.path.isdir("add.png"))

# # 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면
# print(os.path.isfile("")) # False 반환

# 주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다")
# else:
#     print("존재하지 않습니다.")


# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt를 new_file_rename.txt로 이름 변경

# 파일 삭제
# os.remove("new_file_rename.txt")

# 폴더 생성
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
# os.mkdir("d:/") # 절대 경로 기준 폴더 생성

# os.mkdir("new_folders/a/b/c") # 하위 폴더를 가지는 폴더 생성 시도 (실패)
# os.makedirs("new_folders/a/b/c") # 성공

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
os.rmdir("new_folders") # 폴더가 비었을때만 지울수 있음