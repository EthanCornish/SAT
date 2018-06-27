# Importing the 'CreateSet' Function
from FunctionCreateSet import CreateSet
from FunctionSelectSet import SelectSet
from FunctionViewOverview import ViewOverview
from FunctionViewSet import ViewSet
from FunctionHelp import Help
from FunctionDeleteSet import DeleteSet


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
        listSetName = []

    currentSetName = listSetName[-1][0]
    currentSetFile = listSetName[-1][1]

    # menu while loop that calls each a function for each action
    menuActive = True
    while menuActive:
        print("\nYour currently selected set is '{0}' in file '{1}'.".format(currentSetName, currentSetFile))
        print('Choosing a view option will view this set.')
        print('\nSelect an Option by entering the corresponding number.')
        print('1:  Create Set')
        print('2:  Select a Different Set')
        print('3:  View Overview of Set')
        print('4:  View Set')
        print('5:  Help')
        print('6:  Delete Set')
        print('7:  Exit')
        menuInput = input('Option:')

        if menuInput == '1':
            print('Create Set Option Chosen\n')
            CreateSet(listSetName)
            currentSetName = listSetName[-1][0]
            currentSetFile = listSetName[-1][1]
        elif menuInput == '2':
            print('Select a Different Set Option Chosen\n')
            setPosition = SelectSet(listSetName)
            currentSetName = listSetName[setPosition][0]
            currentSetFile = listSetName[setPosition][1]
        elif menuInput == '3':
            print('View Overview Option Chosen\n')
            ViewOverview(currentSetName, currentSetFile)
        elif menuInput == '4':
            print('View Set Option Chosen\n')
            ViewSet(listSetName, currentSetName, currentSetFile)
        elif menuInput == '5':
            print('Help Option Chosen\n')
            Help()
        elif menuInput == '6':
            print('Delete Set Option Chosen\n')
            DeleteSet(listSetName, currentSetName, currentSetFile)
        elif menuInput == '7':
            print('Exit Option Chosen\n')
            menuActive = False
            break
        else:
            print('The option you have chosen is invalid.\nTry Again\n\n')


    # Saving listSetName to the file to save it for the next execution
    fileListSetName = open('fileListSetName.txt', 'w')
    for set in listSetName:
        fileListSetName.write(set[0])
        fileListSetName.write(',')
        fileListSetName.write(set[1])
        fileListSetName.write('\n')

    return


MainCLI()