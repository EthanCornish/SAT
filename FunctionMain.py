# Importing the 'CreateSet' Function
from FunctionCreateSet import CreateSet
# Importing the 'EditSet' Function
from FunctionEditSet import EditSet
# Importing the 'SelectSet' Function
from FunctionSelectSet import SelectSet
# Importing the 'ViewOverview' Function
from FunctionViewOverview import ViewOverview
# Importing the 'ViewSet' Function
from FunctionViewSet import ViewSet
# Importing the 'Help' Function
from FunctionHelp import Help
# Importing the 'DeleteSet' Function
from FunctionDeleteSet import DeleteSet

# Needs the 'Import' and 'Export' functions


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

    # Setting the current/default set. Takes the last set on the listSetName list and records the setName and fileName
    currentSetName = listSetName[-1][0]
    currentSetFile = listSetName[-1][1]

    # menu while loop that calls each a function for each action
    menuActive = True
    while menuActive:
        # Infomation about each menu option
        print('\n\n----------------------------------------==========----------------------------------------')
        print("Your currently selected set is '{0}' in file '{1}'.".format(currentSetName, currentSetFile))
        print('Choosing a view option will view this set.')
        print('\nSelect an Option by entering the corresponding number.')
        print('1:  Create Set')
        print('2:  Edit Set')
        print('3:  Select a Different Set')
        print('4:  View Overview of Set')
        print('5:  View Set')
        print('6:  Import Set')
        print('7:  Export Set')
        print('8:  Help')
        print('9:  Delete Set')
        print('10: Exit')
        menuInput = input('Option:')

        # if block to call each menu function
        if menuInput == '1':
            # Runs the create set function
            # Reset the current set to the one just created
            print('Create Set Option Chosen\n')
            CreateSet(listSetName)
            currentSetName = listSetName[-1][0]
            currentSetFile = listSetName[-1][1]
        elif menuInput == '2':
            # Runs the edit set function
            print('Edit Set Option Chosen')
            EditSet(currentSetName, currentSetFile)
        elif menuInput == '3':
            # Runs the select set function
            # Uses the output from the function to set the new current set
            print('Select a Different Set Option Chosen\n')
            setPosition = SelectSet(listSetName)
            currentSetName = listSetName[setPosition][0]
            currentSetFile = listSetName[setPosition][1]
        elif menuInput == '4':
            # Runs the view overview function
            print('View Overview Option Chosen\n')
            ViewOverview(currentSetName, currentSetFile)
        elif menuInput == '5':
            # Runs the view set function
            print('View Set Option Chosen\n')
            ViewSet(currentSetName, currentSetFile)
        elif menuInput == '8':
            # Runs the help function
            print('Help Option Chosen\n')
            Help()
        elif menuInput == '9':
            # Runs the delete set function
            print('Delete Set Option Chosen\n')
            DeleteSet(listSetName, currentSetName, currentSetFile)
        elif menuInput == '10' or menuInput == '0':
            # Exits the program by finishing the loop.
            print('Exit Option Chosen\n')
            menuActive = False
            break
        else:
            # Informs the user of invalid input for menuInput and allows repeated trials
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