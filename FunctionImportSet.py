import csv


def ImportSet(listSetName):
    # Providing Basic Guidelines
    print('Imported sets must be a CSV (Comma Separated Value) file in the following form;')
    print('term,definition,img_directory\nterm,definition,img_directory\nterm,definition,img_directory\n...,...,...')
    print('Where each line represents a different card.\n\n')

    # Getting the name of the set and the name of the file from the user
    print('\nEnter a Name for the set.')
    setName = input(':')
    print('Enter the name of the file to save the set in.')
    setFile = input(':')

    # Adding the setName and fileName to listSetName
    # The adding to listSetName is at the end in case the file directory is invalid.
    listSetNameSub = [setName, setFile]
    listSetName.append(listSetNameSub)

    # Getting the location of the file the set is stored in
    print('Location of the file (file directory). E.g. /Users/19ecornish/Downloads/fileName.csv')
    setDirectory = input(':')

    # Opening the file. If the file directory is incorrect then the function exits.
    try:
        importFile = open(setDirectory, 'r')
    except FileNotFoundError:
        print('The file could not be found.\nExiting Import Set')
        return
    # Defining listCard
    listCard = []

    # Reading the imported file.
    # The csv.reader automatically strips and splits the line
    try:
        for line in csv.reader(importFile):
            listCardSub = []
            listCardSub.append(line[0])
            listCardSub.append(line[1])
            listCardSub.append(line[2])
            listCard.append(listCardSub)
    # If a UnicodeDecodeError occurs due to the file format the functions exits without crashing.
    except UnicodeDecodeError:
        print('Invalid file type.\nExiting Import Set')
        return listSetName
    listSet = [setName, listCard]
    importFile.close()

    # Saving the set to a file
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

    listSetName.append(listSetNameSub)
    return listSetName
