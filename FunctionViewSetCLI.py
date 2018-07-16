# Importing random library. Used to randomise the order the cards are shown in.
import random

# Randomises the next card displayed.
def CardOrderRnd(currentCardNumber, listSet, shownCards):
    shownCards.append(currentCardNumber)
    # Define a variable to store a randomly generated number
    x = 0
    run = True
    while run:
        # Generate a number
        x = random.randint(0, len(listSet[1])-1)
        try:
            x = int(x)
        except ValueError:
            print('Error X could not be converted into an int after random generate.')
            exit(99)
        # Define variable and list to count what cards have been shown to prevent repeats.
        cycle = 0
        results = []
        while cycle < len(shownCards):
            # Records if the new card has been found before.
            if x == shownCards[cycle]:
                found = 'yes'
            elif x != shownCards[cycle]:
                found = 'no'
            else:
                found = ''
            results.append(found)
            cycle += 1
        # If the card has been found at any point, generate a new number otherwise exit the loop and the function
        for i in results:
            if i == 'yes':
                run = True
                break
            elif i == 'no':
                run = False
        # If everycard has been shown make x the number of cards then the main program
        # will catch it and exit ViewSetFunction
        if len(shownCards) == len(listSet[1]):
            x = len(listSet[1])
            return x

    return x

# Generates the cards individually with three viewing options
def ViewSet(setName, setFile):
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
            listCardSub.append(line[3])
            listCard.append(listCardSub)
    listSet.append(listCard)

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
                            number = CardOrderRnd(number, listSet, shownCards)
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