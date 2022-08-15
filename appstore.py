import csv
import xlsxwriter as xs

# getdata opens csv file from local directory and sorts data into a list

def getdata(filename):
    with open(filename, 'r', encoding='utf-8') as appdata:
        next(appdata)
        sorted_data = list(csv.reader(appdata))
        for x in range(0,4):
            sorted_data.pop(0)
            x = x
    return sorted_data

# countup adds up the download count

def countup(data):
    results = []
    temp = 0
    for i in range(1, len(data[0])):
        for j in range(len(data)):
            if data[j][i] == '-':
                data[j][i] = 0
            temp += float(data[j][i])
        results.append(temp)
        temp = 0
    return results

# getdates gets the time interval where the data is recorded

def getdates(data):
    dates = [data[0][0], data[-1][0]]
    print(dates)
    return dates

# excelwrite writes the resulting values into a excel file

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
    what = input('Is this CC or CV: ')
    what_type = 'AppStore ' + what
    stats = getdata(file)
    names = ['type', 'timespan', 'apple TV', 'Desktop', 'iPad', 'iPhone', 'iPod', 'Total']
    numbers = countup(stats)
    downloadsum = sum(numbers)
    numbers.append(downloadsum)
    datemepls = getdates(stats)
    dateme = str(datemepls[0]) + ' to ' +str(datemepls[1])
    numbers.insert(0, dateme)
    numbers.insert(0, what_type)
    finalvalues = {key:val for key, val in zip(names, numbers)}
    print('Your results are: ' +str(finalvalues))
    excelwrite(finalvalues, len(names))
