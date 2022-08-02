import appstore
import playstore
import onelink
import barcharts
import new_merge
from detect import attr
import tkinter as tk
from tkinter import filedialog as fd


def getfile():
    root = tk.Tk()
    root.title('Open File Dialog')
    root.geometry('0x0')
    root.resizable(False, False)
    file_path = fd.askopenfilename(title='Open a .csv file', initialdir= '/')
    root.destroy()
    return file_path


def entry2():
    decision = input('Auto mode (A) or Manual mode? (M)\n')
    decision = decision.upper()
    if decision == 'A' or decision == 'M':
        return decision
    else:
        print('Wrong input! (A) for auto mode, (M) for manual mode.')
        entry2()


def entry():
    key = input('Select an action: (1) appstore file (2) playstore file (3) onelink file (4) barchart generation (5) combine excel\n')
    return int(key)

def combine_file():
    try:
        new_merge.main()
        print('Excel files have successfully concatenated.')
        print('goodbye!')
    except:
        print('something went wrong try again later.')
    
    

def standard_operation(file, key):
    if key == 1:
        appstore.main(file)
    elif key == 2:
        playstore.main(file)
    elif key == 3:
        onelink.main(file)
    elif key == 4:
        try:
            barcharts.main(file)
        except:
            print('Invalid file! Please try again!')
    else:
        print('Error! Invalid input. Please enter a valid number.')
        main()


def query(key):
    query = input('do you want to process another file? Y/N\n')

    if query == 'Y' or query == 'y':
        main()
    elif key != 5:
        huh = input('would you like to combine excel files? Y/N\n')
        if huh == 'Y' or huh == 'y':
            combine_file()
        else:
            print('goodbye!')
            exit()
    else:
        print('goodbye!')
        exit()

def main():
    key = None
    decision = entry2()

    if decision == 'A':
        file = getfile()
        key = attr(file)
    elif decision == 'M':
        key = entry()
    
    if key == 5:
        combine_file()
        query(key)
    elif key != 5 and decision == 'M':
        file = getfile()
    

    standard_operation(file, key)
    query(key)






main()
