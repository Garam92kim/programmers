from openpyxl import Workbook

excel_path = "D:\Python\SideProject\AutomationForWCBS\Aging_result.xlsx" # Report 저장 경로

def Update_data(aging_start_time, aging_end_time, execution_time, execution_count):
    write_wb = Workbook()
    write_ws = write_wb.active
    write_ws.append(["Start Date", "End Date", "Execution Time", "Total execution"])
    write_ws.append([aging_start_time, aging_end_time, execution_time, execution_count])
    write_wb.save(excel_path)
    write_wb.close()