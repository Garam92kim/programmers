from openpyxl.chart import BarChart, LineChart, Reference # bar chart 사용을 위함
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 제목 포함하여 b1:c11 까지 데이터
line_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3)
line_chart = LineChart()
line_chart.add_data(line_value, titles_from_data = True)
line_chart.title = "성적표" # 제목
line_chart.style = 20 # 미리 적용된 style 사용
line_chart.y_axis.title = "점수" # y축 제목
line_chart.x_axis.title = "번호" # x축 제목
ws.add_chart(line_chart, "E1")


# bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3) # b2:c11 까지 데이터를 차트로 생성
# bar_chart = BarChart() # 차트 종류 설정
# bar_chart.add_data(bar_value)
# ws.add_chart(bar_chart, "E1") # 원하는 차트와 넣을 위치 작성
wb.save("sample_chart.xlsx")

# openpyxl 사이트에서 chart 부분 보면 사용할 수 있는 차트 정리되어 있음