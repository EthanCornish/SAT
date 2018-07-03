# Note there is no information available for help as it requires the GUI to be completed first.

def Help():
    # Setting the variables that will contain the text on how to use different parts of the program
    help1 = 'Help 1: Using the main menu'
    help2 = 'Help 2: Creating Sets'
    help3 = 'Help 3: Editing Sets'
    help4 = 'Help 4: Selecting Different Sets'
    help5 = 'Help 5: Viewing an Overview of Sets'
    help6 = 'Help 6: Viewing Sets'
    help7 = 'Help 7: Deleting Sets'
    help8 = 'Help 8: Importing and Exporting Sets'

    # Menu for help in different areas of the program
    MenuActive = True
    while MenuActive:
        # Menu Options for the user
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

        # If statement to call a variable depending which option the user entered.
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
            # Lets the user re enter input
            print('The option you have selected is invalid\nTry Again\n')
    return
