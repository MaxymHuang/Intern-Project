import pandas as pd
import xlsxwriter as xs

def excelwrite(dc, size):
    YN = input('Do you want to enter the data into an Excel Workbook? Y/N \n')
    if YN == 'Y' or YN == 'y':
        name = list(dc.keys())
        file = input('enter desired file name: ')
        if file.find('.xlsx') == -1:
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

def main(file):
    num = input('how many days do you want? \n')
    what = input('Is this CC or CV? ')
    winnie_the_pooh = input('Is this China (CN) or WorldWide (WW)? ')
    what_type = 'OneLink ' + what + winnie_the_pooh
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



