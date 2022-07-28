import tkinter as tk
import glob
import pandas as pd
from tkinter import filedialog as fd
import tkinter as tk

def ask_dir():
    root = tk.Tk()
    root.title('Open File Dialog')
    root.geometry('0x0')
    root.resizable(False, False)
    path = fd.askdirectory(title = 'Open an Excel file', initialdir = '/', mustexist = True)
    root.destroy()
    return path


def main():
    path = ask_dir()
    file_list = glob.glob(path + '/*.xlsx')
    excel_list = []
    for file in file_list:
        excel_list.append(pd.read_excel(file))
    # print(excel_list)
    excel_merged = pd.concat(excel_list, ignore_index = True)
    # print(excel_merged)
    file_name = input('Enter a filename (suggested name: Weekly_report): \n')
    excel_merged.to_excel(file_name, index = False)





    

