'''
File contains function for components of the program
Does not include ExportSet function
'''


# os library used to delete files. Used in DeleteSet Function
import os
# csv library used when reading lines from a file. Used in ImportSet Function
import csv
# random library used to generate random numbers. Used in CardOrderRnd function which is called in ViewSet Function
import random


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


# Function to create listSet which contains listCard
# setFile is the name of the file the set is stored in
def ListSetCreate(setFile):
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
    return listSet


# Function for editing sets
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def EditSet(setName, setFile):
    listSet = ListSetCreate(setFile)

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
    listSet = [listSet[0], listCard]

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


# Function for saving sets
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
# listCards is the list that contains the cards in the set
def SaveSet(setName, setFile, listCards):
    # Saving the set using the same code as FunctionCreateSet
    file = open(setFile, 'w')
    file.write(setName)
    file.write('\n')
    for a in listCards:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()

# Function for deleting sets
# listSetName is a list of lists that stores the name and file name for each set
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def DeleteSet(listSetName, setName, setFile):
    # Searching for the wanted set in listSetName.
    position = 0
    # Going through each set in listSetName
    for i in listSetName:
        # if the set is found setting it to the variable 'setToDelete' and ending the loop
        if i[0] == setName:
            # Delete the set from listSetName
            listSetName.pop(position)
            # Deleting the file containing the set
            os.remove(setFile)
            return listSetName
        position += 1
    return listSetName

# Function to change the currently viewed set
# listSetName is a list of lists that stores the name and file name for each set
def SelectSet(wantedSet, listSetName):
    position = 0
    # going through each set in listSetName
    for i in listSetName:
        if i[0] == wantedSet:
            return position
        position += 1
    # Informing the user that the set could not be found
    position = -1
    return position


# Function to import a set
# listSetName is a list of lists that stores the name and file name for each set
def ImportSet(listSetName, setDirectory, setName, setFile):


    # Opening the file. If the file directory is incorrect then the function exits.
    try:
        importFile = open(setDirectory, 'r')
    except FileNotFoundError or IsADirectoryError:
        return False
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
    except UnicodeDecodeError or IndexError:
        return False
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
    return True


# Function to show an overview of the set
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def ViewOverview(setName, setFile):
    # Calling the ListSetCreate Function to generate listSet
    listSet = ListSetCreate(setFile)

    # Printing the name of the set.
    print('\nShowing an overview for {0}\n'.format(setName))
    # Prints infomation in a sort of table format however it is not aligned because the final product will be in a GUI
    print('Term,    Definition,   Image')
    # Going through each card and printing the information
    for card in listSet[1]:
        print('{0},      {1},         {2}'.format(card[0], card[1], card[2]))
    return





# Functions for viewing each card individually


# The following functions contain complex algorithms

# Function for performing a Merge Sort on a given list containing integer or string values
def MergeSort(list0):
    # Checks if the given list contains 1 or no items. If it does than the list is sorted.
    if len(list0) == 1 or len(list0) == 0:
        return list0

    # Takes middle point in the list and is used to slice the list into two halves
    midPoint = int(len(list0)/2)
    # Define two lists by slicing the given list in half. list1 is the first half and list2 is the second half
    list1 = list0[0:midPoint]
    list2 = list0[midPoint:]

    # Calls this function (MergeSort) recursively for the two lists.
    MergeSort(list1)
    MergeSort(list2)

    # Defining a counting variable for each list
    # count0 is for list0
    count0 = 0
    # count1 is for list1
    count1 = 0
    # count2 is for list2
    count2 = 0

    # Goes iterates through until there are no more index values in either list
    while count1 < len(list1) and count2 < len(list2):
        # Checks if the current value for list1 is less than the current value for list2
        if list1[count1] < list2[count2]:
            # If the list1 value is smaller than the value from list1 is placed in list0
            list0[count0] = list1[count1]
            # Increases the count for list1 as that previous value for list1 has already been checked against
            count1 += 1
        # If the list1 value was not smaller and therefore was equal or larger
        else:
            # Set the current value in the main list to the value from list2
            list0[count0] = list2[count2]
            # Increases the count for list1 as that previous value for list1 has already been checked against
            count2 += 1
        # Increases the count value for the main list as the previous value has just been rewritten
        count0 += 1

    # Goes through remaining values in list1 that were not reached in the first while loop
    while count1 < len(list1):
        # Replaces the current main list value with the value from list1
        list0[count0] = list1[count1]
        # Increases the count value for list0 and list1 as the previous have just been used
        count0 += 1
        count1 += 1

    # Goes through remaining values in list2 that were not reached in the first while loop
    while count2 < len(list2):
        # Replaces the current main list value with the value from list2
        list0[count0] = list2[count2]
        # Increases the count value for list0 and list2 as the previous have just been used
        count0 += 1
        count2 += 1

    # Returns the sorted list
    return list0


