
def ViewSet(listSetName, setName, setFile):
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
    print('listSet =', listSet)

    # Need to write actual viewing code with viewing options
    # Options on each card: previous, term, image, definition, next, star the card

    print('Showing the cards for {0}'.format(setName))
    number = 0
    while number < len(listSet[1]):
    # for card in listSet[1]:
    #    print('Term: {0}'.format(card[0]))
        print('Term: {0}'.format(listSet[1][number]))

        menuActive = True
        while menuActive:
            print('\nSelect your option.')
            print('1: Previous Card')
            print('2: View Term for Current Card')
            print('3: View Image for Current Card')
            print('4: View Definition for Current Card')
            print('5: Next Card')
            print('6: Star/Unstar the Card')
            print('7: Exit')
            menuOption = input(': ')

            if menuOption == '1':
                print('Previous Card Selected')

            elif menuOption == '2':
                print('View Term Selected')
                print('Term: {0}'.format(card[0]))
            elif menuOption == '3':
                print('View Image Selected')
                print('Image: {0}'.format(card[2]))
            elif menuOption == '4':
                print('View Definition Selected')
                print('Definition: {0}'.format([2]))
            elif menuOption == '5':
                print('Next Card Selected')
                menuActive = False
                break
            elif menuOption == '6':
                print('Star / Unstar Selected')
                if card[3] == 'no':
                    card[3] = 'yes'
                    print('The card has been stared.')
                elif card[3] == 'yes':
                    card[3] = 'no'
                    print('The card has been un starred.')
            elif menuOption == '7':
                print('Exit Option Selected')
                return

    return