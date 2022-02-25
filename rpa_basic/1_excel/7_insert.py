from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 row에 삽입 (8번째 줄이 비어짐)

ws.insert_rows(8, 5) # 8번째 row에 5줄 삽입


wb.save("sample_insert_rows.xlsx")