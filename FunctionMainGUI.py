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
from FunctionsCLI import ListSetCreate, SaveSet, DeleteSet, SelectSet, ImportSet, RndCardOrder


# The Class that contains all of the GUI component
class GUI:
    # Initialisation Function                       INITIAL FUNCTION
    def __init__(self, master):
        # Defing master and giving the root window a title
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
        self.FmePage1ViewOverview = Frame(master)

        # Creating the setName label, setting the size colour and font, placing it in the grid
        # Text uses the variable that stores the current set name.
        self.LblSet = Label(self.FmePage1ViewOverview, textvariable=self.currentSetName, bg='orange', width=32)
        self.LblSet.config(font=('Arial', 32, 'bold underline'))
        self.LblSet.grid(row=0, column=0, rowspan=1, columnspan=4)


        # Calling the function for the table in ViewOverview
        # listSet is listSet from the design and is created using a function. Initial creation is outside the class
        self.ViewOverviewTable(listSet)

        # Creating the Create Set button, setting the size and font, placing it in the grid
        # The command calls the Create Page Function. Gives the master agrument as the CreatePage function has a new top frame
        self.BtnCreate = Button(self.FmePage1ViewOverview, text='Create Set', width=24, command=lambda *args: self.CreatePage(master))
        self.BtnCreate.config(font=('Times', 16))
        self.BtnCreate.grid(row=0, column=5, rowspan=1, columnspan=3)

        # The integer variable stores the current status of the button and the table.
        # 0 is View Mode,   1 is the Edit Mode
        # The default is 0
        self.varEditSaveBtnInt = IntVar()
        self.varEditSaveBtnInt.set(0)
        # The string variable stores the text for the Button. It is changed in the function
        self.VarEditSaveBtnText = StringVar()
        self.VarEditSaveBtnText.set('Edit Set')
        # Creating the Edit Set function, setting the size and font, placing it in the grid
        # The command calls the associated function
        self.BtnEditSave = Button(self.FmePage1ViewOverview, textvariable=self.VarEditSaveBtnText, width=24,
                                  command=self.ViewOverviewEditSaveBtn)
        self.BtnEditSave.config(font=('Times', 16))
        self.BtnEditSave.grid(row=2, column=5, rowspan=1, columnspan=3)

        # Variable stores the text entered into the entry field, by default it is set to an instruction
        self.VarSelectInput = StringVar()
        self.VarSelectInput.set('Enter the Name of the Set you Wish to Change to then click Select.')
        # Creating the entry field for the select set function, setting the size and font, placing it in the grid
        self.EntSelect = Entry(self.FmePage1ViewOverview, textvariable=self.VarSelectInput, width=20)
        self.EntSelect.config(font=('Times', 12))
        self.EntSelect.grid(row=3, column=5, rowspan=1, columnspan=2)
        # Creating the button for the select set function, setting the font and size, placing it in the grid
        # The command calls the select set function which uses the text from the entry field
        self.BtnSelect = Button(self.FmePage1ViewOverview, text='Select', width=8, command=self.ViewOverviewSelect)
        self.BtnSelect.config(font=('Times', 16))
        self.BtnSelect.grid(row=3, column=7, rowspan=1, columnspan=1)

        # Creating the frame for the viewing options and placing it in the top grid
        self.FmeOptions = Frame(self.FmePage1ViewOverview)
        self.FmeOptions.grid(row=4, column=5, columnspan=3, rowspan=7)

        # Default Side Option

        # Creating the Default Side viewing options label, setting the font and placing it in the grid
        self.LblDefaultSide = Label(self.FmeOptions, text='Default Side:', anchor=W)
        self.LblDefaultSide.config(font=('Times', 16))
        self.LblDefaultSide.grid(row=0, column=0)

        # Defining a variable to store the input for the Default Side radio buttons
        self.VarDefaultSideInput = IntVar()

        # Radio Buttons for default side, setting the font and placing them in the grid.
        self.RbDefaultSideTerm = Radiobutton(self.FmeOptions, text='Term', variable=self.VarDefaultSideInput, value=1, anchor=W, width=8)
        self.RbDefaultSideTerm.config(font=('Times', 14))
        self.RbDefaultSideTerm.grid(row=1, column=0)
        self.RbDefaultSideDef = Radiobutton(self.FmeOptions, text='Definition', variable=self.VarDefaultSideInput, value=2, anchor=W, width=10)
        self.RbDefaultSideDef.config(font=('Times', 14))
        self.RbDefaultSideDef.grid(row=1,column=1)
        self.RbDefaultSideImg = Radiobutton(self.FmeOptions, text='Image', variable=self.VarDefaultSideInput, value=3, anchor=W, width=7)
        self.RbDefaultSideImg.config(font=('Times', 14))
        self.RbDefaultSideImg.grid(row=1,column=2)

        # Setting 'Term' as the default option to act as an existence check by forcing a value
        self.RbDefaultSideTerm.select()

        # View Full/Star Option

        # Creating the Full/Star viewing options label, setting the font and placing it in the grid
        self.LblViewFullStar = Label(self.FmeOptions, text='View:', anchor=W, width=8)
        self.LblViewFullStar.config(font=('Times', 16))
        self.LblViewFullStar.grid(row=2,column=0)

        # Defining a variable to store the input for the Default Side radio buttons
        self.VarViewFullStarInput = IntVar()

        # Radio Buttons for View Full/Star side, setting the font and placing them in the grid.
        self.RbViewFull = Radiobutton(self.FmeOptions, text='Full Set', variable=self.VarViewFullStarInput, value=1, width=8, anchor=W)
        self.RbViewFull.config(font=('Times', 14))
        self.RbViewFull.grid(row=3,column=0)
        self.RbViewStar = Radiobutton(self.FmeOptions, text='Starred Cards Only', variable=self.VarViewFullStarInput, value=2, width=16, anchor=W)
        self.RbViewStar.config(font=('Times', 14))
        self.RbViewStar.grid(row=3,column=1, columnspan=2)

        # Setting 'Full' as the default option to act as an existence check by forcing a value
        self.RbViewFull.select()

        # Card Order Option

        # Creating the Card Order viewing options label, setting the font and placing it in the grid
        self.LblCardOrder = Label(self.FmeOptions, text='Card Order:', anchor=W)
        self.LblCardOrder.config(font=('Times', 16))
        self.LblCardOrder.grid(row=4,column=0)

        # Defining a variable to store the input for the Default Side radio buttons
        self.VarCardOrderInput = IntVar()

        # Radio Buttons for View Full/Star side, setting the font and placing them in the grid.
        self.RbCardOrderOrg = Radiobutton(self.FmeOptions, text='Original', variable=self.VarCardOrderInput, value=1, anchor=W)
        self.RbCardOrderOrg.config(font=('Times', 14))
        self.RbCardOrderOrg.grid(row=5, column=0)
        self.RbCardOrderRnd = Radiobutton(self.FmeOptions, text='Random', variable=self.VarCardOrderInput, value=2, anchor=W)
        self.RbCardOrderRnd.config(font=('Times', 14))
        self.RbCardOrderRnd.grid(row=5,column=1)

        # Setting 'Full' as the default option to act as an existence check by forcing a value
        self.RbCardOrderOrg.select()

        # Variables used in ViewPage Function but are defined here as the function is recalled from other functions
        # Defining a variable to store the number of the card that is being shown.
        self.number = 0
        # Defining a list to store the cards that have been shown. Used when the card order option has been set to random
        self.shownCards = []
        # Defining a counting variable to be used when going back to previous cards when the card order option is set to random
        self.cycles = 0
        # Creating the View Set button, setting the size and font, placing it in the grid
        # Command calles the ViewPage function
        self.BtnView = Button(self.FmePage1ViewOverview, text='View Set', width=24, command=lambda *args: self.ViewPage(master, self.number))
        self.BtnView.config(font=('Times', 16))
        self.BtnView.grid(row=11, column=5, rowspan=1, columnspan=3)

        # Creating the delete set button, setting the size and font, placing it in the grid
        # Command calls the corresponding function from FunctionsCLI
        # listSetName argument is listSetName from the design and is defined outside the class
        self.BtnDelete = Button(self.FmePage1ViewOverview, text='Delete Set', command=lambda *args: self.ViewOverviewDelete(listSetName))
        self.BtnView.config(font=('Times', 16))
        self.BtnDelete.grid(row=13, column=5, rowspan=1)

        # Creating a help button, setting the size and font, placing it in the grid
        # Command calls the corresponding function which creates the help page in a sub-window
        self.BtnHelp = Button(self.FmePage1ViewOverview, text='Help', width=8, command=self.HelpPage)
        self.BtnHelp.config(font=('Times', 16))
        self.BtnHelp.grid(row=13, column=7, rowspan=1)

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
                self.LblBlank = Label(self.FmePage1ViewOverview, height=1, width=8)
                self.LblBlank.config(font=('Arial', 10))
                # Placing the label in the grid at column, sublist and row, index of sublist
                self.LblBlank.grid(row=i, column=self.countBlank)
            # Increments the counting variable
            self.countBlank += 1

        # Places the top frame on the grid
        self.FmePage1ViewOverview.grid(column=0, row=0, columnspan=3)

    # Function to create the table in ViewOverview  PAGE CHILD FUNCTION
    # listSet argument is listSet from the desing and is defined outside GUI
    def ViewOverviewTable(self, listSet):
        # Creating list out of listSet that is made up of StringVars
        self.count = 0
        self.cards = []
        # Goes through each card
        for i in range(0, len(listSet[1])):
            # Creates a StringVar for the term of the card and sets it to the current card's term
            self.VarCardT = StringVar()
            self.VarCardT.set(listSet[1][self.count][0])

            # Creates a StringVar for the definition of the card and sets it to the current card's definition
            self.VarCardD = StringVar()
            self.VarCardD.set(listSet[1][self.count][1])

            # Creates a StringVar for the imageDirectory of the card and sets it to the current card's imageDirectory
            self.VarCardI = StringVar()
            self.VarCardI.set(listSet[1][self.count][2])

            # Creates a StringVar for the star status of the card and sets it to the current card's star status
            self.VarCardF = StringVar()
            self.VarCardF.set(listSet[1][self.count][3])

            # Adds the stringVars to the list as one index
            self.cards.append([self.VarCardT, self.VarCardD, self.VarCardI, self.VarCardF])
            self.count += 1

        # A variable to determinine the number of rows in the table size using the number of cards
        # x2 because there needs to be a border for each row,   +3 because there is a header column and a top border
        self.noCards = (len(self.cards) * 2) + 3

        # Creating the scroll bar by placing the table in a frame in a canvas in a frame
        # Function to configure the canvas
        def CanvasConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=490, height=600)
        # Creating the top frame for the scroll bar and placing it in the grid.
        self.FmeSbTop = Frame(self.FmePage1ViewOverview)
        self.FmeSbTop.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)
        # Creating a canvas top put in the top frame, setting it's size and placing it in the frame
        self.canvas = Canvas(self.FmeSbTop)
        # Creating the sub frame for the scroll bar and setting it's size.
        self.FmeSbSub = Frame(self.canvas, width=530, height=600)
        # Creating the scrollbar and making it vertical
        self.ScrollBar = Scrollbar(self.FmeSbTop, orient='vertical', command=self.canvas.yview)
        # Adding the scroll bar to the canvas
        self.canvas.configure(yscrollcommand=self.ScrollBar.set)
        self.ScrollBar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        # Setting the sub frame inside the frame
        self.canvas.create_window((0, 0), window=self.FmeSbSub, anchor='nw')
        self.FmeSbSub.bind('<Configure>', CanvasConfig)

        # Creating the frame to store the table in as a sub frame of the scroll bar sub frame (that's a sub, sub frame)
        #   this is done as the scroll bar was implemented after the creation of the function and the frame was already established.
        # This frame also stores the view (static) version of the table, another frame stores the edit (active) version of the table
        self.FmeTableView = Frame(self.FmeSbSub)

        # Creating the label for the header for the term column of the view table, setting the font and size, placing it in the grid
        self.LblTermHeader = Label(self.FmeTableView, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Creating the label for the header for the definition column of the view table, setting the font and the size, placing it in the grid
        self.LblDefHeader = Label(self.FmeTableView, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Creating the label for the header for the image directory column of the view table, setting the font and the size, placing it in the grid
        self.LblImgHeader = Label(self.FmeTableView, text='Image Directory', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 17, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)


        # Placing the view table in the grid. The rowspan is determined by the number of cards otherwise the other widgets become displaced
        self.FmeTableView.grid(row=2, column=1, rowspan=((len(self.cards) * 3) + (len(self.cards)) + 3), columnspan=3)

        # Setting the content for the 'Term' Column
        self.count = 0
        # Loop that goes through each row and if the row is odd (therefore not a border row)
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                # Variable to store the term of the current card, variable is a StringVar but contains a string version of the stringVar in the list
                self.VarCurrentTerm = StringVar()
                self.VarCurrentTerm.set(self.cards[self.count][0].get())
                # Creating a label where the text is the variable, setting the font and placing it in the grid using the loop as a grid reference for the row
                self.LblTerm = Label(self.FmeTableView, textvariable=self.VarCurrentTerm, anchor='w', width=12,
                                     height=3)
                self.LblTerm.config(font=('Times', 14))
                self.LblTerm.grid(row=i, column=1)
                self.count += 1

        # Setting the content for the 'Definition' Column
        # Code block is the same as above however it uses the 1st value in each sub list of self.cards instead of the 0th
        self.count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.VarCurrentDef = StringVar()
                self.VarCurrentDef.set(self.cards[self.count][1].get())
                self.LblDef = Label(self.FmeTableView, textvariable=self.VarCurrentDef, anchor='w', width=22,
                                    height=3)
                self.LblDef.config(font=('Times', 14))
                self.LblDef.grid(row=i, column=3)
                self.count += 1

        # Setting the content for the 'Image' Column
        # Code block is the same as above however it uses the 2nd value in each sub list of self.cards
        self.count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.VarCurrentImg = StringVar()
                self.VarCurrentImg.set(self.cards[self.count][2].get())
                self.LblImg = Label(self.FmeTableView, textvariable=self.VarCurrentImg, anchor='w', width=12,
                                    height=3)
                self.LblImg.config(font=('Times', 14))
                self.LblImg.grid(row=i, column=5)
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
                    self.LblBorder = Label(self.FmeTableView, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the first column place a label of the same width as the term labels
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableView, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the third column place a label of the same width as the definition labels
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableView, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the fifth column place a label of the same width as the image directory labels
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableView, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and odd column and not the first row place a label as high as the text labels
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On the first row and odd column and place a label as high as the header labels
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

        # Creating the Edit (Active) version of the table

        # Creating the frame which goes in the scroll bar sub frame in the same way as the View Table's frame
        self.FmeTableEdit = Frame(self.FmeSbSub)

        # Creating the label for the header for the term column of the edit table, setting the font and size, placing it in the grid
        self.LblTermHeader = Label(self.FmeTableEdit, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Creating the label for the header for the definition column of the edit table, setting the font and size, placing it in the grid
        self.LblDefHeader = Label(self.FmeTableEdit, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Creating the label for the header for the image directory column of the edit table, setting the font and size, placing it in the grid
        self.LblImgHeader = Label(self.FmeTableEdit, text='Image', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 18, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)

        # Defining a temporary variable to store the number of card for determining table size
        self.noCards = (len(self.cards) * 2) + 3

        # Creating the entry fields

        self.count = 0
        # Defining a list to store the cards after they are edited. Will be a list of lists
        self.LstEditCards = []
        # Loop that goes iterates through every row in the table for the amount of cards
        for i in range(2, self.noCards):
            # Creating a sub list to make adding to the above list easier
            self.LstEditCardsSub = []

            # If the current row is odd
            if (i % 2) == 1:
                # Setting the content for the 'Term' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.VarCurrentTerm = StringVar()
                self.VarCurrentTerm.set(self.cards[self.count][0].get())
                # Creating an entry field, setting the font, placing in the grid
                self.EntTerm = Entry(self.FmeTableEdit, textvariable=self.VarCurrentTerm, width=12)
                # Adding the text to the sub list in a StringVar format
                self.LstEditCardsSub.append(self.VarCurrentTerm)
                self.EntTerm.config(font=('Times', 14))
                self.EntTerm.grid(row=i, column=1)

                # Setting the content for the 'Definition' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.VarCurrentDef = StringVar()
                self.VarCurrentDef.set(self.cards[self.count][1].get())
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.EntDef = Entry(self.FmeTableEdit, textvariable=self.VarCurrentDef, width=22)
                # Adding the text to the sub list in a StringVar format
                self.LstEditCardsSub.append(self.VarCurrentDef)
                self.EntDef.config(font=('Times', 14))
                self.EntDef.grid(row=i, column=3)

                # Setting the content for the 'Image' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.VarCurrentImg = StringVar()
                self.VarCurrentImg.set(self.cards[self.count][2].get())
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.EntImg = Entry(self.FmeTableEdit, textvariable=self.VarCurrentImg, width=12)
                # Adding the text to the sub list in a StringVar format
                self.LstEditCardsSub.append(self.VarCurrentImg)
                self.EntImg.config(font=('Times', 14))
                self.EntImg.grid(row=i, column=5)

                # Keeping the star/unstar value by adding it to the sublist
                self.LstEditCardsSub.append(self.cards[self.count][3])

                # Adding the sublist to the new list
                self.LstEditCards.append(self.LstEditCardsSub)
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
                    self.LblBorder = Label(self.FmeTableEdit, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the first column place a label of the same width as the term labels
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableEdit, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the third column place a label of the same width as the definition labels
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableEdit, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the fifth column place a label of the same width as the image directory labels
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableEdit, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and odd column and not the first row place a label as high as the text labels
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableEdit, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On the first row and odd column and place a label as high as the header labels
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableEdit, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

    # Function to change the currently viewed set   COMPLETE
    def ViewOverviewSelect(self):
        # Call the Select Set Function from FunctionsCLI with input from entry field as wantedSet argument.
        # Use the function to gain the index position of the wanted set
        self.location = SelectSet(self.VarSelectInput.get(), listSetName)
        # If the set was not found
        if self.location == -1:
            # Inform the user with a showinfo message box and exit function
            messagebox.showinfo('Does not Exist', 'The name of the set you entered does not exist.\n'
                                                        'Re-enter a name and try again.')
            return
        # Reset the currentSetName and currentSetFile using output from SelectSet Function
        self.currentSetName.set(listSetName[self.location][0])
        self.currentSetFile.set(listSetName[self.location][1])

        # Call ListSetCreate Function to recreate listSet but with the new set
        listSet = ListSetCreate(self.currentSetFile.get())
        # Recall the table function to update the table with the new list
        self.ViewOverviewTable(listSet)

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
            self.FmeTableView.grid_remove()

            # Place the edit version of the table in the grid using the same line as in the other function
            self.FmeTableEdit.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)

            # Change the text on the button
            self.VarEditSaveBtnText.set('Save Changes')

        # If the table is in edit mode
        elif status == 1:
            # Set status to the view mode
            status = 0

            # Block to read the edit table and change the list of StringVars to a list of strings
            # Also checks if there is a blank space. If there is inform the user using a showinfo message box and abort the function
            self.lstStrings = []
            for i in self.LstEditCards:
                self.lstStringsSub = []
                self.count = 0
                for j in i:
                    x = j.get()
                    if x != '' or self.count == 3:
                        self.lstStringsSub.append(x)
                    else:
                        messagebox.showinfo('Saving', 'Changes could not be saved as there was a blank space.')
                        return
                    self.count += 1
                self.lstStrings.append(self.lstStringsSub)

            # Block to read the edit table and write the values to a list in the format of self.cards then set self.cards
            #       to the new list
            self.LstNew = []
            for i in self.LstNew:
                self.LstNewSub = []
                for j in i:
                    index = StringVar()
                    index.set(j)
                    self.LstNewSub.append(index)
                self.LstNew.append(self.LstNew2Sub)
            self.cards = self.LstNew

            # Save the set by rewriting to file using the SaveSet function using FunctionsCLI
            SaveSet(self.currentSetName.get(), self.currentSetFile.get(), self.lstStrings)

            # Removes the edit table from the grid
            self.FmeTableEdit.grid_remove()

            # Recreating listSet in the format specified in the design
            listSet = [self.currentSetName.get(), self.lstStrings]
            # Recalling the Table function using listSet
            self.ViewOverviewTable(listSet)

            # Place the view version of the table in the grid
            self.FmeTableView.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)

            # Reset the text on the button
            self.VarEditSaveBtnText.set('Edit Set')
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
            # Generate a new listSet using the ListSetCreate function. Using the string from the setFile stringVar
            listSet = ListSetCreate(self.currentSetFile.get())
            # Recall the table function to generate the table with the new set
            self.ViewOverviewTable(listSet)
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
        self.FmePage1ViewOverview.grid_remove()

        # Creating the frame to store the contents of the Create Page
        self.FmePage2CreateSet = Frame(master)

        # Creating a variable to store the name of the set.
        self.VarName = StringVar()
        # Setting the default text to act as an existance check and an instruction
        self.VarName.set('Enter Name of Set')
        # Creating the entry field to enter the name of the set, setting the font, size, colour and placing it in the grid
        self.EntName = Entry(self.FmePage2CreateSet, textvariable=self.VarName, width=24, bg='Orange')
        self.EntName.config(font=('Arail', 32, 'bold underline'))
        self.EntName.grid(row=0,column=0,rowspan=2,columnspan=4)

        # Creating the button to add another row to the table, setting the font and placing it in the grid.
        # Command calls the the function to add or remove a row.
        # The self.varTableRowSpan argument is the amount of rows currently in the table.
        # The 0 tells the function to add a row as the function can add and remove rows
        self.BtnAddRow = Button(self.FmePage2CreateSet, text='Add Row', width=16, command=lambda *args: self.CreateChangeRow(self.VarTableRowSpan, 0))
        self.BtnAddRow.config(font=('Times', 16))
        self.BtnAddRow.grid(row=4, column=5, rowspan=1, columnspan=1)

        # Creating the button to remove a row to the table, setting the font and placing it in the grid.
        # Command calls the the function to add or remove a row.
        # The self.varTableRowSpan argument is the amount of rows currently in the table.
        # The 1 tells the function to remove a row as the function can add and remove rows
        self.BtnRemoveRow = Button(self.FmePage2CreateSet, text='Remove Row', width=16, command=lambda *args: self.CreateChangeRow(self.VarTableRowSpan, 1))
        self.BtnRemoveRow.config(font=('Times', 16))
        self.BtnRemoveRow.grid(row=6, column=5, rowspan=1, columnspan=1)

        # Variable to determine the number of rows in the table. And the rowspan of the table.  Can be changed with buttons
        # VarTableRowSpan = (number of cards * 2) + 3, 15 is the default amount of rows
        self.VarTableRowSpan = IntVar()
        self.VarTableRowSpan = (15 * 2) + 3
        # LstCardsCreate is a list of lists that will contain the entered data
        self.LstCardsCreate = []
        # Calling the function to create the table
        self.CreateTable()

        # Creating the button to save the set that has been created and return to the ViewOverview Page, setting the font and placing it in the grid
        # Command calls the corresponding function
        self.BtnSave = Button(self.FmePage2CreateSet, text='Save Set', width=16, command=self.CreateSave)
        self.BtnSave.config(font=('Times', 16))
        self.BtnSave.grid(row=1, column=5, rowspan=1, columnspan=1)

        # Creating the button to exit the Create page without saving the set, setting the font and placing it in the grid
        # Command calls the corresponding function
        self.BtnDelete = Button(self.FmePage2CreateSet, text='Cancel Set Creation', width=16, command=self.CreateDelete)
        self.BtnDelete.config(font=('Times', 16))
        self.BtnDelete.grid(row=8, column=5, rowspan=1, columnspan=1)

        # Creating the button to call the import set sub window and function, setting the font and placing it in the grid
        # Command calls the corresponding function which creates the sub window and its functionality
        self.BtnImport = Button(self.FmePage2CreateSet, text='Import Set', width=16, command=self.CreateImport)
        self.BtnImport.config(font=('Times', 16))
        self.BtnImport.grid(row=10, column=5, rowspan=1, columnspan=1)

        # Creating the button to call the help sub window, setting the font and placing it in the grid
        # Command calls the help function
        self.BtnHelp = Button(self.FmePage2CreateSet, text='Help', width=16, command=self.HelpPage)
        self.BtnHelp.config(font=('Times', 16))
        self.BtnHelp.grid(row=12, column=5, rowspan=1, columnspan=1)

        # Creating the blank spaces used to format the top frame

        # List of lists stores where the blank spaces need to go. Each sublist is a column and the items in the sublist are the rows for the column
        blanks = [[2,3,4,5,6,7,8,9], [2], [2], [2], [0,1,2,3,4,5,6,7,8,9,11], [0,3,5,7,9,11], [0,3,5,7,9,11]]
        # Defining a counting variable to store the index value of the current sublist
        self.countBlank = 0
        # Goes through each sublist in self.lstBlanks
        while self.countBlank < 7:
            # Goes through each item in the sublist
            for i in blanks[self.countBlank]:
                # Creates a label with no text of specific size
                self.LblBlank = Label(self.FmePage2CreateSet, height=1, width=8)
                self.LblBlank.config(font=('Arial', 10))
                # Placing the label in the grid at column, sublist and row, index of sublist
                self.LblBlank.grid(row=i, column=self.countBlank)
            # Increments the counting variable
            self.countBlank += 1

        # Places the top frame on the grid
        self.FmePage2CreateSet.grid(row=0,column=0)

    # Function to create the table in Create Page   PAGE CHILD FUNCTION
    def CreateTable(self):

        # Creating List of StringVars with default values that act as an existance check and an instruction
        # Define a counting variable to store the number of the card
        self.count = 0
        # Checks that the list is empty and therefore has just been created in the CreatePage function
        # Otherwise everything the function is called the list will reset
        if len(self.LstCardsCreate) < 1:
            while self.count < 15:
                # Default text takes the form of the a string and the counter variable
                self.VarCardT = StringVar()
                self.VarCardT.set(('Enter Term ' + str(self.count)))

                self.VarCardD = StringVar()
                self.VarCardD.set(('Enter Definition ' + str(self.count)))

                self.VarCardI = StringVar()
                self.VarCardI.set(('Enter Image Directory ' + str(self.count)))

                self.LstCardsCreate.append([self.VarCardT, self.VarCardD, self.VarCardI])
                self.count += 1

        # Creating the scroll bar by placing the table in a frame in a canvas in a frame
        # Function to configure the canvas
        def CanvasConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=490, height=600)
        # Creating the top frame for the scroll bar and placing it in the grid.
        self.FmeSbTop = Frame(self.FmePage2CreateSet)
        self.FmeSbTop.grid(row=3, column=1, rowspan=self.VarTableRowSpan, columnspan=3)
        # Creating a canvas top put in the top frame, setting it's size and placing it in the frame
        self.canvas = Canvas(self.FmeSbTop)
        # Creating the sub frame for the scroll bar and setting it's size.
        self.FmeSbSub = Frame(self.canvas, width=100, height=600)
        # Creating the scrollbar and making it vertical
        self.ScrollBar = Scrollbar(self.FmeSbTop, orient='vertical', command=self.canvas.yview)
        # Adding the scroll bar to the canvas
        self.canvas.configure(yscrollcommand=self.ScrollBar.set)
        self.ScrollBar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        # Setting the sub frame inside the frame
        self.canvas.create_window((0, 0), window=self.FmeSbSub, anchor='nw')
        self.FmeSbSub.bind('<Configure>', CanvasConfig)

        # Creating the frame to store the table in as a sub frame of the scroll bar sub frame (that's a sub, sub frame)
        #   this is done as the scroll bar was implemented after the creation of the function and the frame was already established.
        self.FmeTableCreate = Frame(self.FmeSbSub)
        # Placing the grid in the frame
        self.FmeTableCreate.grid(row=3, column=1, rowspan=self.VarTableRowSpan, columnspan=3)


        # Creating the label for the header for the term column of the table, setting the font and size, placing it in the grid
        self.LblTermHeader = Label(self.FmeTableCreate, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Creating the label for the header for the definition column of the table, setting the font and size, placing it in the grid
        self.LblDefHeader = Label(self.FmeTableCreate, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Creating the label for the header for the image directory column of the table, setting the font and size, placing it in the grid
        self.LblImgHeader = Label(self.FmeTableCreate, text='Image Directory', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 17, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)


        # Creating the entry fields in the table

        self.count = 0
        # Loop that iterates through every row in the table
        for i in range(2, self.VarTableRowSpan):
            # Creating a sub list to make adding to the above list easier
            self.LstCardsSub =[]
            if (i % 2) == 1:
                # Setting the content for the 'Term' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.VarCurrentTerm = StringVar()
                self.VarCurrentTerm.set(self.LstCardsCreate[self.count][0].get())
                # Creating an entry field, setting the font, placing in the grid
                self.EntTerm = Entry(self.FmeTableCreate, textvariable=self.VarCurrentTerm, width=12)
                # Adding the text to the sub list in a StringVar format
                self.LstCardsSub.append(self.VarCurrentTerm)
                self.EntTerm.config(font=('Times', 16))
                self.EntTerm.grid(row=i, column=1)

                # Setting the content for the 'Definition' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.VarCurrentDef = StringVar()
                self.VarCurrentDef.set(self.LstCardsCreate[self.count][1].get())
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.EntDef = Entry(self.FmeTableCreate, textvariable=self.VarCurrentDef, width=22)
                # Adding the text to the sub list in a StringVar format
                self.LstCardsSub.append(self.VarCurrentDef)
                self.EntDef.config(font=('Times', 16))
                self.EntDef.grid(row=i, column=3)

                # Setting the content for the 'Image' Column
                # Define a stringVar to store the string version of the current term to be set as the default text in the entry field
                self.VarCurrentImg = StringVar()
                self.VarCurrentImg.set(self.LstCardsCreate[self.count][2].get())
                # Define a stringVar to store the string version of the current definition to be set as the default text in the entry field
                self.EntImg = Entry(self.FmeTableCreate, textvariable=self.VarCurrentImg, width=12)
                # Adding the text to the sub list in a StringVar format
                self.LstCardsSub.append(self.VarCurrentImg)
                self.EntImg.config(font=('Times', 16))
                self.EntImg.grid(row=i, column=5)

                # Adding the sublist to the new list
                self.LstCardsCreate.append(self.LstCardsSub)
                self.count += 1

        # Setting border around the table
        # The label contains no text and is uses a standard colour.
        # The size depends on where the border label is
        # Creating a list to store the cells that have a border label
        self.border = []
        # Loop that iterates for the amount of rows
        for i in range(0, self.VarTableRowSpan):
            # Loop that iterates through every column (there are always seven columns)
            for j in range(0, 7):
                # On even rows and even columns place a label
                if (i % 2) == 0 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableCreate, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the first column place a label of the same width as the term labels
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableCreate, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the third column place a label of the same width as the definition labels
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableCreate, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and the fifth column place a label of the same width as the image directory labels
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableCreate, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On even rows and odd column and not the first row place a label as high as the text labels
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableCreate, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # On the first row and odd column and place a label as high as the header labels
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableCreate, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

    # Function to save the set that has just been made and change the screen back to ViewOverview
    #                                               COMPLETE
    def CreateSave(self):
            # Reading the table list in to a list of lists of strings
            self.lstCardsCreateString = []
            for i in self.LstCardsCreate:
                self.LstNewSub = []
                for j in i:
                    x = j.get()
                    # If there is a blank space in the table inform the user with a showinfo message box and exit the function
                    if x != '':
                        self.LstNewSub.append(x)
                    else:
                        messagebox.showinfo('Saving', 'Set could not saved as there was a blank space.')
                        return
                self.lstCardsCreateString.append(self.LstNewSub)

            # Go through each sublist in the string list and add, 'no' as the default View Full/Star value
            for i in self.lstCardsCreateString:
                i.append('no')

            # String liss is now is listCards from design and is ready to be merged with CLI

            # Crete the name of the file to be stored in using the format, file_setName
            self.setFile = ('file_'+str(self.EntName.get()))

            # Write the set to a file using SaveSet function in FunctionsCLI
            # self.EntName.get() is the string from the entry field on the page.
            SaveSet(self.EntName.get(), self.setFile, self.lstCardsCreateString)

            # Adding the set to listSetName and informing the user with a showinfo messagebox
            listSetName.append([self.EntName.get(), self.setFile])
            messagebox.showinfo('Saving', 'Set Saved Successfully.')

            # Removing the frame containing everything from the create page
            self.FmePage2CreateSet.grid_remove()
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
        # If the function ran from the 'Remove Row' Button, decrease the row variable
        elif change == 1:
            numRow -= 2

        # Reading the table to a list of strings
        self.LstNew = []
        for i in self.LstCardsCreate:
            self.LstNewSub = []
            for j in i:
                x = j.get()
                self.LstNewSub.append(x)
            self.LstNew.append(self.LstNewSub)

        # Taking the list of strings and writing it to a list of StringVars
        self.LstNew2 = []
        for i in self.LstNew:
            self.LstNew2Sub = []
            for j in i:
                index = StringVar()
                index.set(j)
                self.LstNew2Sub.append(index)
            self.LstNew2.append(self.LstNew2Sub)
        self.cards = self.LstNew2

        # Making sure the row number variable is an integer
        numRow = int(numRow)
        # Setting the self variable to the variable that was changed inside the function
        self.VarTableRowSpan = numRow
        # Recalling the table creation function
        self.CreateTable()

    # Function to delete the set being made         COMPLETE
    # Button reads 'Cancel Set Creation'
    def CreateDelete(self):
        # Create a variable to store the text that will be shown in the user notification to make the next line easier to read
        self.message = 'Are you sure you want to cancel set creation?\nThis will return you to the Start-up screen and ' \
                       'progress will be lost.\nThis can not be undone.'
        # Message box asking for confirmation
        self.VarContinue = messagebox.askokcancel(title='Cancel', message=self.message)
        # If the user confirms their choice
        if self.VarContinue:
            # Remove the Create Page and Call the ViewOverview Page Function
            self.FmePage2CreateSet.grid_remove()
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
            self.WinImport = Toplevel(root)
            self.WinImport.title('Import')

            # Create a frame to place everything in. Place the frame in the sub window
            self.FmeImportPage = Frame(self.WinImport)
            self.FmeImportPage.grid()

            # Create a title lable, setting the colour size and font, place in grid
            self.LblImTitle = Label(self.FmeImportPage, text='Import Set', bg='Orange', width=30, height=1)
            self.LblImTitle.config(font=('Arail', 28, 'underline'))
            self.LblImTitle.grid(row=0,column=0,rowspan=1,columnspan=2)

            # Create the label to accompany the entry field that gets the name of the set to be imported
            self.LblImSetName = Label(self.FmeImportPage, text='Name of Set:')
            # Set the font for the label and place in the grid
            self.LblImSetName.config(font=('Times', 16))
            self.LblImSetName.grid(row=1, column=0, rowspan=1, columnspan=1)

            # Define variable to store the input from the entry field as a StringVar
            self.VarImSetName = StringVar()
            # Provide a default value into the entry field to act as an existence check and an instruction
            self.VarImSetName.set('Enter Name Here')
            # Create the entry field to get the name of the set being imported, set the font, place in the grid
            self.EntImSetName = Entry(self.FmeImportPage, textvariable=self.VarImSetName, width=20)
            self.EntImSetName.config(font=('Times', 16))
            self.EntImSetName.grid(row=1, column=1, rowspan=1, columnspan=1)

            # Create a label to accompany the entry field that gets the file directory, set the font and place in the grid
            self.LblImPrompt = Label(self.FmeImportPage, text='Directory of Import File:')
            self.LblImPrompt.config(font=('Times', 16))
            self.LblImPrompt.grid(row=2,column=0,rowspan=1,columnspan=1)

            # Define a variable as a StringVar to store the input from the entry
            self.VarImDirectory = StringVar()
            # Provide a default value into the entry field to act as an existence check
            self.VarImDirectory.set('Enter Directory Here')
            # Create the entry field to get the directory of the file to be imported, set the font and place in the grid
            self.EntImDir = Entry(self.FmeImportPage, textvariable=self.VarImDirectory, width=20)
            self.EntImDir.config(font=('Times', 16))
            self.EntImDir.grid(row=2,column=1,rowspan=1,columnspan=1)

            # Create a button to call the sub function of this function that imports the set. Set the font, place in grid
            # Command calls the sub function
            # The self.VarImDirectory.get() argument is the string of the directory entered into the entry
            # The self.varImSetName.get() argument is the string of the name entered into the entry
            self.BtnImImport = Button(self.FmeImportPage, text='Import File', width=40,
                            command=lambda *args: ImImport(self, self.VarImDirectory.get(), self.VarImSetName.get()))
            self.BtnImImport.config(font=('Times', 16))
            self.BtnImImport.grid(row=3,column=0,rowspan=1,columnspan=2)

            # Define a StringVar to store a short set of instructions
            # Instructions are stored here instead of the widget creation line for readability of the code
            self.VarImTxt = StringVar()
            self.VarImTxt.set('Imported sets must be a CSV (Comma Separated Value) file in the following form;\n'
                     'term,definition,img_directory\nterm,definition,img_directory\n... , ... , ...\nWhere each line '
                     'represents a different card.\nExample Directory: /Users/19ecornish/Downloads/set.csv\nAfter a '
                              'successful import you will be returned to the start-up screen.')
            # Create a label to provide some basic instructions. Set the font and place in the grid
            self.LblImTxt = Label(self.FmeImportPage, textvariable=self.VarImTxt, anchor=NW)
            self.LblImTxt.config(font=('Times', 16))
            self.LblImTxt.grid(row=4,column=0,rowspan=1,columnspan=2)

            # Create a button to exit the importing and close the sub window, set the font and place in the grid
            # Command destroy's the sub window which consequentially exits the function
            self.BtnImExit = Button(self.FmeImportPage, text='Cancel Import', command=self.WinImport.destroy)
            self.BtnImExit.config(font=('Times', 16))
            self.BtnImExit.grid(row=5,column=1,rowspan=1,columnspan=1)

            # Create a blank label of set size to assist in the positioning of the exit button
            self.LblBlank = Label(self.FmeImportPage, width=14, height=1)
            self.LblBlank.grid(row=5, column=0,rowspan=1,columnspan=1)

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
                self.WinImport.destroy()
                # Removing the frame containing everything from the create page
                self.FmePage2CreateSet.grid_remove()
                # Returning to the ViewOverview Screen
                self.ViewOverviewPage(self.master)
            # If the import was not successful
            elif not self.check:
                # Inform the user and provide some quick suggestions on what to check
                messagebox.showinfo('Import', 'Import Unsuccessful\nCheck the directory, file type and the import format.')
                # Exit the function
                return

    # Function for the View Page                    PAGE FUNCTION
    def ViewPage(self, master, number):
        # Checks if there are more cards
        if number < len(self.cards):
            # If the user selected view all or view Fav AND the current card is a favourite
            if self.VarViewFullStarInput.get() == 1 or self.VarViewFullStarInput.get() == 2 and self.cards[number][3].get() == 'yes':
                # Removing the frame containing ViewOverviewPage
                self.FmePage1ViewOverview.grid_remove()

                # Creating the frame to store the contents of Create Page grid line at bottom of function
                self.FmePage3View = Frame(master)

                # Widget 1
                self.LblName = Label(self.FmePage3View, textvariable=self.currentSetName, width=23, bg='Orange')
                self.LblName.config(font=('Arail', 32, 'bold underline'))
                self.LblName.grid(row=0, column=0, rowspan=1, columnspan=5)

                # Widget 2
                self.FmeDisplay = Frame(self.FmePage3View)
                self.FmeDisplay.grid(row=2, column=1, rowspan=9, columnspan=5)


                # Can show text 8 lines high and 30 characters wide

                # Defining a label to show the term of the card
                self.VarCardShowTerm = StringVar()
                self.VarCardShowTerm.set(self.cards[number][0].get())
                self.LblCardTerm = Label(self.FmeDisplay, height=8, width=30, textvariable=self.VarCardShowTerm)
                self.LblCardTerm.config(font=('Times', 32))                                                         # If the default side is set to term show the definition for the first card

                # Defining a label to show the def of the card
                self.VarCardShowDef = StringVar()
                self.VarCardShowDef.set(self.cards[number][1].get())
                self.LblCardDef = Label(self.FmeDisplay, height=8, width=30, textvariable=self.VarCardShowDef)
                self.LblCardDef.config(font=('Times', 32))

                # Defining a label to show the image of the card
                try:
                    self.ImgDirectory = StringVar()
                    self.ImgDirectory.set(self.cards[number][2].get())
                    # Opening the image file
                    self.ImgTemp = Image.open(self.ImgDirectory.get())
                    # Resizing the image
                    self.ImgTemp = self.ImgTemp.resize((367, 275), Image.ANTIALIAS)  # (width,height)
                    # Saving the image to a file in a format recognised by tkinter
                    self.ImgTemp.save('ImageTempFile.gif', 'gif')
                    # Opening the image file as a PhotoImage object
                    self.ImgObj = PhotoImage(file='ImageTempFile.gif')
                    # Placing the image object in a label
                    self.LblCardImg = Label(self.FmeDisplay, image=self.ImgObj)
                    # Setting the image method of the label to the image object
                    self.LblCardImg.image = self.ImgObj
                except FileExistsError or FileNotFoundError or IsADirectoryError or NotADirectoryError:
                    messagebox.showinfo('File Error', 'Directory for this image is invalid.', icon='warning')

                # Depending on what the default side is, place the correct label defined above on the grid
                if self.VarDefaultSideInput.get() == 1:
                    self.LblCardTerm.grid(row=1, column=1)
                # If the default side is set to deinition show the definition for the first card
                elif self.VarDefaultSideInput.get() == 2:
                    self.LblCardDef.grid(row=1, column=1)
                # If the default side is set to image show the image for the first card
                elif self.VarDefaultSideInput.get() == 3:
                    self.LblCardImg.grid(row=1, column=1)


                # Border around content
                self.LblBorder1 = Label(self.FmeDisplay, height=2, width=4, bg='grey90')
                self.LblBorder1.config(font=('Times', 16))
                self.LblBorder1.grid(row=0, column=0)
                self.LblBorder2 = Label(self.FmeDisplay, height=2, width=60, bg='grey90')
                self.LblBorder2.config(font=('Times', 16))
                self.LblBorder2.grid(row=0, column=1)
                self.LblBorder3 = Label(self.FmeDisplay, height=2, width=4, bg='grey90')
                self.LblBorder3.config(font=('Times', 16))
                self.LblBorder3.grid(row=0, column=2)
                self.LblBorder4 = Label(self.FmeDisplay, height=16, width=4, bg='grey90')
                self.LblBorder4.config(font=('Times', 16))
                self.LblBorder4.grid(row=1, column=0)
                self.LblBorder5 = Label(self.FmeDisplay, height=16, width=4, bg='grey90')
                self.LblBorder5.config(font=('Times', 16))
                self.LblBorder5.grid(row=1, column=2)
                self.LblBorder6 = Label(self.FmeDisplay, height=2, width=4, bg='grey90')
                self.LblBorder6.config(font=('Times', 16))
                self.LblBorder6.grid(row=2, column=0)
                self.LblBorder7 = Label(self.FmeDisplay, height=2, width=60, bg='grey90')
                self.LblBorder7.config(font=('Times', 16))
                self.LblBorder7.grid(row=2, column=1)
                self.LblBorder8 = Label(self.FmeDisplay, height=2, width=4, bg='grey90')
                self.LblBorder8.config(font=('Times', 16))
                self.LblBorder8.grid(row=2, column=2)

                # Widget 3
                self.BtnBack = Button(self.FmePage3View, text='Back', width=24, command=self.ViewBack)
                self.BtnBack.config(font=('Times', 16))
                self.BtnBack.grid(row=0, column=5, rowspan=1, columnspan=3)

                # Widget 4
                self.LblProgressLabel = Label(self.FmePage3View, text='Progress:', width=12)
                self.LblProgressLabel.config(font=('Times', 16))
                self.LblProgressLabel.grid(row=2, column=7, rowspan=1, columnspan=1)

                # Widget 5                              WIP May need function to account for viewing option
                self.VarProgress = StringVar()
                if self.VarCardOrderInput.get() == 1:
                    self.VarProgress.set('{0}/{1}'.format((number + 1), len(self.cards)))
                elif self.VarCardOrderInput.get() == 2:
                    self.VarProgress.set('{0}/{1}'.format(len(self.shownCards)+1 - self.cycles, len(self.cards)))
                self.LblProgressResults = Label(self.FmePage3View, textvariable=self.VarProgress, width=12, anchor='e')
                self.LblProgressResults.config(font=('Times', 16))
                self.LblProgressResults.grid(row=3, column=7, rowspan=1, columnspan=1)

                # Widget 6
                self.VarStarUnstarText = StringVar()
                if self.cards[number][3].get() == 'no':
                    self.VarStarUnstarText.set('Star')
                elif self.cards[number][3].get() == 'yes':
                    self.VarStarUnstarText.set('Unstar')
                self.BtnStarUnstar = Button(self.FmePage3View, textvariable=self.VarStarUnstarText, width=12, command=lambda *args: self.ViewStarUnstar(number))
                self.BtnStarUnstar.config(font=('Times', 16))
                self.BtnStarUnstar.grid(row=6, column=7, rowspan=1, columnspan=1)

                # Widget 7
                self.BtnHelp = Button(self.FmePage3View, text='Help', width=12, command=self.HelpPage)
                self.BtnHelp.config(font=('Times', 16))
                self.BtnHelp.grid(row=9, column=7, rowspan=1, columnspan=1)

                # Widget 8
                self.BtnPrevious = Button(self.FmePage3View, text='Previous', width=8, command=lambda *args: self.ViewPrevious(master, number))
                self.BtnPrevious.config(font=('Times', 16))
                self.BtnPrevious.grid(row=11, column=1, rowspan=1, columnspan=1)

                # Widget 9
                self.BtnTerm = Button(self.FmePage3View, text='Term', width=8, command=self.ViewTerm)
                self.BtnTerm.config(font=('Times', 16))
                self.BtnTerm.grid(row=11, column=2, rowspan=1, columnspan=1)

                # Widget 10
                self.BtnImage = Button(self.FmePage3View, text='Image', width=8, command=self.ViewImage)
                self.BtnImage.config(font=('Times', 16))
                self.BtnImage.grid(row=11, column=3, rowspan=1, columnspan=1)

                # Widget 11
                self.BtnDef = Button(self.FmePage3View, text='Definition', width=8, command=self.ViewDef)
                self.BtnDef.config(font=('Times', 16))
                self.BtnDef.grid(row=11, column=4, rowspan=1, columnspan=1)

                # Widget 12
                self.BtnNext = Button(self.FmePage3View, text='Next', width=8, command=lambda *args: self.ViewNext(master, number))
                self.BtnNext.config(font=('Times', 16))
                self.BtnNext.grid(row=11, column=5, rowspan=1, columnspan=1)

                # Blank Spaces
                blanks = [[1,2,3,4,5,6,7,8,9,10,11,12], [1,12], [1,12], [1,12], [1,12], [1,12], [1,2,3,4,5,6,7,8,9,10,11,12],
                          [1,4,5,7,8,10,11,12], [0,1,2,3,4,5,6,7,8,9,10,11,12]]
                self.countBlank = 0
                while self.countBlank < 9:
                    for i in blanks[self.countBlank]:
                        self.LblBlank = Label(self.FmePage3View, height=1, width=8)#, bg='green', text='abc')
                        self.LblBlank.config(font=('Arial', 10))
                        self.LblBlank.grid(row=i, column=self.countBlank)
                    self.countBlank += 1

                self.FmePage3View.grid()

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

        # Rewriting self.cards as a list of strings
        self.cardsStrings = []
        for i in self.cards:
            self.cardsStringsSub = []
            self.cardsStringsSub.append(i[0].get())
            self.cardsStringsSub.append(i[1].get())
            self.cardsStringsSub.append(i[2].get())
            self.cardsStringsSub.append(i[3].get())
            self.cardsStrings.append(self.cardsStringsSub)

        # Rewriting listSet
        SaveSet(self.currentSetName.get(), self.currentSetFile.get(), self.cardsStrings)

        self.FmePage3View.grid_remove()
        self.ViewOverviewPage(self.master)

    # Function to Star/Unstar a card                COMPLETE
    def ViewStarUnstar(self, number):
        # If the card is not starred
        if self.cards[number][3].get() == 'no':
            # Star the card
            self.cards[number][3].set('yes')
            # Inform the user
            messagebox.showinfo('Star and Unstar', ' The card has been starred.')
            # Change the button to read 'Unstar'
            self.VarStarUnstarText.set('Unstar')
        # If the card is starred
        elif self.cards[number][3].get() == 'yes':
            # Unstar the card
            self.cards[number][3].set('no')
            # Inform the user
            messagebox.showinfo('Star and Unstar',' The card has been un-starred.')
            # Change the button to read 'Star'
            self.VarStarUnstarText.set('Star')

    # Function to go to the previous card           COMPLETE
    def ViewPrevious(self, master, number):
        if self.VarCardOrderInput.get() == 1:
            # Decreases the card counter by one
            number -= 1

            # If  viewFullStar is set to star the change back cards until a starred card is reached or there are no more cards
            if self.VarViewFullStarInput.get() == 2:
                while self.cards[number][3].get() == 'no':
                    number -= 1
            # If there are no more cards then inform the user
            if number < 0:
                messagebox.showinfo('No More Cards', 'There are no previous cards to go back to.')
                return
        elif self.VarCardOrderInput.get() == 2:
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
                    number = len(self.cards)

                self.cycles += 1

        # Re-run the view window with the new card
        self.FmePage3View.grid_remove()
        self.ViewPage(master, number)

    # Function to show the term                    COMPLETE
    def ViewTerm(self):
        # Remove the currently shown definition or image
        # Try blocks are to catch the error that ocurs if the card is not showing the definition or the image
        try:
            self.LblCardDef.grid_remove()
        except AttributeError:
            print('self.LblCardDef: Attribute Error')
        try:
            self.LblCardImg.grid_remove()
        except AttributeError:
            print('self.LblCardImg: Attribute Error')
        # Place the term label in the grid
        self.LblCardTerm.grid(row=1,column=1)

    # Function to show the image                   COMPLETE
    def ViewImage(self):
        # Remove the currently shown term or definition
        # Try blocks are to catch the error that ocurs if the card is not showing the term or the definition
        try:
            self.LblCardTerm.grid_remove()
        except AttributeError:                         
            print('self.LblCardTerm: Attribute Error')
        try:
            self.LblCardDef.grid_remove()
        except AttributeError:
            print('self.LblCardDef: Attribute Error')
        # Place the image label in the grid
        self.LblCardImg.grid(row=1,column=1)

    # Function to show the definition              COMPLETE
    def ViewDef(self):
        # Remove the currently shown term or image
        # Try blocks are to catch the error that ocurs if the card is not showing the term or the image
        try:
            self.LblCardTerm.grid_remove()
        except AttributeError:
            print('self.LblCardTerm: Attribute Error')
        try:
            self.LblCardImg.grid_remove()
        except AttributeError:
            print('self.LblCardImg: Attribute Error')
        # Place the definition label in the grid
        self.LblCardDef.grid(row=1,column=1)

    # Function to go to the next card               COMPLETE
    def ViewNext(self, master, number):
        # If the card order is set to Original
        if self.VarCardOrderInput.get() == 1:
            # Continue to the next card
            number += 1
        elif self.VarCardOrderInput.get() == 2:
            # Rewriting self.cards as a list of strings
            self.cardsStrings = []
            for i in self.cards:
                self.cardsStringsSub = []
                self.cardsStringsSub.append(i[0].get())
                self.cardsStringsSub.append(i[1].get())
                self.cardsStringsSub.append(i[2].get())
                self.cardsStringsSub.append(i[3].get())
                self.cardsStrings.append(self.cardsStringsSub)
            # Calling RndCardOrder function from FunctionsCLI to change to the next card in a randomised order
            number = RndCardOrder(number, self.cardsStrings, self.shownCards)
        # Remove the frame and rerun the Page function
        self.FmePage3View.grid_remove()
        self.ViewPage(master, number)

        
    # Function for the Help Page which has a sub window         Needs Text
    # The widgets in the sub window are created in the while loop and the text is determined using the sub function
    def HelpPage(self):
        # While loop with variable to make the program easier to condense and therefore improve readability
        self.HelpPageContents = True
        while self.HelpPageContents:
            # Creating the sub window with title
            self.WinHelp = Toplevel(root)
            self.WinHelp.title('Help')

            # Creating a frame to contain all of the widgets and placing it in the grid
            self.FmeHelpPage = Frame(self.WinHelp)
            self.FmeHelpPage.grid()

            # Creating a title widget, setting the size, colour and font and, placing it in the grid
            self.LblHpTitle = Label(self.FmeHelpPage, text='Help', bg='Orange', width=35, height=1)
            self.LblHpTitle.config(font=('Arail', 52, 'bold underline'))
            self.LblHpTitle.grid(row=0, column=0, rowspan=1, columnspan=9)

            # Creating a label to provide some short instructions on using the sub window, setting the font and placing it in the grid
            self.LblHpInstructions = Label(self.FmeHelpPage, text='Select the Button which'
                                                                  ' corresponds to the area you need help with.')
            self.LblHpInstructions.config(font=('Times', 18))
            self.LblHpInstructions.grid(row=1, column=0, columnspan=9)

            # Creating buttons to show different text for different area's of the program.
            # Buttons all call the same command, integer argument tells the function which button was pressed and therefore which set of text to display

            # Button for program navigation
            self.BtnHp1Navigation = Button(self.FmeHelpPage, text='General Use', width=10, command=lambda *args: HpText(self, 1))
            self.BtnHp1Navigation.config(font=('Times', 16))
            self.BtnHp1Navigation.grid(row=2, column=0, rowspan=1, columnspan=1)

            # Button for creating sets
            self.BtnHp2Creating = Button(self.FmeHelpPage, text='Creating Sets', command=lambda *args: HpText(self, 2))
            self.BtnHp2Creating.config(font=('Times', 16))
            self.BtnHp2Creating.grid(row=2, column=1)

            # Button for Editing Sets
            self.BtnHp3Editing = Button(self.FmeHelpPage, text='Editing Sets', command=lambda *args: HpText(self, 3))
            self.BtnHp3Editing.config(font=('Times', 16))
            self.BtnHp3Editing.grid(row=2, column=2)

            # Button for Selecting Sets
            self.BtnHp4Select = Button(self.FmeHelpPage, text='Selecting Different Sets', command=lambda *args: HpText(self, 4))
            self.BtnHp4Select.config(font=('Times', 16))
            self.BtnHp4Select.grid(row=2, column=3)

            # Button for Viewing an Overview of Sets
            self.BtnHp5ViewOverview = Button(self.FmeHelpPage, text='Viewing an Overview of a Set',
                                             command=lambda *args: HpText(self, 5))
            self.BtnHp5ViewOverview.config(font=('Times', 16))
            self.BtnHp5ViewOverview.grid(row=2, column=4)

            # Button for viewing sets
            self.BtnHp6Viewing = Button(self.FmeHelpPage, text='Viewing Sets', command=lambda *args: HpText(self, 6))
            self.BtnHp6Viewing.config(font=('Times', 16))
            self.BtnHp6Viewing.grid(row=2, column=5)

            # Button for deleting sets
            self.BtnHp7DeletingSets = Button(self.FmeHelpPage, text='Deleting Sets', command=lambda *args: HpText(self, 7))
            self.BtnHp7DeletingSets.config(font=('Times', 16))
            self.BtnHp7DeletingSets.grid(row=2, column=6)

            # Button for Importing Sets
            self.BtnHp8Import = Button(self.FmeHelpPage, text='Importing Sets', command=lambda *args: HpText(self, 8))
            self.BtnHp8Import.config(font=('Times', 16))
            self.BtnHp8Import.grid(row=2, column=7)

            # Button for exiting the help screed
            # Command closes the sub window which ends the function
            self.BtnHp9ExitHelp = Button(self.FmeHelpPage, text='Exit Help', command=self.WinHelp.destroy)
            self.BtnHp9ExitHelp.config(font=('Times', 16))
            self.BtnHp9ExitHelp.grid(row=2, column=8)

            # Creating a StringVar which will store the instructions being shown.
            # Variable will be updated using sub function
            self.VarHpText = StringVar()
            # By default setting it to many blank lines
            self.VarHpText.set('\n\n\n\n\n\n\n\n\n\n')

            # Placing the text in a label with a set width and height, setting the font and placing it in the grid
            self.LblHpText = Label(self.FmeHelpPage, textvariable=self.VarHpText, width=155, height=12, anchor=NW, justify=LEFT)
            self.LblHpText.config(font=('Times', 16))
            self.LblHpText.grid(row=3, column=0, rowspan=10, columnspan=9)

            # Setting the while loop variable to False and therefore ending the while loop after one iteration
            self.HelpPageContents = False

        # Sub function to change the text displayed
        # input argument determines the text being shown
        def HpText(self, input):
            # Creating a string variable to contain the text that will be used to set the StringVar
            text = self.VarHpText.get()
            # Ensuring that the input argument is an integer to prevent a TypeError or a ValueError
            input = int(input)
            # If, elif control structure that takes the given number and sets text to the correct string.
            if input == 1:
                text=('General Use\nThe program has three main pages, View Overview, Create and View.\nThe View Overview '
                      'page shows all of the cards in the set on a table.\nThe Create page allows you to create a new '
                      'set.\nThe View page shows each card one at a time in a sequance.\nThe View Overview page is shown '
                      'by default and is the start-up page. The Create Page can be reached with the Create Set button.\n'
                      'The Create Page can be closed using the Save Set button or the Cancel Set Creation button.\nThe '
                      'View page can be reached from the View Overview page with the View Set button and can be exited '
                      'using the Back button.\n\n')
            elif input == 2:
                text=('Creating sets\nTo enter the create set page select the Create Set button on the start-up page.\n'
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
                text=('Editing Sets\nSets can be edited from the start-up screen. To begin editing select the Edit Set '
                      'button.\nThis will turn the table into an editable version. Each cell can be changed.\nHowever '
                      'the name of the set can not be changed and the amount of cards can not be changed.\nTo save any '
                      'changes reselect the Edit Set button which will not read Save Changes.\nIf there are any blank '
                      'spaces you will not be able to save.\nWARNING if you enter another page by selecting Create Set '
                      'or View Set your changes will not be save and may be lost permanently.\nChanges can also be lost '
                      'if you change to a different set.\n\n\n\n')
            elif input == 4:
                text=('Selecting Sets\nTo select a different set first enter the name of the set you wish to select in '
                      'the entry field.\nThe entry field is Case, Space and Character Sensitive. Anything other than the'
                      ' exact name will not be recignised.\nAfter entering the exact name of the set select the Select S'
                      'et button.\nThe program will then attempt to change the set. If the name was correct then the table'
                      ' and the title will change.\nIf the name is incorrect then the program will inform you and you may'
                      ' try again.\n\n\n\n\n\n')
            elif input == 5:
                text=('Viewing an Overview of Sets.\nThe first screen shown when the program is opened shows an overview '
                      'of the last created set.\nThe set is shown in a table. The name of the set can also be seen in the'
                      ' top left hand corner of the page.\nFor instructions on how to edit the set select the Editing Sets '
                      'button.\nFor instructions on how to change the set select the Selecting Sets button.\nFor instruc'
                      'tions on how to change the current page select the General Use button.\nOn the right hand side of'
                      'the view overview screen are three sets of radio buttons with a label fro each set.\nThe radio '
                      'buttons set options that change how a set is viewed.\nThe options are detailed in the Viewing Se'
                      'ts instructions.\n\n\n')
            elif input == 6:
                text=('Viewing Sets\nSets can be viewed in a standard one card, one side at a time manner in the View S'
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
                text=('Deleting Sets.\nTo delete a set select the set you want to delete. For instructions of selecting'
                      ' a set select the Selecting Sets button.\nTo delete the currently viewed set select the Delete S'
                      'et button at the bottom of the View Overview page.\nThis will bring up a confirmation screen.\n'
                      'Select yes if you wish to delete the set. This will delete the set instantly and forever.\nThe '
                      'screen will then show the last created set.\n\n\n\n\n\n')
            elif input == 8:
                text=('Importing Sets.\nTo import a set select the button on the Create page. This will bring up a sub'
                      ' window.\nEnter a name for the set you wish to import into the name entry field.\nEnter the dire'
                      'ctory into the directory entry field. Then select the Import Set button.\nIf the importing was '
                      'successful you will be notified. If the import was unsuccessful then nothing will happen.\nTo '
                      'cancel importing select the Cancel Import button. This will take you back to the Create page.\n'
                      '\nTo ensure a successful importation of a set check for a correct directory, file type and file '
                      'format.\nExample Directory: /Users/19ecornish/Downloads/fileToImport.csv\nThe file MUST be a '
                      '.csv\nThe file must have the following format; term,definition,image newline where each line re'
                      'presents a new card.\n')
            # Setting the StringVar to the changed text variable
            self.VarHpText.set(text)
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

# Creating listSet from the design using the ListSetCreate function from FunctionsCLI
listSet = ListSetCreate(currentSetFileString)


# Calls the GUI
GUI = GUI(root)
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