from openpyxl import load_workbook
wb = load_workbook("sample_formula.xlsx",data_only=True) # 수식이 아닌 실제 데이터를 가져옴 data_only=True
ws = wb.active

# # 수식 그대로 가져옴
# for row in ws.values: # value를 바로 가져옴 (셀 정보가 아닌)
#     for cell in row:
#         print(cell)

# evaluate = 계산 되지 않는 상태의 데이터는 None 으로 나옴
# excel을 열었다가 닫을때 저장을 하고 닫으면 다시 None이 아닌 값이 출력됨 (작업 시 최종 산출물 기준으로 작업하는 것이)
for row in ws.values: # 수식에 값이 None으로 나옴 -> 데이터에 수식을 실제로 계산하지는 않음
    for cell in row:
        print(cell)
        