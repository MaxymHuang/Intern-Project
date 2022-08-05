import csv
import xlsxwriter as xs

def getdata(file):
    try:
        result = []
        with open(file, 'r', encoding ='utf-8') as playdata:
            data_frame = list(csv.reader(playdata))
            for row in data_frame:
                result.append(row)
    except:
        print('Invalid file! Please try again.')
        return None
    # print(result)
    return result

def findtail(data, col):
    for items in reversed(data):
        if items[col] == '-' or items[col] == '':
            pass
        else:
            tail = items[col]
            break
    if col != 0:
        tail = int(tail)
    return tail

def countrylist(data):
    initial = data[0]
    # print(initial)
    clist = []
    lang = data[:5]
    option = False
    for p in lang:
        for s in p:
            if s.find('安裝數') != -1:
                option = True
                break
    if option:
        for i in initial:
            if i == initial[0] or i == initial[-1] or i == initial[1]:
                continue
            else:
                index = i.find('：')
                # print(index)
                clist.append(i[index+1:])
    else:
        for j in initial:
            if j == initial[0] or j == initial[-1] or j == initial[1]:
                continue
            else:
                index = j.find(':')
                clist.append(j[index+2:])
    return clist


def findhead(data, col):
    for items in data:
        if items[col] == '-' or items[col] == '' or items[col] == '日期' or items[col] == 'Date':
            pass
        else:
            head = items[col]
            break
    return head

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
    what_type = 'PlayStore ' + what
    data_frame = getdata(file)
    countries = countrylist(data_frame)
    values = []
    names = ['type', 'timespan', 'Total']
    for i in countries:
        names.append(i)
    for i in range(len(names) - 1):
        if i == 0:    
            index = findhead(data_frame, i) + ' to ' + findtail(data_frame, i)
            values.append(index)
        else:
            values.append(findtail(data_frame, i))
    values.insert(0, what_type)
    disp = {key:val for key, val in zip(names, values)}
    print("Your results are: " +str(disp))
    excelwrite(disp, len(names))
    

