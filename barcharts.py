import matplotlib.pyplot as plt
import pandas as pd
import googleapi

# Class 'Month' calculates how many days are there to the corresponding month value
# as well as checking if the data is ending.

# Note that Leap year scenario is not considered. Must be updated by 2024.

class Month:
    def __init__(self, month_list):
        self.month_list = month_list
        self.size = len(month_list)
    
    def find_days(self, day):
        if self.size <= 31:
            return self.size
        
        month = self.month_list[day]

        if (month % 2 == 0 and month < 7 and month != 2) or (month % 2 == 1 and month >= 8):
            days = 30
            return days
        elif month == 2:
            days = 28
            return days
        else:
            days = 31
            return days
    
    def check_ending(self, index):
        remaining_days = self.size - index

        if remaining_days < 30 and self.month_list[index] != 2:
            return True
        else:
            return False

# The way barplot represents the data sets is by calculating the average user count of each months
# and present it by using stacked barplot of each months of active users and new users

def findavg(df):
    new_user = df['New users']
    users = df['Users']
    dates = df['month']
    size = len(users)
    users_sum = 0
    new_user_sum = 0
    users_avg = []
    new_user_avg = []
    months = Month(dates)
    step = months.find_days(0)
    index = 0

    while index <= size:
        day = months.find_days(index)

        if months.check_ending(index):
            day = size - index

        users_sum = sum(users[index:index + day])
        new_user_sum = sum(new_user[index:index + day])
        users_avg.append(round(users_sum / day))
        new_user_avg.append(round(new_user_sum / day))
        
        step = months.find_days(index + 1)
        
        index += step

    return users_avg, new_user_avg


    
# findmonthlist() determines which months are included from the inputs

def findmonthlist(df):
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthlist = df['month']
    temp = monthlist[0]
    sortedlist = []
    sortedlist.append(month_name[temp - 1])

    for month in monthlist:

        if month == temp:
            continue

        elif month != temp:
            temp = month
            sortedlist.append(month_name[temp - 1])

    return sortedlist

# main function takes in 3 inputs, 'decide' decides whether the user wants to use API or not
# 'keyfile' indicates the location of the API key, 'file' indicates the location of the data sets (not required for API option)

def main(decide = 'M', keyfile ='client_key.json', file = None):

    if decide == 'A':
        type = input('Which source does the barplot correspond to? CC firebase (A) CV firebase (B)? ')
        type = type.upper()

        # start_date has to be input in exact YYYY-MM-DD format for API to work

        start_date = input('Please enter start date (YYYY-MM-DD): ')
        while start_date.find('-') != 4:
            start_date = input('Please enter start date (YYYY-MM-DD): ')
        
        df = googleapi.get_report(type, start_date, keyfile)

    else:
        df = pd.read_excel(file)

    avg = findavg(df)
    avg_new = avg[1]
    avg_user = avg[0] 
    months = findmonthlist(df)
    
    if len(months) > 12:
        avg_new = avg_new[-12:]
        avg_user = avg_user[-12:]
        months = months[-12:]
    
    # Formats the barplot

    plt.rcParams["figure.figsize"] = (22, 14)
    plt.rcParams.update({'font.size': 22})
    p1 = plt.bar(months, avg_new, color = '#A4AEC9')
    p2 = plt.bar(months, avg_user, bottom=avg_new, color='#D3D8E5')
    plt.title('Active User Count by Month', )
    plt.xlabel('Month')
    plt.ylabel('User Count')
    plt.legend((p1[0], p2[0]), ('New User', 'Active User'))
    plt.rcParams.update({'font.size': 15})

    for i in range(len(months)):
        plt.text(i, avg_user[i]+4, avg_user[i], ha = 'center')
        plt.text(i, avg_new[i]/2.5, avg_new[i], ha = 'center')

    # Presents the output to user

    plt.show()
    

# main('A')
# main('M', "D:\Download\data\CC.xlsx")