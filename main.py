import appstore
import playstore
import onelink
import barcharts
import merge
def entry():
    key = input('Select an action: (1) appstore file (2) playstore file (3) onelink file (4) barchart generation (5) combine excel\n')
    return key

def combine_file():
    try:
        merge.main()
        print('Excel files have successfully concatenated.')
        print('goodbye!')
    except:
        print('something went wrong try again later.')
    

def main():
    key = entry()
    key = int(key)
    if key == 1:
        appstore.main()
    elif key == 2:
        playstore.main()
    elif key == 3:
        onelink.main()
    elif key == 4:
        barcharts.main()
    elif key == 5:
        combine_file()
    else:
        print('Error! Invalid input. Please enter a valid number.')
        main()

    query = input('do you want to process another file? Y/N\n')
    if query == 'Y' or query == 'y':
        main()
    else:
        huh = input('would you like to combine excel files? Y/N\n')
        if huh == 'Y' or huh == 'y':
            combine_file()
        else:
            print('goodbye!')


main()
