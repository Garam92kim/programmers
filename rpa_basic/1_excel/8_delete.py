from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active


# ws.delete_rows(8, 3) # 8 번째 줄부터 3줄 삭제

# ws.delete_cols(2) # 2번째 열 (b) 삭제
ws.delete_cols(2, 2) # 2번째 열부터 2개 열 삭제

# ws.delete_rows(8) # 8번째 줄에 있는 7번학생 데이터 삭제
wb.save("sample_delete_col.xlsx")
