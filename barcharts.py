import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd


# def getfile():
#     root = tk.Tk()
#     root.title('Open File Dialog')
#     root.geometry('0x0')
#     root.resizable(False, False)
#     file_path = fd.askopenfilename(title='open a csv file', initialdir= '/')
#     showinfo(title='Selected file', message=file_path)
#     root.destroy()
#     return file_path

def findavg(df, days=30):
    new_user = df['New users']
    users = df['Users']
    dates = df['month']
    size = len(users)
    avg_user = []
    avg_new = []
    new_sum = 0
    user_sum = 0
    for i in range(1, size, days):
        if (size - i) < 29 and dates[i] != 2:
            days = size - (i + 1)
            # print('yes yes yes')
        elif dates[i] == 4 or dates[i] == 6 or dates[i] == 9 or dates[i] == 11:
            days = 30
            # print('nononono')
        elif dates[i] == 2:
            days = 28
        else:
            days = 31
        new_sum = sum(new_user[i:(i + days)])
        user_sum = sum(users[i:(i + days)])
        avg_new.append(round(new_sum / days))
        avg_user.append(round(user_sum / days))
    return avg_new, avg_user

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


def main(file):
    df = pd.read_excel(file)
    avg = findavg(df)
    avg_new = avg[0]
    avg_user = avg[1] 
    months = findmonthlist(df)
    if len(months) > 12:
        avg_new = avg_new[-12:]
        avg_user = avg_user[-12:]
        months = months[-12:]
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
    plt.show()
    