# Binary Search Algorithm to determine is a given number is present in a list
# list argument is a sorted list that can contain integers or strings
# wanted argument is the value that is being looked for. Can be an integer or a string
def BinarySearch(list, wanted):

    # Define a variable to store the start point in the segment of the list the is being used
    first = int(0)
    # Define a variable to store the end point in the segment of the list the is being used
    last = int(len(list) - 1)
    # first and last are defined as ints to prevent a TypeError or a ValueError

    # Iterates through until the start point in the list has passed the
    while first <= last:
        # Defining a variable to store the location of the center of the list. As an int so it is rounded in the
        #   case of an even list
        midPoint = int((first + last) / 2)

        # Checks is the middle value is the number being looked for
        if list[midPoint] == wanted:
            # If the number is the wanted number then exit the function as 'True'
            return True
        # If the middle value is not the wanted value
        else:
            # Check if the wanted number is smaller
            if wanted < list[midPoint]:
                # If the wanted number is smaller reset the end point of the list to 1 index less (can be one index
                #       less as the midpoint has been checked.
                last = midPoint - 1
            # If the wanted number is not smaller
            else:
                # Reset the start point of the list to 1 index greater than the midpoint (can be one index more as
                #       the midpoint has been checked.
                first = midPoint + 1

    # If this line of code has been reached than the value was not found and the function is exited as False
    return False


# Function to generate a random number that has not been previously generated.
def RndCardOrder(currentCardNumber, listSet, shownCards):
    # Add the current card to the list of shown cards
    shownCards.append(currentCardNumber)

    # If the number of previously shown cards is the same as the number of cards then set x to the number of cards
    #   this will trigger a catch in the ViewSet Function
    if len(shownCards) == len(listSet[1]):
        x = len(listSet[1])
        return x

    generate = True
    while generate:
        # Generate a random number between 0 and the number of index's in the list of drawn numbers
        x = random.randint(0, len(listSet[1])-1)
        # Make the random number an int to prevent a TypeError
        x = int(x)
        # Sort the cards in the list
        shownCards = MergeSort(shownCards)

        if not BinarySearch(shownCards, x):
            return x

