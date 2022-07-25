import pandas as pd
import xlsxwriter as xs
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def excelwrite(dc, size):
    YN = input('Do you want to enter the data into an Excel Workbook? Y/N \n')
    if YN == 'Y' or YN == 'y':
        name = list(dc.keys())
        file = input('enter desired file name: ')
        if file.find('.xlsx') != True:
            file = file + '.xlsx'
        wb = xs.Workbook(file)
        ws = wb.add_worksheet('worksheet')
        df = []
        for i in range(size):
            df.append([name[i], dc[name[i]]])
        row = col = 0
        for name, data in (df):
            ws.write(row, col, name)
            ws.write(row, col + 1, data)
            row += 1
        wb.close()
        print('Your results have been entered into an excel workbook')
    return None

def getfile():
    root = tk.Tk()
    root.title('Open File Dialog')
    root.geometry('0x0')
    root.resizable(False, False)
    file_path = fd.askopenfilename(title='open a csv file', initialdir= '/')
    showinfo(title='Selected file', message=file_path)
    root.destroy()
    return file_path

def main():
    num = input('how many days do you want? \n')
    what = input('Is this CC or CV? ')
    what_type = 'OneLink ' + what
    file = getfile()
    df = pd.read_csv(file)
    if int(num) > len(df):
        print('error! input size too large')
    else:
        num = -abs(int(num))
        df = df[num:]
        dateme = df['YYYYMMDD (UTC)']
        datemepls = str(dateme.iloc[0]) + ' to ' +str(dateme.iloc[-1])
        total = df['Total'].sum()
        iPhone = df['iPhone'].sum()
        iPad = df['iPad'].sum()
        Android = df['Android'].sum()
        Huawei = df['Huawei'].sum()
        other = df['Other'].sum()
        names = ['type', 'timespan', 'iPhone', 'iPad', 'Android', 'Huawei', 'Other', 'Total']
        values = [what_type, datemepls, iPhone, iPad, Android, Huawei, other, total]
        dc = {key:val for key, val in zip(names,values)}
        print('Your results are: ' +str(dc))
        excelwrite(dc, len(names))



