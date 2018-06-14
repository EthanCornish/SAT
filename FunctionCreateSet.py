
def CreateSet(listSetName):
    print('Enter a Name for the set.')
    setName = input(':')
    print('Enter the name of the file to save the set in.')
    fileName = input(':')
    listSet = []
    listSet[0].append(setName)
    listSetNameSub = [setName, fileName]
    listSetName.append(listSetNameSub)

    number = 1
    create = True
    while create:
        create = False
        print('Enter infomation for card number {0} to be?'.format(number))
        side1 = input('Term:')
        side2 = input('Definition:')
        image = input('Directory for image:')

        listCardSub = [side1, side2, image]
        listSet[0][number-1].append(listCardSub)
        print('Your card, {0}, {1}, {2} has been saved as card number {3}.'.format(side1, side2, image, number))

        number = number + 1
        next = input('Another Card? "Yes", "No"')
        if next == 'Yes' or next == 'yes':
            create = True

    file = open(fileName, 'w')
    file.write(setName)
    file.write('\n')
    for element in listSet[1]:
        file.write(element)
        file.write('\n')
    file.close()

    return listSetName
