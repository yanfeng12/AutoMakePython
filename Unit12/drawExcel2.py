from openpyxl import Workbook


wb = Workbook()
sheet = wb.active
for i in range(1, 10):
    sheet["A" + str(i)] = i


from openpyxl.chart import BarChart, Reference, Series
refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)


seriesObj = Series(refObj, title='First series')
chartObj = BarChart()
chartObj.append(seriesObj)


sheet.add_chart(chartObj)
wb.save("SampleChart2.xlsx")
