import csv

class findtype:
    def __init__(self, attr=None):
        self.attr = attr
    
    def calc_result(self):
        if self.attr == 'Apple TV':
            return 1
        elif self.attr == '安裝數':
            return 2
        elif self.attr == 'YYYYMMDD (UTC)':
            return 3
        else:
            return 4

def getdata():

    result = []
    file = "D:\Intern\project\data_scraping\demo_files\onelink_demo.csv"
    with open(file, 'r', encoding ='utf-8') as playdata:
        data_frame = list(csv.reader(playdata))
        for row in data_frame:
            result.append(row)
    result = result[:10]
    # print(result)
    return result

def attr():
    id_list = getdata()
    stop = False
    for id in id_list:
        for list in id:
            if list.find('安裝數') != -1:
                result = findtype('安裝數')
                num = result.calc_result()
                stop = True
                break
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



            

