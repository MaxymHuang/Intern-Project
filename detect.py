import csv

from numpy import true_divide


class findtype:
    def __init__(self, attr=None):
        self.attr = attr
    
    def calc_result(self):
        if self.attr == 'Apple TV':
            return 1
        elif self.attr == '安裝數' or self.attr == 'Install base':
            return 2
        elif self.attr == 'YYYYMMDD (UTC)':
            return 3
        else:
            return 4

def getdata(file):
    result = []
    if file.find('.xlsx') != -1:
        result.append('')
    else:
        with open(file, 'r', encoding ='utf-8') as playdata:
            data_frame = list(csv.reader(playdata))
            for row in data_frame:
                result.append(row)
        result = result[:10]
    return result

def attr(file):
    id_list = getdata(file)
    stop = False
    num = 4
    for id in id_list:
        for list in id:
            if list.find('安裝數') != -1:
                result = findtype('安裝數')
                num = result.calc_result()
                stop = True
                break
            elif list.find('Install base') != -1:
                result = findtype('Install base')
                num = result.calc_result()
                stop = True
            elif list.find('Apple TV') != -1:
                result = findtype('Apple TV')
                num = result.calc_result()
                stop = True
                break
            elif list.find('YYYYMMDD (UTC)') != -1:
                result = findtype('YYYYMMDD (UTC)')
                num = result.calc_result()
                stop = True
                break
        if stop:
            break
    

    return num



            

