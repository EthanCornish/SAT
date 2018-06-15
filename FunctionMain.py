# Importing the 'CreateSet' Function
from FunctionCreateSet import CreateSet
from FunctionSelectSet import SelectSet
from FunctionViewOverview import ViewOverview
from FunctionViewSet import ViewSet
from FunctionHelp import Help
from FunctionDeleteSet import DeleteSet


#listSetName = []
#global listSetName

# Main Function for CLI
def MainCLI():
    # Define listSetName list as empty before reading from file
    listSetName = []
    # Reading listSetName file to the list.
    # Each line in the file is a set
    # The first value is the setName, the second is the fileName
    # The try, except block prevents an error if it is the first time running the program and therefor there is no file
    try:
        fileListSetName = open('fileListSetName.txt', 'r')
        for line in fileListSetName:
            line = line.strip('\n')
            line = line.split(',')
            listSetName.append(line)
        fileListSetName.close()
    except FileNotFoundError:
        print('FileNotFound (fileListSetName.txt)')
        listSetName = []


    # menu while loop that calls each a function for each action
    menuActive = True
    while menuActive:
        print('\nSelect an Option by entering the corresponding number.')
        print('1:  Create')
        print('2:  Select a Different Set')
        print('3:  View Overview of Set')
        print('4:  View Set')
        print('5:  Help')
        print('6:  Delete Set')
        print('7:  Exit')
        menuInput = input(': ')

        if menuInput == '1':
            print('Create Set Option Chosen')
            CreateSet(listSetName)
        elif menuInput == '2':
            print('Select a Different Set Option Chosen')
            SelectSet(listSetName)
        elif menuInput == '3':
            print('View Overview Option Chosen')
            ViewOverview(listSetName)
        elif menuInput == '4':
            print('View Set Option Chosen')
            ViewSet(listSetName)
        elif menuInput == '5':
            print('Help Option Chosen')
            Help()
        elif menuInput == '6':
            print('Delete Set Option Chosen')
            DeleteSet(listSetName)
        elif menuInput == '7':
            print('Exit Option Chosen')
            menuActive = False
            break
        else:
            'The option you have chosen is invalid.\nTry Again\n\n'


    # Saving listSetName to the file to save it for the next execution
    fileListSetName = open('fileListSetName.txt', 'w')
    for set in listSetName:
        fileListSetName.write(set[0])
        fileListSetName.write(',')
        fileListSetName.write(set[1])
        fileListSetName.write('\n')

    return

MainCLI()