
def ViewOverview(listSetName, setName, setFile):
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
            listCard.append(listCardSub)
    listSet.append(listCard)

    print('\nShowing an overview for {0}\n'.format(setName))
    print('Term,    Definition   Image')
    for card in listSet[1]:
        print('{0},      {1},         {2}'.format(card[0], card[1], card[2]))
    return