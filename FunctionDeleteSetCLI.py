
# importing the os library to delete files
import os


def DeleteSet(listSetName, setName, setFile):
    # Searching for the wanted set in listSetName.
    position = 0
    found = False
    setToDelete = ''
    while not found:
        # going through each set in listSetName
        for set in listSetName:
            # if the set is found setting it to the variable 'setToDelete' and ending the loop
            if set[0] == setName:
                setToDelete = set[0]
                found = True
                break
            elif set[0] != setName:
                position += 1

    # Getting confirmation from user
    print('Deleting Set {0}'.format(listSetName[position][0]))
    print("Are You Sure? This action can not be undone. 'Yes' or 'No'")
    confirm = input()
    # While loop to give repeated tries to enter valid input
    completed = False
    while not completed:
        # Deletes the set
        if confirm == 'Yes' or confirm == 'yes':
            completed = True
            # Delete the set from listSetName
            listSetName.pop(position)
            # Deleting the file containing the set
            os.remove(setFile)
            # Tells the user the set has been deleted
            print('{0} has been deleted.'.format(setToDelete))
        # Exits the while loop if the user does not want to delete the set
        elif confirm == 'No' or confirm == 'no':
            print('{0} has not been deleted.'.format(setToDelete))
            completed = True
        else:
            # Re asks for valid input
            print("'Yes' or 'No' has not been entered")
            print("Enter 'Yes' or 'No'.")
            confirm = input()
    return
