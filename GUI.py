# Import Lines for external python libraries

# Importing everything in the tkinter library
# tkinter library is used in creating the gui
from tkinter import *
# Specifically importing the message box widget from tkinter. Could not call widget without specific import line
from tkinter import messagebox
# Importing Items from Photo Imaging Library to allow images to be shown in the program
from PIL import Image

# Importing Functions from FunctionsCLI file.
# The Merge Sort and Binary Search functions are not included as they are called from within FunctionsCLI only.
from Functions import ListCardsCreate, SaveSet, DeleteSet, SelectSet, ImportSet, RndCardOrder


# The Class that contains all of the GUI component
class GUI:
    # Initialisation Function                       INITIAL FUNCTION
    def __init__(self, master):
        # Defining master and giving the root window a title
        self.master = master
        master.title('Flash Card')

        # Calling the ViewOverview page to appear by default
        self.ViewOverviewPage(self.master)

    # Function for the ViewOverview Page            PAGE FUNCTION
    # master argument is the root window
    def ViewOverviewPage(self, master):
        # Define variables to store the name and the file of the current set
        self.currentSetName = StringVar()
        self.currentSetName.set(currentSetNameString)
        self.currentSetFile = StringVar()
        self.currentSetFile.set(currentSetFileString)

        # Defining the frame to store everything in the ViewOverview page
        self.fmePage1ViewOverview = Frame(master)

        # Creating the setName label, setting the size colour and font, placing it in the grid
        # Text uses the variable that stores the current set name.
        self.lblSet = Label(self.fmePage1ViewOverview, textvariable=self.currentSetName, bg='#7AEDFB', width=32)
        self.lblSet.config(font=('Arial', 32, 'bold underline'))
        self.lblSet.grid(row=0, column=0, rowspan=1, columnspan=4)

        # Calling the function for the table in ViewOverview
        # listCards is listCards from the design and is created using a function. Initial creation is outside the class
        self.ViewOverviewTable(lstCards)

        # Creating the Create Set button, setting the size and font, placing it in the grid
        # The command calls the Create Page Function. Gives the master agrument as the CreatePage function has a new top frame
        self.btnCreate = Button(self.fmePage1ViewOverview, text='Create Set', width=24,
                                command=lambda *args: self.CreatePage(master))
        self.btnCreate.config(font=('Times', 16))
        self.btnCreate.grid(row=0, column=5, rowspan=1, columnspan=3)

        # The integer variable stores the current status of the button and the table.
        # 0 is View Mode,   1 is the Edit Mode
        # The default is 0
        self.varEditSaveBtnInt = IntVar()
        self.varEditSaveBtnInt.set(0)
        # The string variable stores the text for the Button. It is changed in the function
        self.varEditSaveBtnText = StringVar()
        self.varEditSaveBtnText.set('Edit Set')
        # Creating the Edit Set function, setting the size and font, placing it in the grid
        # The command calls the associated function
        self.btnEditSave = Button(self.fmePage1ViewOverview, textvariable=self.varEditSaveBtnText, width=24,
                                  command=self.ViewOverviewEditSaveBtn)
        self.btnEditSave.config(font=('Times', 16))
        self.btnEditSave.grid(row=2, column=5, rowspan=1, columnspan=3)

        # Variable stores the text entered into the entry field, by default it is set to an instruction
        self.varSelectInput = StringVar()
        self.varSelectInput.set('Enter the Name of the Set you Wish to Change to then click Select.')
        # Creating the entry field for the select set function, setting the size and font, placing it in the grid
        self.entSelect = Entry(self.fmePage1ViewOverview, textvariable=self.varSelectInput, width=20)
        self.entSelect.config(font=('Times', 12))
        self.entSelect.grid(row=3, column=5, rowspan=1, columnspan=2)
        # Creating the button for the select set function, setting the font and size, placing it in the grid
        # The command calls the select set function which uses the text from the entry field
        self.btnSelect = Button(self.fmePage1ViewOverview, text='Select', width=8, command=self.ViewOverviewSelect)
        self.btnSelect.config(font=('Times', 16))
        self.btnSelect.grid(row=3, column=7, rowspan=1, columnspan=1)

        # Creating the frame for the viewing options and placing it in the top grid
        self.fmeOptions = Frame(self.fmePage1ViewOverview)
        self.fmeOptions.grid(row=4, column=5, columnspan=3, rowspan=7)

        # Default Side Option

        # Creating the Default Side viewing options label, setting the font and placing it in the grid
        self.lblDefaultSide = Label(self.fmeOptions, text='Default Side:', anchor=W)
        self.lblDefaultSide.config(font=('Times', 16))
        self.lblDefaultSide.grid(row=0, column=0)

        # Defining a variable to store the input for the Default Side radio buttons
        self.varDefaultSideInput = IntVar()

        # Radio Buttons for default side, setting the font and placing them in the grid.
        self.rbDefaultSideTerm = Radiobutton(self.fmeOptions, text='Term', variable=self.varDefaultSideInput, value=1,
                                             anchor=W, width=8)
        self.rbDefaultSideTerm.config(font=('Times', 14))
        self.rbDefaultSideTerm.grid(row=1, column=0)
        self.rbDefaultSideDef = Radiobutton(self.fmeOptions, text='Definition', variable=self.varDefaultSideInput,
                                            value=2, anchor=W, width=10)
        self.rbDefaultSideDef.config(font=('Times', 14))
        self.rbDefaultSideDef.grid(row=1, column=1)
        self.rbDefaultSideImg = Radiobutton(self.fmeOptions, text='Image', variable=self.varDefaultSideInput, value=3,
                                            anchor=W, width=7)
        self.rbDefaultSideImg.config(font=('Times', 14))
        self.rbDefaultSideImg.grid(row=1, column=2)

        # Setting 'Term' as the default option to act as an existence check by forcing a value
        self.rbDefaultSideTerm.select()

        # View Full/Star Option

        # Creating the Full/Star viewing options label, setting the font and placing it in the grid
        self.lblViewFullStar = Label(self.fmeOptions, text='View:', anchor=W, width=8)
        self.lblViewFullStar.config(font=('Times', 16))
        self.lblViewFullStar.grid(row=2, column=0)

        # Defining a variable to store the input for the Default Side radio buttons
        self.varViewFullStarInput = IntVar()

        # Radio Buttons for View Full/Star side, setting the font and placing them in the grid.
        self.rbViewFull = Radiobutton(self.fmeOptions, text='Full Set', variable=self.varViewFullStarInput, value=1,
                                      width=8, anchor=W)
        self.rbViewFull.config(font=('Times', 14))
        self.rbViewFull.grid(row=3, column=0)
        self.rbViewStar = Radiobutton(self.fmeOptions, text='Starred Cards Only', variable=self.varViewFullStarInput,
                                      value=2, width=16, anchor=W)
        self.rbViewStar.config(font=('Times', 14))
        self.rbViewStar.grid(row=3, column=1, columnspan=2)

        # Setting 'Full' as the default option to act as an existence check by forcing a value
        self.rbViewFull.select()

        # Card Order Option

        # Creating the Card Order viewing options label, setting the font and placing it in the grid
        self.lblCardOrder = Label(self.fmeOptions, text='Card Order:', anchor=W)
        self.lblCardOrder.config(font=('Times', 16))
        self.lblCardOrder.grid(row=4, column=0)

        # Defining a variable to store the input for the Default Side radio buttons
        self.varCardOrderInput = IntVar()

        # Radio Buttons for View Full/Star side, setting the font and placing them in the grid.
        self.rbCardOrderOrg = Radiobutton(self.fmeOptions, text='Original', variable=self.varCardOrderInput, value=1,
                                          anchor=W)
        self.rbCardOrderOrg.config(font=('Times', 14))
        self.rbCardOrderOrg.grid(row=5, column=0)
        self.rbCardOrderRnd = Radiobutton(self.fmeOptions, text='Random', variable=self.varCardOrderInput, value=2,
                                          anchor=W)
        self.rbCardOrderRnd.config(font=('Times', 14))
        self.rbCardOrderRnd.grid(row=5, column=1)

        # Setting 'Full' as the default option to act as an existence check by forcing a value
        self.rbCardOrderOrg.select()

        # Variables used in ViewPage Function but are defined here as the function is recalled from other functions
        # Defining a variable to store the number of the card that is being shown.
        self.number = 0
        # Defining a list to store the cards that have been shown. Used when the card order option has been set to random
        self.shownCards = []
        # Defining a counting variable to be used when going back to previous cards when the card order option is set to random
        self.cycles = 0
        # Creating the View Set button, setting the size and font, placing it in the grid
        # Command calles the ViewPage function
        self.btnView = Button(self.fmePage1ViewOverview, text='View Set', width=24,
                              command=lambda *args: self.ViewPage(master, self.number))
        self.btnView.config(font=('Times', 16))
        self.btnView.grid(row=11, column=5, rowspan=1, columnspan=3)

        # Creating the delete set button, setting the size and font, placing it in the grid
        # Command calls the corresponding function from FunctionsCLI
        # listSetName argument is listSetName from the design and is defined outside the class
        self.btnDelete = Button(self.fmePage1ViewOverview, text='Delete Set',
                                command=lambda *args: self.ViewOverviewDelete(listSetName))
        self.btnView.config(font=('Times', 16))
        self.btnDelete.grid(row=13, column=5, rowspan=1)

        # Creating a help button, setting the size and font, placing it in the grid
        # Command calls the corresponding function which creates the help page in a sub-window
        self.btnHelp = Button(self.fmePage1ViewOverview, text='Help', width=8, command=self.HelpPage)
        self.btnHelp.config(font=('Times', 16))
        self.btnHelp.grid(row=13, column=7, rowspan=1)

        # Creating the blank spaces used to format the top frame

        # List of lists stores where the blank spaces need to go. Each sublist is a column and the items in the sublist are the rows for the column
        self.lstBlanks = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                          [1, 12], [1, 12, 13], [1, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
        # Defining a counting variable to store the index value of the current sublist
        self.countBlank = 0
        # Goes through each sublist in self.lstBlanks
        while self.countBlank < 9:
            # Goes through each item in the sublist
            for i in self.lstBlanks[self.countBlank]:
                # Creates a label with no text of specific size
                self.lblBlank = Label(self.fmePage1ViewOverview, height=1, width=8)
                self.lblBlank.config(font=('Arial', 10))
                # Placing the label in the grid at column, sublist and row, index of sublist
                self.lblBlank.grid(row=i, column=self.countBlank)
            # Increments the counting variable
            self.countBlank += 1

        # Places the top frame on the grid
        self.fmePage1ViewOverview.grid(column=0, row=0, columnspan=3)

    # Function to create the table in ViewOverview  PAGE CHILD FUNCTION
    def ViewOverviewTable(self, lstCards):

        self.count = 0
        self.lstCards = lstCards

        # A variable to determine the number of rows in the table size using the number of cards
        # x2 because there needs to be a border for each row,   +3 because there is a header column and a top border
        self.noCards = (len(self.lstCards) * 2) + 3

        # Creating the scroll bar by placing the table in a frame in a canvas in a frame
        # Function to configure the canvas
        def CanvasConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=490, height=600)

        # Creating the top frame for the scroll bar and placing it in the grid.
        self.fmeSbTop = Frame(self.fmePage1ViewOverview)
        self.fmeSbTop.grid(row=2, column=1, rowspan=(len(self.lstCards) * 3) + (len(self.lstCards)) + 3, columnspan=3)
        # Creating a canvas top put in the top frame, setting it's size and placing it in the frame
        self.canvas = Canvas(self.fmeSbTop)
        # Creating the sub frame for the scroll bar and setting it's size.
        self.fmeSbSub = Frame(self.canvas, width=530, height=600)
        # Creating the scrollbar and making it vertical
        self.scrollBar = Scrollbar(self.fmeSbTop, orient='vertical', command=self.canvas.yview)
        # Adding the scroll bar to the canvas
        self.canvas.configure(yscrollcommand=self.scrollBar.set)
        self.scrollBar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        # Setting the sub frame inside the frame
        self.canvas.create_window((0, 0), window=self.fmeSbSub, anchor='nw')
        self.fmeSbSub.bind('<Configure>', CanvasConfig)

        # Creating the frame to store the table in as a sub frame of the scroll bar sub frame (that's a sub, sub frame)
        #   this is done as the scroll bar was implemented after the creation of the function and the frame was already established.
        # This frame also stores the view (static) version of the table, another frame stores the edit (active) version of the table
        self.fmeTableView = Frame(self.fmeSbSub)

        # Creating the label for the header for the term column of the view table, setting the font and size, placing it in the grid
        self.lblTermHeader = Label(self.fmeTableView, text='Term', width=12, height=1)
        self.lblTermHeader.config(font=('Times', 18, 'underline'))
        self.lblTermHeader.grid(row=1, column=1)

        # Creating the label for the header for the definition column of the view table, setting the font and the size, placing it in the grid
        self.lblDefHeader = Label(self.fmeTableView, text='Definition', width=22, height=1)
        self.lblDefHeader.config(font=('Times', 18, 'underline'))
        self.lblDefHeader.grid(row=1, column=3)

        # Creating the label for the header for the image directory column of the view table, setting the font and the size, placing it in the grid
        self.lblImgHeader = Label(self.fmeTableView, text='Image Directory', width=12, height=1)
        self.lblImgHeader.config(font=('Times', 17, 'underline'))
        self.lblImgHeader.grid(row=1, column=5)

        # Placing the view table in the grid. The rowspan is determined by the number of cards otherwise the other widgets become displaced
        self.fmeTableView.grid(row=2, column=1, rowspan=((len(self.lstCards) * 3) + (len(self.lstCards)) + 3), columnspan=3)

        # Setting the content for the 'Term' Column
        self.count = 0
        # Loop that goes through each row and if the row is odd (therefore not a border row)
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                # Variable to store the term of the current card, variable is a StringVar but contains a string version of the stringVar in the list
                self.varCurrentTerm = StringVar()
                self.varCurrentTerm.set(self.lstCards[self.count].varTerm)
                # Creating a label where the text is the variable, setting the font and placing it in the grid using the loop as a grid reference for the row
                self.lblTerm = Label(self.fmeTableView, textvariable=self.varCurrentTerm, anchor='w', width=12,
                                     height=3)
                self.lblTerm.config(font=('Times', 14))
                self.lblTerm.grid(row=i, column=1)
                self.count += 1

        # Setting the content for the 'Definition' Column
        # Code block is the same as above however it uses the 1st value in each sub list of self.lstCards instead of the 0th
        self.count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.varCurrentDef = StringVar()
                self.varCurrentDef.set(self.lstCards[self.count].varDef)
                self.lblDef = Label(self.fmeTableView, textvariable=self.varCurrentDef, anchor='w', width=22,
                                    height=3)
                self.lblDef.config(font=('Times', 14))
                self.lblDef.grid(row=i, column=3)
                self.count += 1

        # Setting the content for the 'Image' Column
        # Code block is the same as above however it uses the 2nd value in each sub list of self.lstCards
        self.count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.varCurrentImg = StringVar()
                self.varCurrentImg.set(self.lstCards[self.count].varImg)
                self.lblImg = Label(self.fmeTableView, textvariable=self.varCurrentImg, anchor='w', width=12, height=3)
                self.lblImg.config(font=('Times', 14))
                self.lblImg.grid(row=i, column=5)
                self.count += 1

        # Setting border around the table
        # The label contains no text and is uses a standard colour.
        # The size depends on where the border label is
        # Creating a list to store the cells that have a border label
        self.border = []
        # Loop that iterates for the amount of cards to know how many rows need a border
        for i in range(0, self.noCards):
            # Loop that iterates through every column (there are always seven columns)
            for j in range(0, 7):
                # On even rows and even columns place a label
                if (i % 2) == 0 and (j % 2) == 0:
                    self.lblBorder = Label(self.fmeTableView, width=1, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the first column place a label of the same width as the term labels
                elif (i % 2) == 0 and j == 1:
                    self.lblBorder = Label(self.fmeTableView, width=12, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the third column place a label of the same width as the definition labels
                elif (i % 2) == 0 and j == 3:
                    self.lblBorder = Label(self.fmeTableView, width=22, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the fifth column place a label of the same width as the image directory labels
                elif (i % 2) == 0 and j == 5:
                    self.lblBorder = Label(self.fmeTableView, width=12, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and odd column and not the first row place a label as high as the text labels
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.lblBorder = Label(self.fmeTableView, width=1, height=3, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On the first row and odd column and place a label as high as the header labels
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.lblBorder = Label(self.fmeTableView, width=1, height=2, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)

        # Creating the Edit (Active) version of the table

        # Creating the frame which goes in the scroll bar sub frame in the same way as the View Table's frame
        self.fmeTableEdit = Frame(self.fmeSbSub)

        # Creating the label for the header for the term column of the edit table, setting the font and size, placing it in the grid
        self.lblTermHeader = Label(self.fmeTableEdit, text='Term', width=12, height=1)
        self.lblTermHeader.config(font=('Times', 18, 'underline'))
        self.lblTermHeader.grid(row=1, column=1)

        # Creating the label for the header for the definition column of the edit table, setting the font and size, placing it in the grid
        self.lblDefHeader = Label(self.fmeTableEdit, text='Definition', width=22, height=1)
        self.lblDefHeader.config(font=('Times', 18, 'underline'))
        self.lblDefHeader.grid(row=1, column=3)

        # Creating the label for the header for the image directory column of the edit table, setting the font and size, placing it in the grid
        self.lblImgHeader = Label(self.fmeTableEdit, text='Image', width=12, height=1)
        self.lblImgHeader.config(font=('Times', 18, 'underline'))
        self.lblImgHeader.grid(row=1, column=5)

        # Defining a temporary variable to store the number of card for determining table size
        self.noCards = (len(self.lstCards) * 2) + 3

        # Creating the entry fields

        self.count = 0
        # Defining a list to store the cards after they are edited. Will be a list of lists
        self.lstEditCards = []
        # Loop that goes iterates through every row in the table for the amount of cards
        for i in range(2, self.noCards):
            # Creating a sub list to make adding to the above list easier
            self.lstEditCardsSub = []

            # If the current row is odd
            if (i % 2) == 1:
                # Setting the content for the 'Term' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.varCurrentTerm = StringVar()
                self.varCurrentTerm.set(self.lstCards[self.count].varTerm)
                # Creating an entry field, setting the font, placing in the grid
                self.entTerm = Entry(self.fmeTableEdit, textvariable=self.varCurrentTerm, width=12)
                # Adding the text to the sub list in a StringVar format
                self.lstEditCardsSub.append(self.varCurrentTerm)
                self.entTerm.config(font=('Times', 14))
                self.entTerm.grid(row=i, column=1)

                # Setting the content for the 'Definition' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.varCurrentDef = StringVar()
                self.varCurrentDef.set(self.lstCards[self.count].varDef)
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.entDef = Entry(self.fmeTableEdit, textvariable=self.varCurrentDef, width=22)
                # Adding the text to the sub list in a StringVar format
                self.lstEditCardsSub.append(self.varCurrentDef)
                self.entDef.config(font=('Times', 14))
                self.entDef.grid(row=i, column=3)

                # Setting the content for the 'Image' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.varCurrentImg = StringVar()
                self.varCurrentImg.set(self.lstCards[self.count].varImg)
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.entImg = Entry(self.fmeTableEdit, textvariable=self.varCurrentImg, width=12)
                # Adding the text to the sub list in a StringVar format
                self.lstEditCardsSub.append(self.varCurrentImg)
                self.entImg.config(font=('Times', 14))
                self.entImg.grid(row=i, column=5)

                # Keeping the star/unstar value by adding it to the sublist
                self.varCurrentIsStar = StringVar()
                self.varCurrentIsStar.set(self.lstCards[self.count].varIsStar)
                self.lstEditCardsSub.append(self.varCurrentIsStar)

                # Adding the sublist to the new list
                self.lstEditCards.append(self.lstEditCardsSub)
                self.count += 1

        # Setting border around the table
        # The label contains no text and is uses a standard colour.
        # The size depends on where the border label is
        # Creating a list to store the cells that have a border label
        self.border = []
        # Loop that iterates for the amount of cards to know how many rows need a border
        for i in range(0, self.noCards):
            # Loop that iterates through every column (there are always seven columns)
            for j in range(0, 7):
                # On even rows and even columns place a label
                if (i % 2) == 0 and (j % 2) == 0:
                    self.lblBorder = Label(self.fmeTableEdit, width=1, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the first column place a label of the same width as the term labels
                elif (i % 2) == 0 and j == 1:
                    self.lblBorder = Label(self.fmeTableEdit, width=12, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the third column place a label of the same width as the definition labels
                elif (i % 2) == 0 and j == 3:
                    self.lblBorder = Label(self.fmeTableEdit, width=22, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the fifth column place a label of the same width as the image directory labels
                elif (i % 2) == 0 and j == 5:
                    self.lblBorder = Label(self.fmeTableEdit, width=12, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and odd column and not the first row place a label as high as the text labels
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.lblBorder = Label(self.fmeTableEdit, width=1, height=3, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On the first row and odd column and place a label as high as the header labels
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.lblBorder = Label(self.fmeTableEdit, width=1, height=2, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)

    # Function to change the currently viewed set   COMPLETE
    def ViewOverviewSelect(self):
        # Call the Select Set Function from FunctionsCLI with input from entry field as wantedSet argument.
        # Use the function to gain the index position of the wanted set
        self.location = SelectSet(self.varSelectInput.get(), listSetName)
        # If the set was not found
        if self.location == -1:
            # Inform the user with a showinfo message box and exit function
            messagebox.showinfo('Does not Exist', 'The name of the set you entered does not exist.\n'
                                                  'Re-enter a name and try again.')
            return
        # Reset the currentSetName and currentSetFile using output from SelectSet Function
        self.currentSetName.set(listSetName[self.location][0])
        self.currentSetFile.set(listSetName[self.location][1])

        # Call ListSetCreate Function to recreate listCards but with the new set
        lstCards = ListCardsCreate(self.currentSetFile.get())
        # Recall the table function to update the table with the new list
        self.ViewOverviewTable(lstCards)

    # Function for the ViewOverview Page to change to table from label to entry
    #                                               COMPLETE
    def ViewOverviewEditSaveBtn(self):
        # Define status variable to store if the table is currently showing the view or edit version
        status = self.varEditSaveBtnInt.get()
        # If the table is in view mode
        if status == 0:
            # Set status to the edit mode
            status = 1

            # Remove the view version of the table
            self.fmeTableView.grid_remove()

            # Place the edit version of the table in the grid using the same line as in the other function
            self.fmeTableEdit.grid(row=2, column=1, rowspan=(len(self.lstCards) * 3) + (len(self.lstCards)) + 3, columnspan=3)

            # Change the text on the button
            self.varEditSaveBtnText.set('Save Changes')

        # If the table is in edit mode
        elif status == 1:
            # Set status to the view mode
            status = 0

            # Block to read the edit table and change the list of StringVars to a list of strings
            # Also checks if there is a blank space. If there is inform the user using a showinfo message box and abort the function
            self.lstStrings = []
            for i in self.lstEditCards:
                self.lstStringsSub = []
                self.count = 0
                for j in i:
                    if j.get() != '' or self.count == 3:
                        self.lstStringsSub.append(j.get())
                    else:
                        messagebox.showinfo('Saving', 'Changes could not be saved as there was a blank space.')
                        return
                    self.count += 1
                self.lstStrings.append(self.lstStringsSub)

            # Save the set by rewriting to file using the SaveSet function using FunctionsCLI
            SaveSet(self.currentSetName.get(), self.currentSetFile.get(), self.lstStrings)

            # Create a new ListCards using the ListCardsCreate Function from FunctionsCLI
            lstCards = ListCardsCreate(self.currentSetFile.get())

            # Removes the edit table from the grid
            self.fmeTableEdit.grid_remove()

            # Recalling the Table function using listCards
            self.ViewOverviewTable(lstCards)

            # Place the view version of the table in the grid
            self.fmeTableView.grid(row=2, column=1, rowspan=(len(self.lstCards) * 3) + (len(self.lstCards)) + 3, columnspan=3)

            # Reset the text on the button
            self.varEditSaveBtnText.set('Edit Set')
        # Set the status intVar to the status integer variable
        self.varEditSaveBtnInt.set(status)

    # Function to delete the current set            COMPLETE
    # listSetName argument is listSetName from the design
    def ViewOverviewDelete(self, listSetName):
        # Uses an askyesno message box to recive confirmation from the user about deleting the set
        self.confirm = messagebox.askyesno('Confirm', 'ARE YOU SURE.\n\nThis action can not be undone.', icon='warning')
        # If the user confirms their choice
        if self.confirm:
            # Call the DeleteSet function from FunctionsCLI using the strings from the setName and setFile stringVars
            # Give the deleteSet function listSetName and take it as the output as the function modifies it
            listSetName = DeleteSet(listSetName, self.currentSetName.get(), self.currentSetFile.get())
            # Reset the current setName and setFile to the last set in listSetName as the set that was being viewed has just been deleted
            self.currentSetName.set(listSetName[-1][0])
            self.currentSetFile.set(listSetName[-1][1])
            # Generate a new listCards using the ListSetCreate function. Using the string from the setFile stringVar
            lstCards = ListCardsCreate(self.currentSetFile.get())
            # Recall the table function to generate the table with the new set
            self.ViewOverviewTable(lstCards)
        # If the user backs out of deleting their set
        elif not self.confirm:
            # Inform the user that their cancelation has been confirmed with a showinfo messagebox
            messagebox.showinfo('Confirm', 'Delete Cancelled', icon='warning')
            # Exit the function
            return

    # Function for the Create Page                  PAGE FUNCTION
    # master argument is the root window
    def CreatePage(self, master):
        # Remove the frame containing ViewOverviewPage
        self.fmePage1ViewOverview.grid_remove()

        # Creating the frame to store the contents of the Create Page
        self.fmePage2CreateSet = Frame(master)

        # Creating a variable to store the name of the set.
        self.varName = StringVar()
        # Setting the default text to act as an existance check and an instruction
        self.varName.set('Enter Name of Set')
        # Creating the entry field to enter the name of the set, setting the font, size, colour and placing it in the grid
        self.entName = Entry(self.fmePage2CreateSet, textvariable=self.varName, width=24, bg='#7AEDFB')
        self.entName.config(font=('Arail', 32, 'bold underline'))
        self.entName.grid(row=0, column=0, rowspan=2, columnspan=4)

        # Creating the button to add another row to the table, setting the font and placing it in the grid.
        # Command calls the the function to add or remove a row.
        # The self.varTableRowSpan argument is the amount of rows currently in the table.
        # The 0 tells the function to add a row as the function can add and remove rows
        self.btnAddRow = Button(self.fmePage2CreateSet, text='Add Row', width=16,
                                command=lambda *args: self.CreateChangeRow(self.varTableRowSpan, 0))
        self.btnAddRow.config(font=('Times', 16))
        self.btnAddRow.grid(row=4, column=5, rowspan=1, columnspan=1)

        # Creating the button to remove a row to the table, setting the font and placing it in the grid.
        # Command calls the the function to add or remove a row.
        # The self.varTableRowSpan argument is the amount of rows currently in the table.
        # The 1 tells the function to remove a row as the function can add and remove rows
        self.btnRemoveRow = Button(self.fmePage2CreateSet, text='Remove Row', width=16,
                                   command=lambda *args: self.CreateChangeRow(self.varTableRowSpan, 1))
        self.btnRemoveRow.config(font=('Times', 16))
        self.btnRemoveRow.grid(row=6, column=5, rowspan=1, columnspan=1)

        # Variable to determine the number of rows in the table. And the rowspan of the table.  Can be changed with buttons
        # VarTableRowSpan = (number of cards * 2) + 3, 15 is the default amount of rows
        self.varTableRowSpan = IntVar()
        self.varTableRowSpan = (5 * 2) + 3
        # lstCardsCreate is a list of lists that will contain the entered data
        self.lstCardsCreate = []
        # Calling the function to create the table
        self.CreateTable()

        # Creating the button to save the set that has been created and return to the ViewOverview Page, setting the font and placing it in the grid
        # Command calls the corresponding function
        self.btnSave = Button(self.fmePage2CreateSet, text='Save Set', width=16, command=self.CreateSave)
        self.btnSave.config(font=('Times', 16))
        self.btnSave.grid(row=1, column=5, rowspan=1, columnspan=1)

        # Creating the button to exit the Create page without saving the set, setting the font and placing it in the grid
        # Command calls the corresponding function
        self.btnDelete = Button(self.fmePage2CreateSet, text='Cancel Set Creation', width=16, command=self.CreateDelete)
        self.btnDelete.config(font=('Times', 16))
        self.btnDelete.grid(row=8, column=5, rowspan=1, columnspan=1)

        # Creating the button to call the import set sub window and function, setting the font and placing it in the grid
        # Command calls the corresponding function which creates the sub window and its functionality
        self.btnImport = Button(self.fmePage2CreateSet, text='Import Set', width=16, command=self.CreateImport)
        self.btnImport.config(font=('Times', 16))
        self.btnImport.grid(row=10, column=5, rowspan=1, columnspan=1)

        # Creating the button to call the help sub window, setting the font and placing it in the grid
        # Command calls the help function
        self.btnHelp = Button(self.fmePage2CreateSet, text='Help', width=16, command=self.HelpPage)
        self.btnHelp.config(font=('Times', 16))
        self.btnHelp.grid(row=12, column=5, rowspan=1, columnspan=1)

        # Creating the blank spaces used to format the top frame

        # List of lists stores where the blank spaces need to go. Each sublist is a column and the items in the sublist are the rows for the column
        blanks = [[2, 3, 4, 5, 6, 7, 8, 9], [2], [2], [2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11], [0, 3, 5, 7, 9, 11],
                  [0, 3, 5, 7, 9, 11]]
        # Defining a counting variable to store the index value of the current sublist
        self.countBlank = 0
        # Goes through each sublist in self.lstBlanks
        while self.countBlank < 7:
            # Goes through each item in the sublist
            for i in blanks[self.countBlank]:
                # Creates a label with no text of specific size
                self.lblBlank = Label(self.fmePage2CreateSet, height=1, width=8)
                self.lblBlank.config(font=('Arial', 10))
                # Placing the label in the grid at column, sublist and row, index of sublist
                self.lblBlank.grid(row=i, column=self.countBlank)
            # Increments the counting variable
            self.countBlank += 1

        # Places the top frame on the grid
        self.fmePage2CreateSet.grid(row=0, column=0)

    # Function to create the table in Create Page   PAGE CHILD FUNCTION
    def CreateTable(self):

        # Creating List of StringVars with default values that act as an existence check and an instruction
        # Define a counting variable to store the number of the card
        self.count = 0
        # Checks that the list is empty and therefore has just been created in the CreatePage function
        # Otherwise everything the function is called the list will reset
        if len(self.lstCardsCreate) < 1:
            while self.count < 5:
                # Default text takes the form of the a string and the counter variable
                self.varCardT = StringVar()
                self.varCardT.set('Enter Term')

                self.varCardD = StringVar()
                self.varCardD.set('Enter Definition')

                self.varCardI = StringVar()
                self.varCardI.set('Enter Image Directory')

                self.lstCardsCreate.append([self.varCardT, self.varCardD, self.varCardI])
                self.count += 1

        # Creating the scroll bar by placing the table in a frame in a canvas in a frame
        # Function to configure the canvas
        def CanvasConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=490, height=600)

        # Creating the top frame for the scroll bar and placing it in the grid.
        self.fmeSbTop = Frame(self.fmePage2CreateSet)
        self.fmeSbTop.grid(row=3, column=1, rowspan=self.varTableRowSpan, columnspan=3)
        # Creating a canvas top put in the top frame, setting it's size and placing it in the frame
        self.canvas = Canvas(self.fmeSbTop)
        # Creating the sub frame for the scroll bar and setting it's size.
        self.fmeSbSub = Frame(self.canvas, width=100, height=600)
        # Creating the scrollbar and making it vertical
        self.ScrollBar = Scrollbar(self.fmeSbTop, orient='vertical', command=self.canvas.yview)
        # Adding the scroll bar to the canvas
        self.canvas.configure(yscrollcommand=self.ScrollBar.set)
        self.ScrollBar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        # Setting the sub frame inside the frame
        self.canvas.create_window((0, 0), window=self.fmeSbSub, anchor='nw')
        self.fmeSbSub.bind('<Configure>', CanvasConfig)

        # Creating the frame to store the table in as a sub frame of the scroll bar sub frame (that's a sub, sub frame)
        #   this is done as the scroll bar was implemented after the creation of the function and the frame was already established.
        self.fmeTableCreate = Frame(self.fmeSbSub)
        # Placing the grid in the frame
        self.fmeTableCreate.grid(row=3, column=1, rowspan=self.varTableRowSpan, columnspan=3)

        # Creating the label for the header for the term column of the table, setting the font and size, placing it in the grid
        self.lblTermHeader = Label(self.fmeTableCreate, text='Term', width=12, height=1)
        self.lblTermHeader.config(font=('Times', 18, 'underline'))
        self.lblTermHeader.grid(row=1, column=1)

        # Creating the label for the header for the definition column of the table, setting the font and size, placing it in the grid
        self.lblDefHeader = Label(self.fmeTableCreate, text='Definition', width=22, height=1)
        self.lblDefHeader.config(font=('Times', 18, 'underline'))
        self.lblDefHeader.grid(row=1, column=3)

        # Creating the label for the header for the image directory column of the table, setting the font and size, placing it in the grid
        self.lblImgHeader = Label(self.fmeTableCreate, text='Image Directory', width=12, height=1)
        self.lblImgHeader.config(font=('Times', 17, 'underline'))
        self.lblImgHeader.grid(row=1, column=5)

        # Creating the entry fields in the table

        self.count = 0
        # Loop that iterates through every row in the table
        for i in range(2, self.varTableRowSpan):
            # Creating a sub list to make adding to the above list easier
            self.lstCardsSub = []
            if (i % 2) == 1:
                # Setting the content for the 'Term' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.varCurrentTerm = StringVar()
                self.varCurrentTerm.set(self.lstCardsCreate[self.count][0].get())
                # Creating an entry field, setting the font, placing in the grid
                self.entTerm = Entry(self.fmeTableCreate, textvariable=self.varCurrentTerm, width=12)
                # Adding the text to the sub list in a StringVar format
                self.lstCardsSub.append(self.varCurrentTerm)
                self.entTerm.config(font=('Times', 16))
                self.entTerm.grid(row=i, column=1)

                # Setting the content for the 'Definition' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.varCurrentDef = StringVar()
                self.varCurrentDef.set(self.lstCardsCreate[self.count][1].get())
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.entDef = Entry(self.fmeTableCreate, textvariable=self.varCurrentDef, width=22)
                # Adding the text to the sub list in a StringVar format
                self.lstCardsSub.append(self.varCurrentDef)
                self.entDef.config(font=('Times', 16))
                self.entDef.grid(row=i, column=3)

                # Setting the content for the 'Image' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.varCurrentImg = StringVar()
                self.varCurrentImg.set(self.lstCardsCreate[self.count][2].get())
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.entImg = Entry(self.fmeTableCreate, textvariable=self.varCurrentImg, width=12)
                # Adding the text to the sub list in a StringVar format
                self.lstCardsSub.append(self.varCurrentImg)
                self.entImg.config(font=('Times', 16))
                self.entImg.grid(row=i, column=5)

                # Adding the sublist to the new list
                #self.lstCardsCreate.append(self.LstCardsSub)
                self.lstCardsCreate[self.count] = ([self.varCurrentTerm, self.varCurrentDef, self.varCurrentImg])

                self.count += 1

        # Setting border around the table
        # The label contains no text and is uses a standard colour.
        # The size depends on where the border label is
        # Creating a list to store the cells that have a border label
        self.border = []
        # Loop that iterates for the amount of rows
        for i in range(0, self.varTableRowSpan):
            # Loop that iterates through every column (there are always seven columns)
            for j in range(0, 7):
                # On even rows and even columns place a label
                if (i % 2) == 0 and (j % 2) == 0:
                    self.lblBorder = Label(self.fmeTableCreate, width=1, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the first column place a label of the same width as the term labels
                elif (i % 2) == 0 and j == 1:
                    self.lblBorder = Label(self.fmeTableCreate, width=12, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the third column place a label of the same width as the definition labels
                elif (i % 2) == 0 and j == 3:
                    self.lblBorder = Label(self.fmeTableCreate, width=22, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and the fifth column place a label of the same width as the image directory labels
                elif (i % 2) == 0 and j == 5:
                    self.lblBorder = Label(self.fmeTableCreate, width=12, height=1, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On even rows and odd column and not the first row place a label as high as the text labels
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.lblBorder = Label(self.fmeTableCreate, width=1, height=3, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)
                # On the first row and odd column and place a label as high as the header labels
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.lblBorder = Label(self.fmeTableCreate, width=1, height=2, bg='grey')
                    self.lblBorder.grid(row=i, column=j)
                    self.border.append(self.lblBorder)

    # Function to save the set that has just been made and change the screen back to ViewOverview
    #                                               COMPLETE
    def CreateSave(self):
        # Reading the table list in to a list of lists of strings
        self.lstCardsCreateString = []

        for i in self.lstCardsCreate:
            self.lstNewSub = []
            for j in i:
                x = j.get()
                # If there is a blank space in the table inform the user with a showinfo message box and exit the function
                if x != '':
                    self.lstNewSub.append(x)
                else:
                    messagebox.showinfo('Saving', 'Set could not saved as there was a blank space.')
                    return
            self.lstCardsCreateString.append(self.lstNewSub)

        # Go through each sublist in the string list and add, 'no' as the default View Full/Star value
        for i in self.lstCardsCreateString:
            i.append('no')

        # String list is now is listCards from design and is ready to be merged with CLI

        # Crete the name of the file to be stored in using the format, file_setName
        self.setFile = ('file_' + str(self.entName.get()))

        # Write the set to a file using SaveSet function in FunctionsCLI
        # self.EntName.get() is the string from the entry field on the page.
        SaveSet(self.entName.get(), self.setFile, self.lstCardsCreateString)

        self.currentSetName.set(self.entName.get())
        self.currentSetFile.set(self.setFile)

        # Adding the set to listSetName and informing the user with a showinfo messagebox
        listSetName.append([self.entName.get(), self.setFile])
        messagebox.showinfo('Saving', 'Set Saved Successfully.')

        # Removing the frame containing everything from the create page
        self.fmePage2CreateSet.grid_remove()
        # Returning to the ViewOverview Screen
        self.ViewOverviewPage(self.master)

    # Function to change the amount of rows in the table      COMPLETE
    # numRow argument is the amount of rows in the table
    # change argument is if the function needs to add a row or remove a row
    def CreateChangeRow(self, numRow, change):
        # Does so by incrementing the variable by +2 (+2 because there needs to be a border row)
        # If the function ran from the 'Add Row' Button, increase the row variable
        if change == 0:
            numRow += 2

            # Adding another card to the list to show on the table and prevent an indexing logic error
            # This is done here as the step is unnecessary when removing a card
            self.varTerm = StringVar()
            self.varTerm.set('Enter Term')
            self.varDef = StringVar()
            self.varDef.set('Enter Definition')
            self.varImg = StringVar()
            self.varImg.set('Enter Image Directory')
            self.lstCardsCreate.append([self.varTerm, self.varDef, self.varImg])
        # If the function ran from the 'Remove Row' Button, decrease the row variable
        elif change == 1:
            numRow -= 2
            # Adding a check that exits the function if the user wants to have less than 4 rows
            if numRow <= 10:
                messagebox.showinfo('Row Limit Reached', 'This is the minimum amount of rows. '
                                                         'You can not remove any more.', icon='warning')
                return

        # Reading the table to a make a of strings
        self.lstCardsString = []
        for i in self.lstCardsCreate:
            self.lstCardsString.append([i[0].get(), i[1].get(), i[2].get()])

        # Recreating self.lstCards using the list of strings created above
        self.lstCardsCreateTemp = []
        for i in self.lstCardsString:
            self.varTerm = StringVar()
            self.varTerm.set(i[0])
            self.varDef = StringVar()
            self.varDef.set(i[1])
            self.varImg = StringVar()
            self.varImg.set(i[2])
            self.lstCardsCreateTemp.append([self.varTerm, self.varDef, self.varImg])
        self.lstCards = self.lstCardsCreateTemp

        # Making sure the row number variable is an integer
        numRow = int(numRow)
        # Setting the self variable to the variable that was changed inside the function
        self.varTableRowSpan = numRow
        # Recalling the table creation function
        self.CreateTable()

    # Function to delete the set being made         COMPLETE
    # Button reads 'Cancel Set Creation'
    def CreateDelete(self):
        # Create a variable to store the text that will be shown in the user notification to make the next line easier to read
        self.message = 'Are you sure you want to cancel set creation?\nThis will return you to the Start-up screen and ' \
                       'progress will be lost.\nThis can not be undone.'
        # Message box asking for confirmation
        self.varContinue = messagebox.askokcancel(title='Cancel', message=self.message)
        # If the user confirms their choice
        if self.varContinue:
            # Remove the Create Page and Call the ViewOverview Page Function
            self.fmePage2CreateSet.grid_remove()
            self.ViewOverviewPage(self.master)
            return

    # Function to import a set                      COMPLETE
    # Has a sub window and a function for the functionality which calls a function in FunctionsCLI
    def CreateImport(self):

        # Variable to run the while loop, is made false at the end. Done to make it easier to condense the program
        self.ImportPageContents = True
        # While loop contains the code to create and place the widgets in the sub window
        while self.ImportPageContents:
            # Define, create and name a sub window
            self.winImport = Toplevel(root)
            self.winImport.title('Import')

            # Create a frame to place everything in. Place the frame in the sub window
            self.fmeImportPage = Frame(self.winImport)
            self.fmeImportPage.grid()

            # Create a title lable, setting the colour size and font, place in grid
            self.lblImTitle = Label(self.fmeImportPage, text='Import Set', bg='#7AEDFB', width=30, height=1)
            self.lblImTitle.config(font=('Arail', 28, 'underline'))
            self.lblImTitle.grid(row=0, column=0, rowspan=1, columnspan=2)

            # Create the label to accompany the entry field that gets the name of the set to be imported
            self.lblImSetName = Label(self.fmeImportPage, text='Name of Set:')
            # Set the font for the label and place in the grid
            self.lblImSetName.config(font=('Times', 16))
            self.lblImSetName.grid(row=1, column=0, rowspan=1, columnspan=1)

            # Define variable to store the input from the entry field as a StringVar
            self.varImSetName = StringVar()
            # Provide a default value into the entry field to act as an existence check and an instruction
            self.varImSetName.set('Enter Name Here')
            # Create the entry field to get the name of the set being imported, set the font, place in the grid
            self.entImSetName = Entry(self.fmeImportPage, textvariable=self.varImSetName, width=20)
            self.entImSetName.config(font=('Times', 16))
            self.entImSetName.grid(row=1, column=1, rowspan=1, columnspan=1)

            # Create a label to accompany the entry field that gets the file directory, set the font and place in the grid
            self.lblImPrompt = Label(self.fmeImportPage, text='Directory of Import File:')
            self.lblImPrompt.config(font=('Times', 16))
            self.lblImPrompt.grid(row=2, column=0, rowspan=1, columnspan=1)

            # Define a variable as a StringVar to store the input from the entry
            self.varImDirectory = StringVar()
            # Provide a default value into the entry field to act as an existence check
            self.varImDirectory.set('Enter Directory Here')
            # Create the entry field to get the directory of the file to be imported, set the font and place in the grid
            self.entImDir = Entry(self.fmeImportPage, textvariable=self.varImDirectory, width=20)
            self.entImDir.config(font=('Times', 16))
            self.entImDir.grid(row=2, column=1, rowspan=1, columnspan=1)

            # Create a button to call the sub function of this function that imports the set. Set the font, place in grid
            # Command calls the sub function
            # The self.VarImDirectory.get() argument is the string of the directory entered into the entry
            # The self.varImSetName.get() argument is the string of the name entered into the entry
            self.btnImImport = Button(self.fmeImportPage, text='Import File', width=40,
                                      command=lambda *args: ImImport(self, self.varImDirectory.get(),
                                                                     self.varImSetName.get()))
            self.btnImImport.config(font=('Times', 16))
            self.btnImImport.grid(row=3, column=0, rowspan=1, columnspan=2)

            # Define a StringVar to store a short set of instructions
            # Instructions are stored here instead of the widget creation line for readability of the code
            self.varImTxt = StringVar()
            self.varImTxt.set('Imported sets must be a CSV (Comma Separated Value) file in the following form;\n'
                              'term,definition,img_directory\nterm,definition,img_directory\n... , ... , ...\nWhere each line '
                              'represents a different card.\nExample Directory: /Users/19ecornish/Downloads/set.csv\nAfter a '
                              'successful import you will be returned to the start-up screen.')
            # Create a label to provide some basic instructions. Set the font and place in the grid
            self.lblImTxt = Label(self.fmeImportPage, textvariable=self.varImTxt, anchor=NW)
            self.lblImTxt.config(font=('Times', 16))
            self.lblImTxt.grid(row=4, column=0, rowspan=1, columnspan=2)

            # Create a button to exit the importing and close the sub window, set the font and place in the grid
            # Command destroy's the sub window which consequentially exits the function
            self.btnImExit = Button(self.fmeImportPage, text='Cancel Import', command=self.winImport.destroy)
            self.btnImExit.config(font=('Times', 16))
            self.btnImExit.grid(row=5, column=1, rowspan=1, columnspan=1)

            # Create a blank label of set size to assist in the positioning of the exit button
            self.lblBlank = Label(self.fmeImportPage, width=14, height=1)
            self.lblBlank.grid(row=5, column=0, rowspan=1, columnspan=1)

            # Set the while loop variable to false so that the while loop only runs once
            self.ImportPageContents = False

        # Function to import the set using input gathered in the while loop.
        # directory argument is the directory gathered from the entry
        # setName argument is the name from the entry
        # Both arguments are strings
        def ImImport(self, directory, setName):
            # Create the name of the file for the set using the format used when creating a set
            setFile = ('file_' + str(setName))

            # Call the ImportSet function from FunctionsCLI which reads the given file and writes it to a file made
            #       by the program
            # listSetName argument is listSetName from the design
            # directory and setName arguments is the same as the argument from this function
            # setFile argument is the variable that was just created and is a string
            # Function returns a boolean value. If true the file was read successfully
            #       If false then there was an error reading the file
            self.check = ImportSet(directory, setName, setFile)
            # If the import was successful
            if self.check:
                # Add the set to listSetName
                listSetName.append([setName, setFile])
                # Inform the user that the import was successful with a messagebox
                messagebox.showinfo('Import', 'Import Successful\nReturning to start-up screen')

                # Close the sub window
                self.winImport.destroy()
                # Removing the frame containing everything from the create page
                self.fmePage2CreateSet.grid_remove()
                # Returning to the ViewOverview Screen
                self.ViewOverviewPage(self.master, self.currentSetName.get(), self.currentSetFile.get())
            # If the import was not successful
            elif not self.check:
                # Inform the user and provide some quick suggestions on what to check
                messagebox.showinfo('Import',
                                    'Import Unsuccessful\nCheck the directory, file type and the import format.')
                # Exit the function
                return

    # Function for the View Page                    PAGE FUNCTION
    def ViewPage(self, master, number):

        # Removing the frame containing ViewOverviewPage
        self.fmePage1ViewOverview.grid_remove()
        # Creating the frame to store the contents of Create Page
        self.fmePage3View = Frame(master)
        self.fmePage3View.grid()

        # Checks if there are more cards
        if number < len(self.lstCards):
            # If the user selected view all or view Fav AND the current card is a favourite
            if self.varViewFullStarInput.get() == 1 or self.varViewFullStarInput.get() == 2 and self.lstCards[number]\
                  [3].get() == 'yes':

                # Widget 1
                self.lblName = Label(self.fmePage3View, textvariable=self.currentSetName, width=23, bg='#7AEDFB')
                self.lblName.config(font=('Arail', 32, 'bold underline'))
                self.lblName.grid(row=0, column=0, rowspan=1, columnspan=5)

                # Widget 2
                self.fmeDisplay = Frame(self.fmePage3View)
                self.fmeDisplay.grid(row=2, column=1, rowspan=9, columnspan=5)

                # Can show text 8 lines high and 30 characters wide

                # Defining a label to show the term of the card
                self.varCardShowTerm = StringVar()
                self.varCardShowTerm.set(self.lstCards[number].varTerm)
                self.lblCardTerm = Label(self.fmeDisplay, height=8, width=30, textvariable=self.varCardShowTerm)
                self.lblCardTerm.config(
                    font=('Times', 32))  # If the default side is set to term show the definition for the first card

                # Defining a label to show the def of the card
                self.varCardShowDef = StringVar()
                self.varCardShowDef.set(self.lstCards[number].varDef)
                self.lblCardDef = Label(self.fmeDisplay, height=8, width=30, textvariable=self.varCardShowDef)
                self.lblCardDef.config(font=('Times', 32))

                # Defining a label to show the image of the card
                try:
                    self.ImgDirectory = StringVar()
                    self.ImgDirectory.set(self.lstCards[number].varImg)
                    # Opening the image file
                    self.ImgTemp = Image.open(self.ImgDirectory.get())
                    # Resizing the image
                    self.ImgTemp = self.ImgTemp.resize((367, 275), Image.ANTIALIAS)  # (width,height)
                    # Saving the image to a file in a format recognised by tkinter
                    self.ImgTemp.save('ImageTempFile.gif', 'gif')
                    # Opening the image file as a PhotoImage object
                    self.ImgObj = PhotoImage(file='ImageTempFile.gif')
                    # Placing the image object in a label
                    self.lblCardImg = Label(self.fmeDisplay, image=self.ImgObj)
                    # Setting the image method of the label to the image object
                    self.lblCardImg.image = self.ImgObj
                except (FileExistsError, FileNotFoundError, IsADirectoryError, NotADirectoryError):
                    messagebox.showinfo('File Error', 'Directory for this image is invalid.', icon='warning')
                    self.ViewBack()

                # Depending on what the default side is, place the correct label defined above on the grid
                if self.varDefaultSideInput.get() == 1:
                    self.lblCardTerm.grid(row=1, column=1)
                # If the default side is set to deinition show the definition for the first card
                elif self.varDefaultSideInput.get() == 2:
                    self.lblCardDef.grid(row=1, column=1)
                # If the default side is set to image show the image for the first card
                elif self.varDefaultSideInput.get() == 3:
                    self.lblCardImg.grid(row=1, column=1)

                # Border around content
                self.lblBorder1 = Label(self.fmeDisplay, height=2, width=4, bg='grey')
                self.lblBorder1.config(font=('Times', 16))
                self.lblBorder1.grid(row=0, column=0)
                self.lblBorder2 = Label(self.fmeDisplay, height=2, width=60, bg='grey')
                self.lblBorder2.config(font=('Times', 16))
                self.lblBorder2.grid(row=0, column=1)
                self.lblBorder3 = Label(self.fmeDisplay, height=2, width=4, bg='grey')
                self.lblBorder3.config(font=('Times', 16))
                self.lblBorder3.grid(row=0, column=2)
                self.lblBorder4 = Label(self.fmeDisplay, height=16, width=4, bg='grey')
                self.lblBorder4.config(font=('Times', 16))
                self.lblBorder4.grid(row=1, column=0)
                self.lblBorder5 = Label(self.fmeDisplay, height=16, width=4, bg='grey')
                self.lblBorder5.config(font=('Times', 16))
                self.lblBorder5.grid(row=1, column=2)
                self.lblBorder6 = Label(self.fmeDisplay, height=2, width=4, bg='grey')
                self.lblBorder6.config(font=('Times', 16))
                self.lblBorder6.grid(row=2, column=0)
                self.lblBorder7 = Label(self.fmeDisplay, height=2, width=60, bg='grey')
                self.lblBorder7.config(font=('Times', 16))
                self.lblBorder7.grid(row=2, column=1)
                self.lblBorder8 = Label(self.fmeDisplay, height=2, width=4, bg='grey')
                self.lblBorder8.config(font=('Times', 16))
                self.lblBorder8.grid(row=2, column=2)

                # Widget 3
                self.btnBack = Button(self.fmePage3View, text='Back', width=24, command=self.ViewBack)
                self.btnBack.config(font=('Times', 16))
                self.btnBack.grid(row=0, column=5, rowspan=1, columnspan=3)

                # Widget 4
                self.lblProgressLabel = Label(self.fmePage3View, text='Progress:', width=12)
                self.lblProgressLabel.config(font=('Times', 16))
                self.lblProgressLabel.grid(row=2, column=7, rowspan=1, columnspan=1)

                # Widget 5                              WIP May need function to account for viewing option
                self.varProgress = StringVar()
                if self.varCardOrderInput.get() == 1:
                    self.varProgress.set('{0}/{1}'.format((number + 1), len(self.lstCards)))
                elif self.varCardOrderInput.get() == 2:
                    self.varProgress.set('{0}/{1}'.format(len(self.shownCards) + 1 - self.cycles, len(self.lstCards)))
                self.lblProgressResults = Label(self.fmePage3View, textvariable=self.varProgress, width=12, anchor='e')
                self.lblProgressResults.config(font=('Times', 16))
                self.lblProgressResults.grid(row=3, column=7, rowspan=1, columnspan=1)

                # Widget 6
                self.varStarUnstarText = StringVar()
                if self.lstCards[number].varIsStar == 'no':
                    self.varStarUnstarText.set('Star')
                elif self.lstCards[number].varIsStar == 'yes':
                    self.varStarUnstarText.set('Unstar')
                self.btnStarUnstar = Button(self.fmePage3View, textvariable=self.varStarUnstarText, width=12,
                                            command=lambda *args: self.ViewStarUnstar(number))
                self.btnStarUnstar.config(font=('Times', 16))
                self.btnStarUnstar.grid(row=6, column=7, rowspan=1, columnspan=1)

                # Widget 7
                self.btnHelp = Button(self.fmePage3View, text='Help', width=12, command=self.HelpPage)
                self.btnHelp.config(font=('Times', 16))
                self.btnHelp.grid(row=9, column=7, rowspan=1, columnspan=1)

                # Widget 8
                self.btnPrevious = Button(self.fmePage3View, text='Previous', width=8,
                                          command=lambda *args: self.ViewPrevious(master, number))
                self.btnPrevious.config(font=('Times', 16))
                self.btnPrevious.grid(row=11, column=1, rowspan=1, columnspan=1)

                # Widget 9
                self.btnTerm = Button(self.fmePage3View, text='Term', width=8, command=self.ViewTerm)
                self.btnTerm.config(font=('Times', 16))
                self.btnTerm.grid(row=11, column=2, rowspan=1, columnspan=1)

                # Widget 10
                self.btnImage = Button(self.fmePage3View, text='Image', width=8, command=self.ViewImage)
                self.btnImage.config(font=('Times', 16))
                self.btnImage.grid(row=11, column=3, rowspan=1, columnspan=1)

                # Widget 11
                self.btnDef = Button(self.fmePage3View, text='Definition', width=8, command=self.ViewDef)
                self.btnDef.config(font=('Times', 16))
                self.btnDef.grid(row=11, column=4, rowspan=1, columnspan=1)

                # Widget 12
                self.btnNext = Button(self.fmePage3View, text='Next', width=8,
                                      command=lambda *args: self.ViewNext(master, number))
                self.btnNext.config(font=('Times', 16))
                self.btnNext.grid(row=11, column=5, rowspan=1, columnspan=1)

                # Blank Spaces
                blanks = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 12], [1, 12], [1, 12], [1, 12], [1, 12],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                          [1, 4, 5, 7, 8, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
                self.countBlank = 0
                while self.countBlank < 9:
                    for i in blanks[self.countBlank]:
                        self.lblBlank = Label(self.fmePage3View, height=1, width=8)  # , bg='green', text='abc')
                        self.lblBlank.config(font=('Arial', 10))
                        self.lblBlank.grid(row=i, column=self.countBlank)
                    self.countBlank += 1

            # If view full fav is set the fav and the current card is not a favourite then skip to the next card
            else:
                number += 1
                self.ViewPage(master, number)

        # If there are no more cards inform the user and exit view page.
        else:
            messagebox.showinfo('Finished', 'All cards have been shown\nReturning to start-up screen.')
            self.ViewBack()

    # Function to go back to ViewOverview Page      COMPLETE
    def ViewBack(self):
        print('ViewBack Function Ran')
        # Rewriting self.lstCards as a list of strings
        self.lstCardsStrings = []
        for i in self.lstCards:
            self.lstCardsStringsSub = []
            self.lstCardsStringsSub.append(i.varTerm)
            self.lstCardsStringsSub.append(i.varDef)
            self.lstCardsStringsSub.append(i.varImg)
            self.lstCardsStringsSub.append(i.varIsStar)
            self.lstCardsStrings.append(self.lstCardsStringsSub)

        # Rewriting listCards
        SaveSet(self.currentSetName.get(), self.currentSetFile.get(), self.lstCardsStrings)

        self.fmePage3View.grid_remove()
        self.ViewOverviewPage(self.master)
        return

    # Function to Star/Unstar a card                COMPLETE
    def ViewStarUnstar(self, number):
        # If the card is not starred
        if self.lstCards[number].varIsStar == 'no':
            # Star the card
            self.lstCards[number].varIsStar = 'yes'
            # Inform the user
            messagebox.showinfo('Star and Unstar', ' The card has been starred.')
            # Change the button to read 'Unstar'
            self.varStarUnstarText.varIsStar = 'Unstar'
        # If the card is starred
        elif self.lstCards[number].varIsStar == 'yes':
            # Unstar the card
            self.lstCards[number].varIsStar = 'no'
            # Inform the user
            messagebox.showinfo('Star and Unstar', ' The card has been un-starred.')
            # Change the button to read 'Star'
            self.varStarUnstarText.set('Star')

    # Function to go to the previous card           COMPLETE
    def ViewPrevious(self, master, number):
        if self.varCardOrderInput.get() == 1:
            # Decreases the card counter by one
            number -= 1

            # If  viewFullStar is set to star the change back cards until a starred card is reached or there are no more cards
            if self.varViewFullStarInput.get() == 2:
                while self.lstCards[number].varIsStar == 'no':
                    number -= 1
            # If there are no more cards then inform the user
            if number < 0:
                messagebox.showinfo('No More Cards', 'There are no previous cards to go back to.')
                return
        elif self.varCardOrderInput.get() == 2:
            # If only one card has been shown then the previous card is the first card
            if len(self.shownCards) == 1:
                x = self.shownCards[0]
            else:
                # Reverses the list of the shown cards into a new list using function from FunctionsCLI
                self.shownCardsReversed = self.shownCards.copy()
                self.shownCardsReversed.reverse()

                try:
                    x = self.shownCardsReversed[self.cycles]
                    number = x
                except IndexError:
                    # If the first card shown is the current card then the current card is the number
                    # of cards in the list which triggers an exit out of the function
                    number = len(self.lstCards)

                self.cycles += 1

        # Re-run the view window with the new card
        self.fmePage3View.grid_remove()
        self.ViewPage(master, number)

    # Function to show the term                    COMPLETE
    def ViewTerm(self):
        # Remove the currently shown definition or image
        # Try blocks are to catch the error that ocurs if the card is not showing the definition or the image
        try:
            self.lblCardDef.grid_remove()
        except AttributeError:
            print('self.lblCardDef: Attribute Error')
        try:
            self.lblCardImg.grid_remove()
        except AttributeError:
            print('self.lblCardImg: Attribute Error')
        # Place the term label in the grid
        self.lblCardTerm.grid(row=1, column=1)

    # Function to show the image                   COMPLETE
    def ViewImage(self):
        # Remove the currently shown term or definition
        # Try blocks are to catch the error that ocurs if the card is not showing the term or the definition
        try:
            self.lblCardTerm.grid_remove()
        except AttributeError:
            print('self.lblCardTerm: Attribute Error')
        try:
            self.lblCardDef.grid_remove()
        except AttributeError:
            print('self.lblCardDef: Attribute Error')
        # Place the image label in the grid
        self.lblCardImg.grid(row=1, column=1)

    # Function to show the definition              COMPLETE
    def ViewDef(self):
        # Remove the currently shown term or image
        # Try blocks are to catch the error that ocurs if the card is not showing the term or the image
        try:
            self.lblCardTerm.grid_remove()
        except AttributeError:
            print('self.lblCardTerm: Attribute Error')
        try:
            self.lblCardImg.grid_remove()
        except AttributeError:
            print('self.lblCardImg: Attribute Error')
        # Place the definition label in the grid
        self.lblCardDef.grid(row=1, column=1)

    # Function to go to the next card               COMPLETE
    def ViewNext(self, master, number):
        # If the card order is set to Original
        if self.varCardOrderInput.get() == 1:
            # Continue to the next card
            number += 1
        elif self.varCardOrderInput.get() == 2:
            # Rewriting self.lstCards as a list of strings
            self.lstCardsStrings = []
            for i in self.lstCards:
                self.lstCardsStringsSub = []
                self.lstCardsStringsSub.append(i[0].get())
                self.lstCardsStringsSub.append(i[1].get())
                self.lstCardsStringsSub.append(i[2].get())
                self.lstCardsStringsSub.append(i[3].get())
                self.lstCardsStrings.append(self.lstCardsStringsSub)
            # Calling RndCardOrder function from FunctionsCLI to change to the next card in a randomised order
            number = RndCardOrder(number, self.lstCardsStrings, self.shownCards)
        # Remove the frame and rerun the Page function
        self.fmePage3View.grid_remove()
        self.ViewPage(master, number)

    # Function for the Help Page which has a sub window         Needs Text
    # The widgets in the sub window are created in the while loop and the text is determined using the sub function
    def HelpPage(self):
        # While loop with variable to make the program easier to condense and therefore improve readability
        self.HelpPageContents = True
        while self.HelpPageContents:
            # Creating the sub window with title
            self.winHelp = Toplevel(root)
            self.winHelp.title('Help')

            # Creating a frame to contain all of the widgets and placing it in the grid
            self.fmeHelpPage = Frame(self.winHelp)
            self.fmeHelpPage.grid()

            # Creating a title widget, setting the size, colour and font and, placing it in the grid
            self.lblHpTitle = Label(self.fmeHelpPage, text='Help', bg='#7AEDFB', width=35, height=1)
            self.lblHpTitle.config(font=('Arail', 52, 'bold underline'))
            self.lblHpTitle.grid(row=0, column=0, rowspan=1, columnspan=9)

            # Creating a label to provide some short instructions on using the sub window, setting the font and placing it in the grid
            self.lblHpInstructions = Label(self.fmeHelpPage, text='Select the Button which'
                                                                  ' corresponds to the area you need help with.')
            self.lblHpInstructions.config(font=('Times', 18))
            self.lblHpInstructions.grid(row=1, column=0, columnspan=9)

            # Creating buttons to show different text for different area's of the program.
            # Buttons all call the same command, integer argument tells the function which button was pressed and therefore which set of text to display

            # Button for program navigation
            self.btnHp1Navigation = Button(self.fmeHelpPage, text='General Use', width=10,
                                           command=lambda *args: HpText(self, 1))
            self.btnHp1Navigation.config(font=('Times', 16))
            self.btnHp1Navigation.grid(row=2, column=0, rowspan=1, columnspan=1)

            # Button for creating sets
            self.btnHp2Creating = Button(self.fmeHelpPage, text='Creating Sets', command=lambda *args: HpText(self, 2))
            self.btnHp2Creating.config(font=('Times', 16))
            self.btnHp2Creating.grid(row=2, column=1)

            # Button for Editing Sets
            self.btnHp3Editing = Button(self.fmeHelpPage, text='Editing Sets', command=lambda *args: HpText(self, 3))
            self.btnHp3Editing.config(font=('Times', 16))
            self.btnHp3Editing.grid(row=2, column=2)

            # Button for Selecting Sets
            self.btnHp4Select = Button(self.fmeHelpPage, text='Selecting Different Sets',
                                       command=lambda *args: HpText(self, 4))
            self.btnHp4Select.config(font=('Times', 16))
            self.btnHp4Select.grid(row=2, column=3)

            # Button for Viewing an Overview of Sets
            self.btnHp5ViewOverview = Button(self.fmeHelpPage, text='Viewing an Overview of a Set',
                                             command=lambda *args: HpText(self, 5))
            self.btnHp5ViewOverview.config(font=('Times', 16))
            self.btnHp5ViewOverview.grid(row=2, column=4)

            # Button for viewing sets
            self.btnHp6Viewing = Button(self.fmeHelpPage, text='Viewing Sets', command=lambda *args: HpText(self, 6))
            self.btnHp6Viewing.config(font=('Times', 16))
            self.btnHp6Viewing.grid(row=2, column=5)

            # Button for deleting sets
            self.btnHp7DeletingSets = Button(self.fmeHelpPage, text='Deleting Sets',
                                             command=lambda *args: HpText(self, 7))
            self.btnHp7DeletingSets.config(font=('Times', 16))
            self.btnHp7DeletingSets.grid(row=2, column=6)

            # Button for Importing Sets
            self.btnHp8Import = Button(self.fmeHelpPage, text='Importing Sets', command=lambda *args: HpText(self, 8))
            self.btnHp8Import.config(font=('Times', 16))
            self.btnHp8Import.grid(row=2, column=7)

            # Button for exiting the help screed
            # Command closes the sub window which ends the function
            self.btnHp9ExitHelp = Button(self.fmeHelpPage, text='Exit Help', command=self.winHelp.destroy)
            self.btnHp9ExitHelp.config(font=('Times', 16))
            self.btnHp9ExitHelp.grid(row=2, column=8)

            # Creating a StringVar which will store the instructions being shown.
            # Variable will be updated using sub function
            self.varHpText = StringVar()
            # By default setting it to many blank lines
            self.varHpText.set('\n\n\n\n\n\n\n\n\n\n')

            # Placing the text in a label with a set width and height, setting the font and placing it in the grid
            self.lblHpText = Label(self.fmeHelpPage, textvariable=self.varHpText, width=155, height=12, anchor=NW,
                                   justify=LEFT)
            self.lblHpText.config(font=('Times', 16))
            self.lblHpText.grid(row=3, column=0, rowspan=10, columnspan=9)

            # Setting the while loop variable to False and therefore ending the while loop after one iteration
            self.HelpPageContents = False

        # Sub function to change the text displayed
        # input argument determines the text being shown
        def HpText(self, input):
            # Creating a string variable to contain the text that will be used to set the StringVar
            text = self.varHpText.get()
            # Ensuring that the input argument is an integer to prevent a TypeError or a ValueError
            input = int(input)
            # If, elif control structure that takes the given number and sets text to the correct string.
            if input == 1:
                text = (
                    'General Use\nThe program has three main pages, View Overview, Create and View.\nThe View Overview '
                    'page shows all of the cards in the set on a table.\nThe Create page allows you to create a new '
                    'set.\nThe View page shows each card one at a time in a sequance.\nThe View Overview page is shown '
                    'by default and is the start-up page. The Create Page can be reached with the Create Set button.\n'
                    'The Create Page can be closed using the Save Set button or the Cancel Set Creation button.\nThe '
                    'View page can be reached from the View Overview page with the View Set button and can be exited '
                    'using the Back button.\n\n')
            elif input == 2:
                text = (
                    'Creating sets\nTo enter the create set page select the Create Set button on the start-up page.\n'
                    'The name of the set you are creating can be set by typing into the title on the top list of your '
                    'screen.\nCards can be added using the table. Each row is a card and the cells are editable. '
                    '(except the headers).\nIf nothing is entered then the default text will become part of the set.\n'
                    'To enter an image type in its directory. Example: /Users/19ecornish/Desktop/image_5024.png   '
                    'Images can be in any standard format. Including .jpg, .png, .jpeg, .gif (only stills)\nTo add or '
                    'remove a row press the corresponding button. The table will regenerate but anything entered will '
                    'remain. The rows will be added and removed from the end.\nHowever rows with your infomation can be '
                    'cleared.\nWhen you are finished select Save Set to save your new set and return to the View Overview'
                    ' screen. If there are any blank spaces you will not be able to save.\nIf you wish to return to '
                    'the View Overview page without saving select the Cancel Set Creation button. You will need to '
                    'confirm this action.\nIf you want to import a set select the Import Set button. This will bring '
                    'up a new window. For instructions on importing sets select the button.\n')
            elif input == 3:
                text = (
                    'Editing Sets\nSets can be edited from the start-up screen. To begin editing select the Edit Set '
                    'button.\nThis will turn the table into an editable version. Each cell can be changed.\nHowever '
                    'the name of the set can not be changed and the amount of cards can not be changed.\nTo save any '
                    'changes reselect the Edit Set button which will not read Save Changes.\nIf there are any blank '
                    'spaces you will not be able to save.\nWARNING if you enter another page by selecting Create Set '
                    'or View Set your changes will not be save and may be lost permanently.\nChanges can also be lost '
                    'if you change to a different set.\n\n\n\n')
            elif input == 4:
                text = (
                    'Selecting Sets\nTo select a different set first enter the name of the set you wish to select in '
                    'the entry field.\nThe entry field is Case, Space and Character Sensitive. Anything other than the'
                    ' exact name will not be recignised.\nAfter entering the exact name of the set select the Select S'
                    'et button.\nThe program will then attempt to change the set. If the name was correct then the table'
                    ' and the title will change.\nIf the name is incorrect then the program will inform you and you may'
                    ' try again.\n\n\n\n\n\n')
            elif input == 5:
                text = (
                    'Viewing an Overview of Sets.\nThe first screen shown when the program is opened shows an overview '
                    'of the last created set.\nThe set is shown in a table. The name of the set can also be seen in the'
                    ' top left hand corner of the page.\nFor instructions on how to edit the set select the Editing Sets '
                    'button.\nFor instructions on how to change the set select the Selecting Sets button.\nFor instruc'
                    'tions on how to change the current page select the General Use button.\nOn the right hand side of'
                    'the view overview screen are three sets of radio buttons with a label fro each set.\nThe radio '
                    'buttons set options that change how a set is viewed.\nThe options are detailed in the Viewing Se'
                    'ts instructions.\n\n\n')
            elif input == 6:
                text = (
                    'Viewing Sets\nSets can be viewed in a standard one card, one side at a time manner in the View S'
                    'et Page. For information on navigating between pages select the General Use Button.\nBefore view'
                    'ing a set select your viewing options. There are three viewing options that are set with the rad'
                    'io buttons on the View Overview page.\nDefault Side determines if you want to the the term, defi'
                    'nition or image for each card first. View determines if you want to see every card or just those'
                    ' that you have marked as starred.\nCard Order determines if the cards will be shown in the order '
                    'that they were created and appear on the table or in a randomised order.\nWhen in the view page the name of the set can be '
                    'seen on the top right. The progresss label and number on the right show how far through the set y'
                    'ou are.\nThe Star button stars the card so it will show if the View option is set to starred car'
                    'ds only. If a card is starred then the button reads Unstar.\nTo show the previously viewed card '
                    'select the Previous button.\nTo show the term for the current card select the Term button.\nTo s'
                    'how the image for the currently viewed card select the Image button.\nTo show the definition for'
                    ' the currently viewed card select the Definition button.\nTo show the next card select the Next '
                    'button.')
            elif input == 7:
                text = (
                    'Deleting Sets.\nTo delete a set select the set you want to delete. For instructions of selecting'
                    ' a set select the Selecting Sets button.\nTo delete the currently viewed set select the Delete S'
                    'et button at the bottom of the View Overview page.\nThis will bring up a confirmation screen.\n'
                    'Select yes if you wish to delete the set. This will delete the set instantly and forever.\nThe '
                    'screen will then show the last created set.\n\n\n\n\n\n')
            elif input == 8:
                text = (
                    'Importing Sets.\nTo import a set select the button on the Create page. This will bring up a sub'
                    ' window.\nEnter a name for the set you wish to import into the name entry field.\nEnter the dire'
                    'ctory into the directory entry field. Then select the Import Set button.\nIf the importing was '
                    'successful you will be notified. If the import was unsuccessful then nothing will happen.\nTo '
                    'cancel importing select the Cancel Import button. This will take you back to the Create page.\n'
                    '\nTo ensure a successful importation of a set check for a correct directory, file type and file '
                    'format.\nExample Directory: /Users/19ecornish/Downloads/fileToImport.csv\nThe file MUST be a '
                    '.csv\nThe file must have the following format; term,definition,image newline where each line re'
                    'presents a new card.\n')
            # Setting the StringVar to the changed text variable
            self.varHpText.set(text)
            return


# Creating the root window and setting its size
root = Tk()
root.geometry('1000x800')

# Creating listSetName from the design
listSetName = []
# Reading listSetName file to the list.
# Each line in the file is a set
# The first value is the setName, the second is the fileName
# The try, except block prevents an error if it is the first time running the program and therefor there is no file
try:
    fileListSetName = open('fileListSetName.txt', 'r')
    for line in fileListSetName:
        line = line.strip('\n')
        line = line.split(',')
        listSetName.append(line)
    fileListSetName.close()
except FileNotFoundError:
    listSetName = []

# Setting the current/default set. Takes the last set on the listSetName list and records the setName and fileName
# These variables are converted into StringVars in the GUI
currentSetNameString = listSetName[-1][0]
currentSetFileString = listSetName[-1][1]

lstCards = ListCardsCreate(currentSetFileString)


# Calls the GUI
gui = GUI(root)
# Runs the window
root.mainloop()

# Writes listSetName to the file after the window is closed. This code is important if new sets are created otherwise
#       after the program is closed the program will not be able to access the newly created set.
fileListSetName = open('fileListSetName.txt', 'w')
for set in listSetName:
    fileListSetName.write(set[0])
    fileListSetName.write(',')
    fileListSetName.write(set[1])
    fileListSetName.write('\n')
fileListSetName.close()