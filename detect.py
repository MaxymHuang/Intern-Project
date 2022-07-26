import csv
import pandas as pd

class findtype:
    def __init__(self, attr=None):
        self.attr = attr
    
    def calc_result(self):
        if self.attr == 'Apple TV':
            return '1'
        elif self.attr == '日期':
            return '2'
        elif self.attr == 'YYYY':
            return '3'
        else:
            return '4'



def getdata():
    try:
        result = []
        file = "D:\Intern\project\data_scraping\demo_files\playstore_demo.csv"
        with open(file, 'r', encoding ='utf-8') as playdata:
            data_frame = list(csv.reader(playdata))
            for row in data_frame:
                result.append(row)
        result = result[:4]
    except:
        print('Invalid file! Please try again.')
        return None
    # print(result)
    return result

def attr():
    id_list = getdata()
    # print(id_list)
    
    for id in id_list:
        for list in id:
            if list.find('日期') != -1:
                result = findtype('日期')
                num = result.calc_result()
                break
            elif list.find('Apple TV') != -1:
                result = findtype('Apple TV')
                num = result.calc_result()
                break
            elif list.find('YYYYMMDD (UTC)'):
                result = findtype('YYYYMMDD (UTC)')
                num = result.calc_result()
            else:
                num = '4'
    return num



print(attr())


            

