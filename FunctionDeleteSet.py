import os


def DeleteSet(listSetName, setName, fileName):
    position = 0
    found = False
    setToDelete = ''
    while not found:
        for set in listSetName:
            if set[0] == setName:
                setToDelete = set[0]
                found = True
                break
            elif set[0] != setName:
                position += 1
    print('Deleting Set {0}'.format(listSetName[position][0]))
    print("Are You Sure? This action can not be undone. 'Yes' or 'No'")
    confirm = input()
    completed = False
    while not completed:
        if confirm == 'Yes' or confirm == 'yes':
            print('{0} has been deleted.'.format(setToDelete))
            completed = True
            # Delete the set from listSetName
            listSetName.pop(position)
            os.remove(fileName)

        elif confirm == 'No' or confirm == 'no':
            print('{0} has not been deleted.'.format(setToDelete))
            completed = True
        else:
            print("'Yes' or 'No' has not been entered")
            print("Enter 'Yes' or 'No'.")
            confirm = input()
    return
