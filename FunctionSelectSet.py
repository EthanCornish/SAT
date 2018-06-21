
def SelectSet(listSetName):
    print('Your sets are:')
    for set in listSetName:
        print("  {0} in file: {1}".format(set[0], set[1]))
    wantedSet = input('\nName of wanted Set:')
    print('wantedSet =', wantedSet)
    position = 0
    for i in listSetName:
        if i[0] == wantedSet:
            print('{0} was found and has been selected.'.format(wantedSet))
            print('position =', position)
            return position
        position += 1

    position = -1
    print('{0} was not found. Choose the select set option again to retry.'.format(wantedSet))
    return position