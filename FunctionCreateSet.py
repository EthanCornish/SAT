
# from FunctionMain import listSetName


def CreateSet(listSetName):
    # Getting the name of the set and the name of the file from the user
    print('Enter a Name for the set.')
    setName = input(':')
    print('Enter the name of the file to save the set in.')
    fileName = input(':')
    # Defining listSet and adding setName to it
    listSet = []
    listSet.append(setName)
    # Adding the setName and fileName to listSetName
    listSetNameSub = [setName, fileName]
    listSetName.append(listSetNameSub)

    # Setting variables for while loop
    number = 1
    create = True
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
        image = input('Directory for image:')
        # Setting isFav to no as a default value
        isFav = 'no'

        # Adding information for card to listCardSub and adding listCardSub to listCard
        listCardSub = [side1, side2, image, isFav]
        listCard.append(listCardSub)
        print('Your card, {0}, {1}, {2} has been saved as card number {3}.'.format(side1, side2, image, number))

        # Increasing number to move on to next card
        number = number + 1

    # Adding card card to listSet making it complete
    listSet.append(listCard)

    # Saving the set to a file
    file = open(fileName, 'w')
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
