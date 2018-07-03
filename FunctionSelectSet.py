
def SelectSet(listSetName):
    # Providing a list of sets
    print('Your sets are:')
    for set in listSetName:
        print("  {0}".format(set[0]))
    # Getting name of the set to be changed to
    wantedSet = input('\nName of wanted Set:')
    position = 0
    # going through each set in listSetName
    for i in listSetName:
        if i[0] == wantedSet:
            # if the set is found informing the user and exiting the function
            print('{0} was found and has been selected.'.format(wantedSet))
            return position
        position += 1
    # Informing the user that the set could not be found
    position = -1
    print('{0} was not found. Choose the select set option again to retry.'.format(wantedSet))
    return position
