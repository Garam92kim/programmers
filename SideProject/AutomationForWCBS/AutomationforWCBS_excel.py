from asyncore import write
from openpyxl import Workbook

excel_path = "D:\Python\SideProject\AutomationForWCBS\Aging_result.xlsx"
excel_sheet_name = "Aging"


write_wb = Workbook()
write_ws = write_wb.create_sheet(excel_sheet_name)
write_ws = write_wb.active
write_ws.append(["Start date", "End Date", "Total excution"])
write_ws.append([1, 2, 3])
write_wb.save(excel_path)
write_wb.close()