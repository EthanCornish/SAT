import random

def ViewSet(setName, setFile):
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
    # Done: defaultSide, ViewFullFav
    # To be completed: FlipMode, cardOrder

    # setting the FlipModeOption
    print('\nFlip Mode:\n1: Manual\n2: Automatic')
    flipModeInput = input(': ')
    if flipModeInput == '1':
        flipMode = 'manual'
        print('The flip mode has been set to manual')
    elif flipModeInput == '2':
        flipMode = 'auto'
        print('The flip mode has been set to automatic')
    else:
        defaultSide = 'manual'
        print('Invalid input was entered for the flip mode.\nIt has been set to manual.')

    # setting the DefaultSideOption
    print('\nDefault Side Shown:\n1: Term\n2: Definition\n3: Image')
    defaultSideInput = input(':')
    if defaultSideInput == '1':
        defaultSide = 'Term'
        print('The Default Side has been set to Term')
    elif defaultSideInput == '2':
        defaultSide = 'Def'
        print('The Default Side has been set to Definition')
    elif defaultSideInput == '3':
        defaultSide = 'Img'
        print('The Default Side has been set to Image')
    else:
        defaultSide = 'Term'
        print('Invalid input was entered for the default side.\nIt has been set to term.')

    # setting the CardOrderOption
    print('\nCard Order:\n1: Original\n2: Random')
    cardOrderInput = input(': ')
    if cardOrderInput == '1':
        cardOrder = 'Org'
        print('The cards will be shown in their original order.')
    elif cardOrderInput == '2':
        cardOrder = 'Rnd'
        print('The cards will be shown in a randomised order.')
    else:
        cardOrder = 'Org'
        print('Invalid input was entered for the Card Order.\nThe cards will be shown in their original order.')

    # setting ViewFullFavOption
    print('\nFull Set or Starred Cards:\n1: Full Set\n2: Starred Cards Only')
    viewFullFavInput = input(': ')
    if viewFullFavInput == '1':
        viewFullFav = 'Full'
        print('The Full Set will be shown.')
    elif viewFullFavInput == '2':
        viewFullFav = 'Star'
        print('Only Starred Cards will be shown')
    else:
        viewFullFav = 'Full'
        print('Invalid input was entered.\nAll of the cards will be shown.')


    print('\n\nShowing the cards for {0}'.format(setName))
    number = 0
    while number <= len(listSet[1]):
        print('DEBUG 2 number =', number)
        menuActive = True
        while menuActive:
            menuOption = '0'
            if viewFullFav == 'Full' or viewFullFav == 'Star' and listSet[1][number][3] == 'yes':

                # Checking if the card is starred and if it should be shown
                if viewFullFav == 'Full':
                    # Displaying the default side
                    if defaultSide == 'Term':
                        print('len(listSet[1] =', len(listSet[1]))
                        print('len(listSet[1][number] =', len(listSet[1][number]))
                        print('Term: {0}'.format(listSet[1][number][0]))
                    elif defaultSide == 'Def':
                        print('Definition: {0}'.format(listSet[1][number][1]))
                    elif defaultSide == 'Img':
                        print('Image: {0}'.format(listSet[1][number][2]))

                elif viewFullFav == 'Star' and listSet[1][number][3] == 'yes':
                    # Displaying the default side
                    if defaultSide == 'Term':
                        print('Term: {0}'.format(listSet[1][number][0]))
                    elif defaultSide == 'Def':
                        print('Definition: {0}'.format(listSet[1][number][1]))
                    elif defaultSide == 'Img':
                        print('Image: {0}'.format(listSet[1][number][2]))

                subMenuActive = True
                while subMenuActive:
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
                        if listSet[1][number - 1][3] == 'no' and number - 1 == 0:
                            print('There are no previous cards that are marked as starred.\n')
                        number -= 1
                        subMenuActive = False
                        break
                    elif menuOption == '2':
                        print('\nView Term Selected')
                        print('\nTerm: {0}'.format(listSet[1][number][0]))
                    elif menuOption == '3':
                        print('\nView Image Selected')
                        print('Image: {0}'.format(listSet[1][number][2]))
                    elif menuOption == '4':
                        print('\nView Definition Selected')
                        print('Definition: {0}'.format(listSet[1][number][1]))
                    elif menuOption == '5':
                        print('\nNext Card Selected')
                        if cardOrder == 'Org':
                            number += 1
                        elif cardOrder == 'Rnd':
                            x = -1
                            print('number =', number)
                            print('x =', x)
                            print('len(listSet[1]) =', len(listSet[1]))
                            x = random.randint(0,len(listSet[1]))
                            x = int(x)
                            if x == number:
                                x = random.randint(0, len(listSet[1])-1)
                                x = int(x)
                            print('number =', number)
                            print('x =', x)
                            number = x

                        subMenuActive = False
                        break
                    elif menuOption == '6':
                        if listSet[1][number][3] == 'no':
                            listSet[1][number][3] = 'yes'
                            print('\nThe card has been stared.')
                        elif listSet[1][number][3] == 'yes':
                            listSet[1][number][3] = 'no'
                            print('\nThe card has been un starred.')
                    elif menuOption == '7':
                        print('\nExit Option Selected')

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
            else:
                print('else block after menuOptions run')
                if menuOption != '1':
                    number += 1
            #if number == len(listSet):
            print('DEBUG 1 number =', number)
            print('DEBUG 1 len(listSet[1])', len(listSet[1]))
            menuActive = False
            #    break

    print('There are no more cards. Exiting View Set.')

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