

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