# Generates the cards individually with three viewing options
def ViewSet(setName, setFile):
    # Calling the ListSetCreate Function to generate listSet
    listSet = ListSetCreate(setFile)

    # Setting the viewing options

    # setting the DefaultSideOption
    # Getting input
    print('\nDefault Side Shown:\n1: Term\n2: Definition\n3: Image')
    defaultSideInput = input(':')
    # If the input is 1 then the option is set to term and the user is notified
    if defaultSideInput == '1':
        defaultSide = 'Term'
        print('The Default Side has been set to Term')
    # If the input is 2 then the option is set to definition and the user is notified
    elif defaultSideInput == '2':
        defaultSide = 'Def'
        print('The Default Side has been set to Definition')
    # If the input is 3 then the option is set to image and the user is notified
    elif defaultSideInput == '3':
        defaultSide = 'Img'
        print('The Default Side has been set to Image')
    # If 1, 2 or 3 are not entered the option is set to term and the user is notified
    else:
        defaultSide = 'Term'
        print('Invalid input was entered for the default side.\nIt has been set to term.')

    # setting the CardOrderOption
    # Getting input
    print('\nCard Order:\n1: Original\n2: Random')
    cardOrderInput = input(': ')
    # If the input is 1 then the option is set to Origional and the user is notified
    if cardOrderInput == '1':
        cardOrder = 'Org'
        print('The cards will be shown in their original order.')
    # If the input is 2  then the option is set to Randomised and the user is notified
    elif cardOrderInput == '2':
        cardOrder = 'Rnd'
        print('The cards will be shown in a randomised order.')
    # If 1 or 2 is not entered the option is set to origional and the user is notified.
    else:
        cardOrder = 'Org'
        print('Invalid input was entered for the Card Order.\nThe cards will be shown in their original order.')

    # setting ViewFullFavOption
    # Getting input
    print('\nFull Set or Starred Cards:\n1: Full Set\n2: Starred Cards Only')
    viewFullFavInput = input(': ')
    # If the input is 1 then the option is set to Full Set and the user is notified
    if viewFullFavInput == '1':
        viewFullFav = 'Full'
        print('The Full Set will be shown.')
    # If the input is 1 then the option is set to Starred Cards Only and the user is notified
    elif viewFullFavInput == '2':
        viewFullFav = 'Star'
        print('Only Starred Cards will be shown')
    else:
        viewFullFav = 'Full'
        print('Invalid input was entered.\nAll of the cards will be shown.')

    # Start of main block

    # Defining variables and informing the user of the set
    print('\n\nShowing the cards for {0}'.format(setName))
    number = 0
    cycles = 0
    shownCards = []
    # While loop ensures that the card number being shown exists and prevents an IndexError
    while number < len(listSet[1]):
            # Setting variable to store the menu option selected
            menuOption = '0'

            # If the user selected All cards or If the user selected starred cards and the current card is starred
            if viewFullFav == 'Full' or viewFullFav == 'Star' and listSet[1][number][3] == 'yes':

                # Displaying the default side of the current card
                if defaultSide == 'Term':
                    print('Term: {0}'.format(listSet[1][number][0]))
                elif defaultSide == 'Def':
                    print('Definition: {0}'.format(listSet[1][number][1]))
                elif defaultSide == 'Img':
                    print('Image: {0}'.format(listSet[1][number][2]))

                # Menu for the actions the users can perform while viewing a card. Will be buttons in the GUI
                subMenuActive = True
                while subMenuActive:
                    # Providing options for the user and getting input
                    print('\nSelect your option.')
                    print('1: Previous Card')
                    print('2: View Term for Current Card')
                    print('3: View Image for Current Card')
                    print('4: View Definition for Current Card')
                    print('5: Next Card')
                    print('6: Star/Unstar the Card')
                    print('7: Exit')
                    menuOption = input(': ')

                    # If block to run each option
                    if menuOption == '1':
                        # Previous card option
                        print('Previous Card Selected')

                        # If the card order is original
                        if cardOrder == 'Org':
                            # Checks if the previous card exists and is starred if not then it informs the user.
                            if listSet[1][number - 1][3] == 'no' and number - 1 == 0:
                                print('There are no previous cards that are marked as starred.\n')
                            # Changes to previous card
                            number -= 1
                            # If starred cards only and there is a previous card
                            if viewFullFav == 'Star' and number - 1 >= 0:
                                # Change to a previous card until a starred card is reached
                                while listSet[1][number][3] == 'no':
                                    number -= 1
                            # If there aren't any previous cards inform the user and set the current card
                            #   to the first card
                            if number < 0:
                                print('There are no Previous Cards')
                                number = 0
                        # If the card order is randomised
                        elif cardOrder == 'Rnd':
                            # If only one card has been shown then the current card is the first card
                            if len(shownCards) == 1:
                                x = shownCards[0]
                            else:
                                # Reverses the list of shown cards into a new list
                                shownCardsReversed = shownCards.copy()
                                shownCardsReversed.reverse()
                                try:
                                    # Sets the current card to the card that was shown the number of times the previous
                                    # card has been shown ago
                                    x = shownCardsReversed[cycles]
                                except IndexError:
                                    # If the first card shown is the current card then the current card is the number
                                    #   of cards in the list which triggers an exit out of the ViewSet Function
                                    print('No previous card to go back to.')
                                    number = len(listSet[1])
                                    break
                                # Increases the variable to counts the number of times the uses has gone to a
                                #   previous card
                                cycles += 1
                            # Sets the card being shown to the random number generated
                            number = x
                        # Exits the menu
                        break
                    elif menuOption == '2':
                        # View the term of the current card
                        print('\nView Term Selected')
                        # Displays the term of the current card
                        print('\nTerm: {0}'.format(listSet[1][number][0]))
                    elif menuOption == '3':
                        # View the image for the current card
                        print('\nView Image Selected')
                        # Displays the image directory of the current card, in the GUI it will be the image
                        print('Image: {0}'.format(listSet[1][number][2]))
                    elif menuOption == '4':
                        # Displays the definition of the current card
                        print('\nView Definition Selected')
                        # Displays the definition of the current card
                        print('Definition: {0}'.format(listSet[1][number][1]))
                    elif menuOption == '5':
                        # Next Card Option
                        print('\nNext Card Selected')

                        # If the card order is original
                        if cardOrder == 'Org':
                            # Change the card being shown to the next in the list
                            number += 1
                        # If the card order is random
                        elif cardOrder == 'Rnd':
                            # Call the CardOrderRnd Function
                            number = RndCardOrder(number, listSet, shownCards)
                        # Decrese the number of times previous card has been selected
                        cycles -= 1
                        # Exit the menu
                        break
                    elif menuOption == '6':
                        # If the card is not starred then star the card and inform the user
                        if listSet[1][number][3] == 'no':
                            listSet[1][number][3] = 'yes'
                            print('\nThe card has been stared.')
                        # If the card is starred then un star the card and inform the user
                        elif listSet[1][number][3] == 'yes':
                            listSet[1][number][3] = 'no'
                            print('\nThe card not starred.')
                    elif menuOption == '7':
                        # Exit Option

                        # Inform the user
                        print('\nExit Option Selected')
                        # Rewrite the set to the file
                        # This is needed as the set may have changed which cards are starred
                        file = open(setFile, 'w')
                        file.write(setName)
                        file.write('\n')
                        for a in listSet[1]:
                            for b in a:
                                file.write(b)
                                file.write(',')
                            file.write('\n')
                        file.close()
                        return
            # If only starred cards are being shown and the current card is not starred
            else:
                # If the user did not select the previous card option then increase the current card
                if menuOption != '1':
                    number += 1
    # Inform the user if the have seen all of the cards
    print('There are no more cards. Exiting View Set.')

    # Rewrite the set to the file
    # This is needed as the set may have changed which cards are starred
    file = open(setFile, 'w')
    file.write(setName)
    file.write('\n')
    for a in listSet[1]:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()
    return