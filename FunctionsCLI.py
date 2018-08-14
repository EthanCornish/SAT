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


# Function to create listSet as it is detailed in the design            COMPLETE
# setFile is the name of the file the set is stored in
def ListSetCreate(setFile):
    # Opening the given file and defining listSet
    file = open(setFile, 'r')
    listSet = []
    # Getting the name of the set which is the first line of the file and adding it to listSet
    setName = file.readline()
    setName = setName.strip('\n')
    listSet.append(setName)

    # Creating list cards from the design which is a list of lists stored in listSet[1] and contains all of the cards
    # Creates the list by going through each line in the file and addint each line in as a sublist
    listCard = []
    for line in file:
        line = line.strip('\n')
        if line != setName:
            line = line.split(',')
            listCardSub = []
            listCardSub.append(line[0])
            listCardSub.append(line[1])
            listCardSub.append(line[2])
            listCardSub.append(line[3])
            listCard.append(listCardSub)
    listSet.append(listCard)
    return listSet


# Function for saving sets
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
# listCards is the list that contains the cards in the set
def SaveSet(setName, setFile, listCards):
    # Opens the file the set has been stored in
    file = open(setFile, 'w')
    # Add the name of the set as the first line
    file.write(setName)
    file.write('\n')
    # Write each sublist in as a line with commas inbetween indexes in the sublist
    for a in listCards:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()
    return

# Function for deleting sets
# listSetName is a list of lists that stores the name and file name for each set
# setName is the name of the set that is being edited
# setFile is the name of the file the set is in
def DeleteSet(listSetName, setName, setFile):
    # Defining a variable to store the location of the set being deleted
    position = 0
    # Going through each set in listSetName
    for i in listSetName:
        # If the current set the one currently being looked for
        if i[0] == setName:
            # Delete the set from listSetName
            listSetName.pop(position)
            # Deleting the file containing the set
            os.remove(setFile)
            # Exit the function with the modified listSetName
            return listSetName
        position += 1
    # If this line is reached then the set does not exist and therefore for all intents and purposes has been deleted
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
# Returns a boolean based on if the import was successful. True = Successful, False = Unsuccessful
# FunctionMainGui interprets the return
def ImportSet(setDirectory, setName, setFile):
    # Opening the file. If the file directory is incorrect then the function exits.
    try:
        importFile = open(setDirectory, 'r')
    # IsADirectoryError is when the computer recognises that a directory was entered but can not be located
    except FileNotFoundError or IsADirectoryError or FileExistsError:
        return False

    # Defining listCard
    listCard = []

    # Reading the imported file.
    # The csv.reader automatically strips and splits the line
    try:
        # Goes through each line in the file to create listCard from the design
        for line in csv.reader(importFile):
            listCardSub = []
            listCardSub.append(line[0])
            listCardSub.append(line[1])
            listCardSub.append(line[2])
            listCard.append(listCardSub)
    # If the file is not formatted correctly
    except UnicodeDecodeError or IndexError:
        return False
    # Creating listSet from the design
    listSet = [setName, listCard]
    importFile.close()

    # Saving the set to a file
    # Opening the file
    file = open(setFile, 'w')
    # Adding the setName as the first line
    file.write(setName)
    file.write('\n')
    # Add each card in the list as a seperate line, indexes seperated by commas
    for a in listSet[1]:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()
    # If this line was reached then the import was successful
    return True


# Functions for viewing each card individually
# The following two functions contain complex algorithms

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
# Function is called from FunctionMainGui in the ViewNext function which is linked to the ViewPage Function
# Function calls MergeSort and BinarySearch which are my Complex Algorithms
# currentCardNumber is the index value of the current card that is being shown
# listCards is listCards from the design and the rest of the program
# shownCards is a list of integers that is used to store the cards (indexes) that have been shown to avoid a repeat
def RndCardOrder(currentCardNumber, listCards, shownCards):
    # Add the current card to the list of shown cards/indexes
    shownCards.append(currentCardNumber)
    # If the number of previously shown cards is greater than or the same as the number of cards then set x to the
    #       number of cards this will trigger a catch in the ViewSet Function
    # When this condition is met it means that all of the cards have been viewed
    if len(shownCards) >= len(listCards):
        x = len(listCards)
        return x

    # Create a while loop that will generate a random index and check that it has not been generated before r
    generate = True
    while generate:
        # Generate a random number between 0 and the number of index's in the list of drawn numbers
        x = random.randint(0, len(listCards)-1)
        # Make the random number an int to prevent a TypeError or a ValueError
        x = int(x)
        # Sort the cards in the list using the MergeSort function
        shownCards = MergeSort(shownCards)
        # Check if the generated number is in the list by using a BinarySearch
        found = BinarySearch(shownCards, x)
        # If the number was not found output the gnerated number and exit the function
        if not found:
            return x
        # The while loop can not be infinite as there will always be a possible value because the amount of values that
        #       can be generated will exceed the numbers that have been generated because the if condition checks that.
