'''
File contains function for components of the program
Does not include the ViewSet function or ExportSet function
'''


# os library used to delete files. Used in DeleteSet Function
import os
# csv library used when reading lines from a file. Used in ImportSet Function
import csv


# Function for creating sets
# listSetName is a list of lists that stores the name and file name for each set
def CreateSet(listSetName):
    # Getting the name of the set and the name of the file from the user
    print('Enter a Name for the set.')
    # setName is the name of the set
    setName = input(':')
    print('Enter the name of the file to save the set in.')
    # setFile is the name of the file the set is stored in
    setFile = input(':')
    # Defining listSet and adding setName to it
    # listSet contains all of the cards in a set and it's name
    listSet = []
    listSet.append(setName)
    # Adding the setName and setFile to listSetName
    # listSetNameSub is a sub list of listSetName that has the name and file name for the set being created
    listSetNameSub = [setName, setFile]
    listSetName.append(listSetNameSub)

    # Setting variables for while loop
    # number is a counting variable used to determine the number of the card being created
    number = 1
    # create is a boolean that is used to activate the while loop
    create = True
    # listCard is a sublist of listSet (listSet[1]) and stores all of the cards in a set
    listCard = []
    # While loop for creating cards
    while create:
        print('Enter information for card number {0}.'.format(number))
        # Getting input for the term of the card
        side1 = input('Term:')
        # If the user enters \n exiting the while loop
        if side1 == '':
            break
        # Getting input for the term and directory for the image of the card
        side2 = input('Definition:')
        imageDir = input('Directory for image:')
        # Setting isFav to no as a default value
        isFav = 'no'

        # Adding information for card to listCardSub and adding listCardSub to listCard
        listCardSub = [side1, side2, imageDir, isFav]
        listCard.append(listCardSub)
        print('Your card, {0}, {1}, {2} has been saved as card number {3}.'.format(side1, side2, imageDir, number))

        # Increasing number to move on to next card
        number += 1

    # Adding card card to listSet making it complete
    listSet.append(listCard)

    # Saving the set to a file
    file = open(setFile, 'w')
    file.write(setName)
    file.write('\n')
    for a in listSet[1]:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()

    print('Set Saved')

    return listSetName


# Function for editing sets
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def EditSet(setName, setFile):
    # Reading file and creating listSet
    # This may be put in a different function to be used by FunctionViewOverview and FunctionViewSet
    file = open(setFile, 'r')
    listSet = []
    fileSetName = file.readline()
    fileSetName = fileSetName.strip('\n')
    listSet.append(fileSetName)

    listCard = []
    for line in file:
        line = line.strip('\n')
        if line != fileSetName:
            line = line.split(',')
            listCardSub = []
            listCardSub.append(line[0])
            listCardSub.append(line[1])
            listCardSub.append(line[2])
            listCardSub.append(line[3])
            listCard.append(listCardSub)
    listSet.append(listCard)

    # Providing information and instructions for the user
    print('\nThe set currently contains {0} cards.'.format(len(listSet[1])))

    print("\nThe program will go through each card and show the current term/definition/image directory.")
    print("Type in the new information to change it then select the enter/return key on the keyboard.")
    print("To leave as is select the enter/return key without typing anything.\n\n")

    # Setting variables for the while loop
    number = 1
    create = True
    listCard = []
    # While loop for existing cards
    while create:
        print('Enter information for card number {0}.'.format(number))
        # Telling the user what the current information is, getting new information. Repeats for definition and imageDir
        print('Current Term: {0}'.format(listSet[1][number-1][0]))
        # if the new input is different changing the old input to the new version. Repeats for definition and imageDir
        side1New = input('New Term: ')
        if side1New != '':
            side1 = side1New
        else:
            side1 = listSet[1][number-1][0]

        print('Current Definition: {0}'.format(listSet[1][number - 1][1]))
        side2New = input('New Definition: ')
        if side2New != '':
            side2 = side2New
        else:
            side2 = listSet[1][number - 1][1]

        print('Current Image Directory: {0}'.format(listSet[1][number - 1][2]))
        print('Current Image Directory: {0}'.format(listSet[1][number - 1][2]))
        imageDirNew = input('New Image Directory: ')
        if imageDirNew != '':
            imageDir = imageDirNew
        else:
            imageDir = listSet[1][number - 1][2]

        # Setting the isFav to the previous isFav

        isFav = listSet[1][number-1][3]

        # Adding card information to listCardSub then adding listCardSub to listCard
        listCardSub = [side1, side2, imageDir, isFav]
        listCard.append(listCardSub)
        # Telling the user what their card is
        print('Your card: {0}, {1}, {2} has been saved as card number {3}.\n'.format(side1, side2, imageDir, number))

        # Adding a value to number and checking if the next card exists to prevent and Index Error
        number = number + 1

        if number > len(listSet[1]):
            create = False

    # Asking the user if they wish to extend the set
    print("Add more cards to the set? 'Yes', 'No'")
    more = input(': ')

    # if the user does want to add more cards
    if more == 'yes' or more == 'Yes':
        print('Adding new cards')

        # Same loop as FunctionCreateSet
        create = True
        while create:
            print('Enter information for card number {0}.'.format(number))
            side1 = input('Term:')
            if side1 == '':
                create = False
                break
            side2 = input('Definition:')
            imageDir = input('Directory for image:')
            isFav = 'no'

            listCardSub = [side1, side2, imageDir, isFav]
            listCard.append(listCardSub)
            print('Your card, {0}, {1}, {2} has been saved as card number {3}.'.format(side1, side2, imageDir, number))

            number = number + 1

    # If the user doesn't want to add more cards or enters invalid input.
    elif more == 'no' or more == 'No':
        print('No more cards to add. Saving Set')
    else:
        print('Invalid input entered.')
        print('Saving Set')

    # Redefining listSet
    listSet = [setName, listCard]

    # Saving the set using the same code as FunctionCreateSet
    file = open(setFile, 'w')
    file.write(setName)
    file.write('\n')
    for a in listSet[1]:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()

    print('Set Saved')

    return


