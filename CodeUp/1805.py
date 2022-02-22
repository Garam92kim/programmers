from collections import deque

"""
입체기동장치 1~100 식별번호, 가스보유량10000을 같이관리
"""
kit_ea = int(input())
kit_num_gas = {}

for i in range(kit_ea):
    kit_number, gas = input().split()
    kit_number = int(kit_number)
    gas = int (gas)
    kit_num_gas.append(kit_number, gas)
    
for i in range(0, kit_ea-1):
    print(kit_ea, kit_num_gas[i][i])



