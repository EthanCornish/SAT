

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
    # Going through each card and printing the infomation
    for card in listSet[1]:
        print('{0},      {1},         {2}'.format(card[0], card[1], card[2]))
    return
