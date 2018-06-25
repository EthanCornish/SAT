
def Help():
    help1 = 'Help 1: Using the main menu'
    help2 = 'Help 2: Creating Sets'
    help3 = 'Help 3: Editing Sets'
    help4 = 'Help 4: Selecting Different Sets'
    help5 = 'Help 5: Viewing an Overview of Sets'
    help6 = 'Help 6: Viewing Sets'
    help7 = 'Help 7: Deleting Sets'
    help8 = 'Help 8: Importing and Exporting Sets'

    MenuActive = True
    while MenuActive:
        print('\n\nSelect the following option to chose which are you need help using.')
        print('1: Using the main menu and exiting the program.')
        print('2: Creating Sets')
        print('3: Editing Sets')
        print('4: Selecting a Different Set and how to know your currently selected set.')
        print('5: Viewing an Overview of Sets.')
        print('6: Viewing Sets')
        print('7: Deleting Sets')
        print('8: Importing and Exporting Sets')
        print('9: Exit Help')
        menuOption = input('Option:')

        if menuOption == '1':
            print(help1)
        elif menuOption == '2':
            print(help2)
        elif menuOption == '3':
            print(help3)
        elif menuOption == '4':
            print(help4)
        elif menuOption == '5':
            print(help5)
        elif menuOption == '6':
            print(help6)
        elif menuOption == '7':
            print(help7)
        elif menuOption == '8':
            print(help8)
        elif menuOption == '9':
            print('Exiting Help\n')
            menuActive = False
            break
        else:
            print('The option you have selected is invalid\nTry Again\n')
    return