# Function for deleting sets
# listSetName is a list of lists that stores the name and file name for each set
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def DeleteSet(listSetName, setName, setFile):
    # Searching for the wanted set in listSetName.
    position = 0
    found = False
    setToDelete = ''
    while not found:
        # going through each set in listSetName
        for set in listSetName:
            # if the set is found setting it to the variable 'setToDelete' and ending the loop
            if set[0] == setName:
                setToDelete = set[0]
                found = True
                break
            elif set[0] != setName:
                position += 1

    # Getting confirmation from user
    print('Deleting Set {0}'.format(listSetName[position][0]))
    print("Are You Sure? This action can not be undone. 'Yes' or 'No'")
    confirm = input()
    # While loop to give repeated tries to enter valid input
    completed = False
    while not completed:
        # Deletes the set
        if confirm == 'Yes' or confirm == 'yes':
            completed = True
            # Delete the set from listSetName
            listSetName.pop(position)
            # Deleting the file containing the set
            os.remove(setFile)
            # Tells the user the set has been deleted
            print('{0} has been deleted.'.format(setToDelete))
        # Exits the while loop if the user does not want to delete the set
        elif confirm == 'No' or confirm == 'no':
            print('{0} has not been deleted.'.format(setToDelete))
            completed = True
        else:
            # Re asks for valid input
            print("'Yes' or 'No' has not been entered")
            print("Enter 'Yes' or 'No'.")
            confirm = input()
    return


# Function to change the currently viewed set
# listSetName is a list of lists that stores the name and file name for each set
def SelectSet(listSetName):
    # Providing a list of sets
    print('Your sets are:')
    for set in listSetName:
        print("  {0}".format(set[0]))
    # Getting name of the set to be changed to
    wantedSet = input('\nName of wanted Set:')
    position = 0
    # going through each set in listSetName
    for i in listSetName:
        if i[0] == wantedSet:
            # if the set is found informing the user and exiting the function
            print('{0} was found and has been selected.'.format(wantedSet))
            return position
        position += 1
    # Informing the user that the set could not be found
    position = -1
    print('{0} was not found. Choose the select set option again to retry.'.format(wantedSet))
    return position


# Function to import a set
# listSetName is a list of lists that stores the name and file name for each set
def ImportSet(listSetName):
    # Providing Basic Guidelines
    print('Imported sets must be a CSV (Comma Separated Value) file in the following form;')
    print('term,definition,img_directory\nterm,definition,img_directory\nterm,definition,img_directory\n...,...,...')
    print('Where each line represents a different card.\n\n')

    # Getting the name of the set and the name of the file from the user
    print('\nEnter a Name for the set.')
    setName = input(':')
    print('Enter the name of the file to save the set in.')
    setFile = input(':')

    # Adding the setName and fileName to listSetName
    # The adding to listSetName is at the end in case the file directory is invalid.
    listSetNameSub = [setName, setFile]
    listSetName.append(listSetNameSub)

    # Getting the location of the file the set is stored in
    print('Location of the file (file directory). E.g. /Users/19ecornish/Downloads/fileName.csv')
    setDirectory = input(':')

    # Opening the file. If the file directory is incorrect then the function exits.
    try:
        importFile = open(setDirectory, 'r')
    except FileNotFoundError:
        print('The file could not be found.\nExiting Import Set')
        return
    # Defining listCard
    listCard = []

    # Reading the imported file.
    # The csv.reader automatically strips and splits the line
    try:
        for line in csv.reader(importFile):
            listCardSub = []
            listCardSub.append(line[0])
            listCardSub.append(line[1])
            listCardSub.append(line[2])
            listCard.append(listCardSub)
    # If a UnicodeDecodeError occurs due to the file format the functions exits without crashing.
    except UnicodeDecodeError:
        print('Invalid file type.\nExiting Import Set')
        return listSetName
    listSet = [setName, listCard]
    importFile.close()

    # Saving the set to a file
    file = open(setFile, 'w')
    file.write(setName)
    file.write('\n')
    for a in listSet[1]:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()

    print('Set Saved')

    listSetName.append(listSetNameSub)
    return listSetName


# Function to show an overview of the set
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def ViewOverview(setName, setFile):
    # Reading file and creating listSet
    file = open(setFile, 'r')
    listSet = []
    fileSetName = file.readline()
    fileSetName = fileSetName.strip('\n')
    listSet.append(fileSetName)

    listCard = []
    for line in file:
        line = line.strip('\n')
        if line != fileSetName:
            line = line.split(',')
            listCardSub = []
            listCardSub.append(line[0])
            listCardSub.append(line[1])
            listCardSub.append(line[2])
            listCard.append(listCardSub)
    listSet.append(listCard)

    # Printing the name of the set.
    print('\nShowing an overview for {0}\n'.format(setName))
    # Prints infomation in a sort of table format however it is not aligned because the final product will be in a GUI
    print('Term,    Definition,   Image')
    # Going through each card and printing the information
    for card in listSet[1]:
        print('{0},      {1},         {2}'.format(card[0], card[1], card[2]))
    return