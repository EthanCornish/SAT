#from FunctionMain import listSetName


def CreateSet(listSetName):
    print('Enter a Name for the set.')
    setName = input(':')
    print('Enter the name of the file to save the set in.')
    fileName = input(':')
    listSet = []
    listSet.append(setName)
    listSetNameSub = [setName, fileName]
    listSetName.append(listSetNameSub)

    number = 1
    create = True
    listCard = []
    while create:
        print('Enter information for card number {0}.'.format(number))
        side1 = input('Term:')
        if side1 == '':
            create = False
            break
        side2 = input('Definition:')
        image = input('Directory for image:')

        listCardSub = [side1, side2, image]
        listCard.append(listCardSub)
        print('Your card, {0}, {1}, {2} has been saved as card number {3}.'.format(side1, side2, image, number))

        number = number + 1

    listSet.append(listCard)

    file = open(fileName, 'w')
    file.write(setName)
    file.write('\n')
    for a in listSet[1]:
        for b in a:
            file.write(b)
            file.write(',')
        file.write('\n')
    file.close()

    return listSetName
