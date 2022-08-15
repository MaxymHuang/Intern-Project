import appstore
import playstore
import onelink
import barcharts
import new_merge
from detect import attr
import tkinter as tk
from tkinter import filedialog as fd

# getfile() handles any user file input dialog

def getfile():
    root = tk.Tk()
    root.title('Open File Dialog')
    root.geometry('0x0')
    root.resizable(False, False)
    file_path = fd.askopenfilename(title='Open a file', initialdir= '/')
    root.destroy()
    return file_path

# entry() and entry2() handles user decision which dictates how the program works entirely

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

# combine_file calls new_merge.py script that essentially combines all the output excel files

def combine_file():
    try:
        new_merge.main()
        print('Excel files have successfully concatenated.')
        print('goodbye!')
    except:
        print('something went wrong try again later.')

# standard operation takes in 2 values file and key. File is where the specified file is 

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

# query askes user if the user wants to process another file or end the program

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

# main function calls and execute most of the requests

def main():
    key = None
    decision = entry2()

    if decision == 'A':
        file = getfile()
        key = attr(file)
        standard_operation(file, key)
    elif decision == 'M':
        key = entry()
    
    if key == 5:
        combine_file()
        query(key)
    elif key == 4:
        ask = entry2()
        if ask == 'M':
            file = getfile()
            barcharts.main('M', file)
        else:
            keyfile_path = getfile()
            barcharts.main('A', keyfile=keyfile_path)
    elif key != 5 and decision == 'M':
        file = getfile('A')
        standard_operation(file, key)
    
    query(key)

main()