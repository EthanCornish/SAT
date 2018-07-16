
def ExportSet(setName, setFile):
    # Reading the file and creating listSet
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

    # Export File Directory
    print('\n\nEnter the directory for the exported file. (Do not put the / at the end. It will be added automatically'
          '.\nE.g. /Users/19ecornish/Downloads')
    directory = input(':')
    # Name of the file with directory to save the file in a location easily accessed by the user
    fname = ('{0}/{1}.txt'.format(directory, setName))

    # Creating the file that will be exported
    try:
        exportFile = open(fname, 'w')
    except FileNotFoundError:
        print('The directory entered was invalid.')
        return

    # Writing the list to the file, without the first line being the setName
    for a in listSet[1]:
        for b in a:
            exportFile.write(b)
            exportFile.write(',')
        exportFile.write('\n')
    exportFile.close()

    # Informing the user that the file has been exported.
    print('The file has been exported to {0}.\nIt is named {1}.txt'.format(directory, setName))
    return