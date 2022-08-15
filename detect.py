import csv

# This script is a fundamental to automation that affects the whole process

# Class 'findtype' essentially determines which platform does the input file come from
# by using each file formatting differences and their characteristics


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
            return print("invalid file please try again")

# getdata in this script uses the same getdata UDF in other file like appstore.py
# the only difference is that it only reads very few values since its purpose is 
# to determine the type of the file

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

# attr takes in 'file' as an input and processes which type the 'file'
# correspondes to and returns a number that represents the type of file.

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



            

