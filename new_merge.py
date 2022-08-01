import openpyxl as opxl
import glob


path = "D:/Intern/project/data_scraping/Test_folder"

file_list = glob.glob(path + '/*.xlsx')

wb = opxl.workbook()

for file in file_list:
    wb_obj = opxl.load_workbook()
    s_obj = wb_obj.active
    for i in range(1, 9):
        for j in range(2):
            cell = s_obj.cell(row = i, column = j)




