from tkinter import *
from tkinter import messagebox

class GUI:
    # Initialisation Function
    def __init__(self, master):
        self.master = master
        master.title('Flash Card')

        # Calling the ViewOverview page to appear by default
        self.ViewOverviewPage(self.master)


    # Function for the ViewOverview Page            PAGE FUNCTION
    def ViewOverviewPage(self, master):

        # Default Page
        self.ViewOverviewPageContents = True
        while self.ViewOverviewPageContents:
            self.FmePage1ViewOverview = Frame(master)

            # Widget 1
            self.LblSet = Label(self.FmePage1ViewOverview, text='setName', bg='orange', width=32)
            self.LblSet.config(font=('Arial', 32, 'bold underline'))
            self.LblSet.grid(row=0, column=0, rowspan=1, columnspan=4)


            # Widget 2
            self.cards = []
            self.ViewOverviewTable()


            # Widget 3
            self.BtnCreate = Button(self.FmePage1ViewOverview, text='Create Set', width=24, command=lambda *args: self.CreatePage(master))
            self.BtnCreate.config(font=('Times', 16))
            self.BtnCreate.grid(row=0, column=5, rowspan=1, columnspan=3)

            # Widget 4
            self.VarEditSaveBtnBool = IntVar()
            self.VarEditSaveBtnBool.set(0)
            self.VarEditSaveBtnText = StringVar()
            self.VarEditSaveBtnText.set('Edit Set')
            self.BtnEditSave = Button(self.FmePage1ViewOverview, textvariable=self.VarEditSaveBtnText, width=24,
                                      command=self.ViewOverviewEditSaveBtn)
            self.BtnEditSave.config(font=('Times', 16))
            self.BtnEditSave.grid(row=2, column=5, rowspan=1, columnspan=3)

            # Widget 5

            # Need to change to entry field and a button for a search, this will allow for the use of a search function
            # Row = 3, column = 5       Rowspan =1,     Rowspan = 3
            self.VarSelectInput = StringVar()
            self.VarSelectInput.set('Enter the Name of the Set you Wish to Change to then click Select.')
            self.EntSelect = Entry(self.FmePage1ViewOverview, textvariable=self.VarSelectInput, width=20)
            self.EntSelect.config(font=('Times', 12))
            self.EntSelect.grid(row=3, column=5, rowspan=1, columnspan=2)

            self.BtnSelect = Button(self.FmePage1ViewOverview, text='Select', width=8, command=self.ViewOverviewSelect)
            self.BtnSelect.config(font=('Times', 16))
            self.BtnSelect.grid(row=3, column=7, rowspan=1, columnspan=1)


            # Widget 6

            # Creating the Frame
            self.FmeOptions = Frame(self.FmePage1ViewOverview)
            self.FmeOptions.grid(row=4, column=5, columnspan=3, rowspan=7)

            # Default Side

            # Default side label
            self.LblDefaultSide = Label(self.FmeOptions, text='Default Side:', anchor=W)
            self.LblDefaultSide.config(font=('Times', 16))
            self.LblDefaultSide.grid(row=0, column=0)

            # Variable for default side
            self.VarDefaultSideInput = IntVar()

            self.VarDefaultSideInput = 3

            # Radio Buttons for default side
            self.RbDefaultSideTerm = Radiobutton(self.FmeOptions, text='Term', variable=self.VarDefaultSideInput, value=1, anchor=W, width=8)
            self.RbDefaultSideTerm.config(font=('Times', 14))
            self.RbDefaultSideDef = Radiobutton(self.FmeOptions, text='Definition', variable=self.VarDefaultSideInput, value=2, anchor=W, width=10)
            self.RbDefaultSideDef.config(font=('Times', 14))
            self.RbDefaultSideImg = Radiobutton(self.FmeOptions, text='Image', variable=self.VarDefaultSideInput, value=3, anchor=W, width=7)
            self.RbDefaultSideImg.config(font=('Times', 14))

            # Setting 'Term' as the default option
            self.RbDefaultSideTerm.select()

            self.RbDefaultSideTerm.grid(row=1, column=0)
            self.RbDefaultSideDef.grid(row=1,column=1)
            self.RbDefaultSideImg.grid(row=1,column=2)

            # View Full/Star

            # View Full/Star Label
            self.LblViewFullStar = Label(self.FmeOptions, text='View:', anchor=W, width=8)
            self.LblViewFullStar.config(font=('Times', 16))
            self.LblViewFullStar.grid(row=2,column=0)

            # Variable for ViewFullStar
            self.VarViewFullStarInput = IntVar()

            # Radio Buttons for ViewFullStar
            self.RbViewFull = Radiobutton(self.FmeOptions, text='Full Set', variable=self.VarViewFullStarInput, value=1, width=8, anchor=W)
            self.RbViewFull.config(font=('Times', 14))
            self.RbViewStar = Radiobutton(self.FmeOptions, text='Starred Cards Only', variable=self.VarViewFullStarInput, value=16, anchor=W)
            self.RbViewStar.config(font=('Times', 14))

            # Setting 'Full' as the default option
            self.RbViewFull.select()

            self.RbViewFull.grid(row=3,column=0)
            self.RbViewStar.grid(row=3,column=1, columnspan=2)

            # Card Order

            # Card Order Label
            self.LblCardOrder = Label(self.FmeOptions, text='Card Order:', anchor=W)
            self.LblCardOrder.config(font=('Times', 16))
            self.LblCardOrder.grid(row=4,column=0)

            # Variable for Card Order
            self.VarCardOrderInput = IntVar()

            # Radio Buttons for Card Order
            self.RbCardOrderOrg = Radiobutton(self.FmeOptions, text='Original', variable=self.VarCardOrderInput, value=1, anchor=W)
            self.RbCardOrderOrg.config(font=('Times', 14))
            self.RbCardOrderRnd = Radiobutton(self.FmeOptions, text='Random', variable=self.VarCardOrderInput, value=2, anchor=W)
            self.RbCardOrderRnd.config(font=('Times', 14))

            # Setting 'Original' as the default option
            self.RbCardOrderOrg.select()

            self.RbCardOrderOrg.grid(row=5, column=0)
            self.RbCardOrderRnd.grid(row=5,column=1)

            # Widget 7
            self.BtnView = Button(self.FmePage1ViewOverview, text='View Set', width=24)
            self.BtnView.config(font=('Times', 16))
            self.BtnView.grid(row=11, column=5, rowspan=1, columnspan=3)

            # Widget 8
            self.BtnDelete = Button(self.FmePage1ViewOverview, text='Delete Set')
            self.BtnView.config(font=('Times', 16))
            self.BtnDelete.grid(row=13, column=5, rowspan=1)

            # Widget 9
            self.BtnHelp = Button(self.FmePage1ViewOverview, text='Help', width=8, command=self.HelpPage)
            self.BtnHelp.config(font=('Times', 16))
            self.BtnHelp.grid(row=13, column=7, rowspan=1)

            # Blank Spaces

            blanks = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
             [1, 12], [1, 12, 13], [1, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
            self.countBlank = 0
            while self.countBlank < 9:
                for i in blanks[self.countBlank]:
                    self.LblBlank = Label(self.FmePage1ViewOverview, height=1, width=8)
                    self.LblBlank.config(font=('Arial', 10))
                    # self.LblBlank = Label(self.FmePage1ViewOverview, height=1, width=8)
                    self.LblBlank.grid(row=i, column=self.countBlank)
                self.countBlank += 1
            self.ViewOverviewPageContents = False
        # Placing The main Page on the grid as default
        self.FmePage1ViewOverview.grid(column=0, row=0, columnspan=3)

    # Function to create the table
    def ViewOverviewTable(self):

        # Creating List
        self.count = 0
        if len(self.cards) < 1:
            while self.count < 24:
                self.VarCardT = StringVar()
                self.VarCardT.set(('term' + str(self.count)))

                self.VarCardD = StringVar()
                self.VarCardD.set(('def' + str(self.count)))

                self.VarCardI = StringVar()
                self.VarCardI.set(('IMG' + str(self.count)))

                self.cards.append([self.VarCardT, self.VarCardD, self.VarCardI])
                self.count += 1

        # Defining a temporary variable to store the number of card for determining table size
        self.noCards = (len(self.cards) * 2) + 3

        # Creating the scroll bar through a frame in a canvas in a frame
        def CanvasConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=490, height=600)

        self.FmeSbTop = Frame(self.FmePage1ViewOverview)
        self.FmeSbTop.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)
        self.canvas = Canvas(self.FmeSbTop)
        self.FmeSbSub = Frame(self.canvas, width=530, height=600)
        self.ScrollBar = Scrollbar(self.FmeSbTop, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ScrollBar.set)
        self.ScrollBar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0, 0), window=self.FmeSbSub, anchor='nw')
        self.FmeSbSub.bind('<Configure>', CanvasConfig)

        # Creating the View Frame
        self.FmeTableView = Frame(self.FmeSbSub)
        # Grid line is below as it uses a variable to determine rowspan

        # Header for 'Term' Column
        self.LblTermHeader = Label(self.FmeTableView, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Header for 'Definition' Column
        self.LblDefHeader = Label(self.FmeTableView, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Header for 'Image' Column
        self.LblImgHeader = Label(self.FmeTableView, text='Image Directory', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 17, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)

        # Creating a list of dummy data to appear in form:
        # [['term1', 'def1', 'img1'], ['term2', 'def2', 'img2'], ['term3', 'def3', 'img3'],
        #              ['term4', 'def5', 'img6'], ['term7', 'def7', 'img7'], ['term8', 'def8', 'img8']
        #         , ['term9', 'def9', 'img9'], ['term10', 'def10', 'img10'], ['term11', 'def11', 'img11']]

        # Placing the table in the grid so it appears by default
        self.FmeTableView.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)

        # Setting the content for the 'Term' Column
        self.count = 0
        for i in range(2, self.noCards):
            if (i % 2) == 1:
                self.VarCurrentTerm = StringVar()
                self.VarCurrentTerm.set(self.cards[self.count][0].get())
                self.LblTerm = Label(self.FmeTableView, textvariable=self.VarCurrentTerm, anchor='w', width=12,
                                     height=3)
                self.LblTerm.config(font=('Times', 14))
                self.LblTerm.grid(row=i, column=1)
                self.count += 1

        # Setting the content for the 'Definition' Column
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

        # Setting border around table
        self.border = []
        for i in range(0, self.noCards):
            for j in range(0, 7):
                # Even row and column = 0, 2, 4, 6 (even)
                if (i % 2) == 0 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (term)
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableView, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 3 (def)
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableView, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (img)
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableView, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableView, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

        # Edit Table

        # Creating the frame
        self.FmeTableEdit = Frame(self.FmeSbSub)

        # Header for 'Term' Column
        self.LblTermHeader = Label(self.FmeTableEdit, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Header for 'Definition' Column
        self.LblDefHeader = Label(self.FmeTableEdit, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Header for 'Image' Column
        self.LblImgHeader = Label(self.FmeTableEdit, text='Image', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 18, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)

        # Defining a temporary variable to store the number of card for determining table size
        self.noCards = (len(self.cards) * 2) + 3

        # Creating the entry fields

        self.count = 0
        self.LstEditCards = []

        for i in range(2, self.noCards):
            self.LstEditCardsSub = []

            if (i % 2) == 1:
                # Setting the content for the 'Term' Column
                self.VarCurrentTerm = StringVar()
                self.VarCurrentTerm.set(self.cards[self.count][0].get())
                self.EntTerm = Entry(self.FmeTableEdit, textvariable=self.VarCurrentTerm, width=12)
                self.LstEditCardsSub.append(self.VarCurrentTerm)
                self.EntTerm.config(font=('Times', 14))
                self.EntTerm.grid(row=i, column=1)

                # Setting the content for the 'Definition' Column
                self.VarCurrentDef = StringVar()
                self.VarCurrentDef.set(self.cards[self.count][1].get())
                self.EntDef = Entry(self.FmeTableEdit, textvariable=self.VarCurrentDef, width=22)
                self.LstEditCardsSub.append(self.VarCurrentDef)
                self.EntDef.config(font=('Times', 14))
                self.EntDef.grid(row=i, column=3)

                # Setting the content for the 'Image' Column
                self.VarCurrentImg = StringVar()
                self.VarCurrentImg.set(self.cards[self.count][2].get())
                self.EntImg = Entry(self.FmeTableEdit, textvariable=self.VarCurrentImg, width=12)
                self.LstEditCardsSub.append(self.VarCurrentImg)
                self.EntImg.config(font=('Times', 14))
                self.EntImg.grid(row=i, column=5)

                self.count += 1
                self.LstEditCards.append(self.LstEditCardsSub)

        # Setting border around table
        self.border = []
        for i in range(0, self.noCards):
            for j in range(0, 7):
                # Even row and column = 0, 2, 4, 6 (even)
                if (i % 2) == 0 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableEdit, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (term)
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableEdit, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 3 (def)
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableEdit, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (img)
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableEdit, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableEdit, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableEdit, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

    # Function to change the currently viewed set   CLI Merge
    def ViewOverviewSelect(self):
        print('Select Clicked')
        wantedSet = self.VarSelectInput.get()
        print('self.VarSelectInput =', wantedSet)
        # Ready to merge with CLI

    # Function for the ViewOverview Page to change to table from label to entry
    #                                               WIP
    def ViewOverviewEditSaveBtn(self):
        #     # WIP changes are not saved
        status = self.VarEditSaveBtnBool.get()
        # If in view mode change to edit mode and change text
        if status == 0:
            status = 1
            # Remove the view table
            self.FmeTableView.grid_remove()

            # Code to place the edit version of the table in the grid
            self.FmeTableEdit.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)

            self.VarEditSaveBtnText.set('View Set')

        # If in edit mode change to view mode and change text
        elif status == 1:
            status = 0

            self.LstNew = []
            for i in self.LstEditCards:
                self.LstNewSub = []
                for j in i:
                    x = j.get()
                    if x != '':
                        self.LstNewSub.append(x)
                    else:
                        messagebox.showinfo('Saving', 'Changes could not be saved as there was a blank space.')
                        # Aborts the function
                        return
                self.LstNew.append(self.LstNewSub)

            # Rewriting self.LstCards but each string is a StringVar()
            self.LstNew2 = []
            for i in self.LstNew:
                self.LstNew2Sub = []
                for j in i:
                    index = StringVar()
                    index.set(j)
                    self.LstNew2Sub.append(index)
                self.LstNew2.append(self.LstNew2Sub)

            self.cards = self.LstNew2

            # Removes the edit table
            self.FmeTableEdit.grid_remove()

            self.ViewOverviewTable()

            # Code to place the view version of the table in the grid
            self.FmeTableView.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)

            self.VarEditSaveBtnText.set('Edit Set')
        self.VarEditSaveBtnBool.set(status)


    # Function for the Create Page                  PAGE FUNCTION
    def CreatePage(self, master):
        # Removing the frame containing ViewOverviewPage
        self.FmePage1ViewOverview.grid_remove()

        # Creating the frame to store the contents of Create Page grid line at bottom of function
        self.FmePage2CreateSet = Frame(master)

        # Widget 1
        self.VarName = StringVar()
        self.VarName.set('Name of Set')
        self.EntName = Entry(self.FmePage2CreateSet, textvariable=self.VarName, width=24, bg='Orange')
        self.EntName.config(font=('Arail', 32, 'bold underline'))
        self.EntName.grid(row=0,column=0,rowspan=2,columnspan=4)

        # Widget 4:     Add row to bottom of table
        self.BtnAddRow = Button(self.FmePage2CreateSet, text='Add Row', width=16, command=lambda *args: self.CreateChangeRow(self.VarTableRowSpan, 0))
        self.BtnAddRow.config(font=('Times', 16))
        self.BtnAddRow.grid(row=4, column=5, rowspan=1, columnspan=1)

        # Widget 5:     Remove row from bottom of tabxle
        self.BtnRemoveRow = Button(self.FmePage2CreateSet, text='Remove Row', width=16, command=lambda *args: self.CreateChangeRow(self.VarTableRowSpan, 1))
        self.BtnRemoveRow.config(font=('Times', 16))
        self.BtnRemoveRow.grid(row=6, column=5, rowspan=1, columnspan=1)

        # Widget 2
        # Variable to determine the number of rows in the table. Can be changed with buttons
        # VarTableRowSpan = (number of cards * 2) + 3
        # Num cards = 9
        self.VarTableRowSpan = IntVar()
        self.VarTableRowSpan = (17 * 2) + 3
        self.LstCardsCreate = []
        self.CreateTable()

        # Widget 3
        self.BtnSave = Button(self.FmePage2CreateSet, text='Save Set', width=16, command=self.CreateSave)
        self.BtnSave.config(font=('Times', 16))
        self.BtnSave.grid(row=1, column=5, rowspan=1, columnspan=1)

        # Widget 5
        self.BtnDelete = Button(self.FmePage2CreateSet, text='Delete Set', width=16, command=self.CreateDelete)
        self.BtnDelete.config(font=('Times', 16))
        self.BtnDelete.grid(row=8, column=5, rowspan=1, columnspan=1)

        # Widget 6
        self.BtnImport = Button(self.FmePage2CreateSet, text='Import Set', width=16, command=self.CreateImport)
        self.BtnImport.config(font=('Times', 16))
        self.BtnImport.grid(row=10, column=5, rowspan=1, columnspan=1)

        # Widget 7
        self.BtnHelp = Button(self.FmePage2CreateSet, text='Help', width=16, command=self.HelpPage)
        self.BtnHelp.config(font=('Times', 16))
        self.BtnHelp.grid(row=12, column=5, rowspan=1, columnspan=1)

        # Blank Spaces

        blanks = [[2,3,4,5,6,7,8,9], [2], [2], [2], [0,1,2,3,4,5,6,7,8,9,11], [0,3,5,7,9,11], [0,3,5,7,9,11]]
        self.countBlank = 0
        while self.countBlank < 7:
            for i in blanks[self.countBlank]:
                self.LblBlank = Label(self.FmePage2CreateSet, height=1, width=8)
                self.LblBlank.config(font=('Arial', 10))
                # self.LblBlank = Label(self.FmePage1ViewOverview, height=1, width=8)
                self.LblBlank.grid(row=i, column=self.countBlank)
            self.countBlank += 1

        self.FmePage2CreateSet.grid(row=0,column=0)

    # Function to create the table
    def CreateTable(self):

        # Creating List
        self.count = 0
        if len(self.LstCardsCreate) < 1:
            while self.count < 24:
                self.VarCardT = StringVar()
                self.VarCardT.set(('Enter Term ' + str(self.count)))

                self.VarCardD = StringVar()
                self.VarCardD.set(('Enter Definition ' + str(self.count)))

                self.VarCardI = StringVar()
                self.VarCardI.set(('Enter Image Directory ' + str(self.count)))

                self.LstCardsCreate.append([self.VarCardT, self.VarCardD, self.VarCardI])
                self.count += 1

        # Creating the scroll bar through a frame in a canvas in a frame
        def CanvasConfig(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=490, height=600)
        self.FmeSbTop = Frame(self.FmePage2CreateSet)
        self.FmeSbTop.grid(row=3, column=1, rowspan=self.VarTableRowSpan, columnspan=3)
        self.canvas = Canvas(self.FmeSbTop)
        self.FmeSbSub = Frame(self.canvas, width=100, height=600)
        self.ScrollBar = Scrollbar(self.FmeSbTop, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ScrollBar.set)
        self.ScrollBar.pack(side='right', fill='y')
        self.canvas.pack(side='left')
        self.canvas.create_window((0, 0), window=self.FmeSbSub, anchor='nw')
        self.FmeSbSub.bind('<Configure>', CanvasConfig)

        # Frame to contain table
        self.FmeTableCreate = Frame(self.FmeSbSub)
        self.FmeTableCreate.grid(row=3, column=1, rowspan=self.VarTableRowSpan, columnspan=3)


        # Header for 'Term' Column
        self.LblTermHeader = Label(self.FmeTableCreate, text='Term', width=12, height=1)
        self.LblTermHeader.config(font=('Times', 18, 'underline'))
        self.LblTermHeader.grid(row=1, column=1)

        # Header for 'Definition' Column
        self.LblDefHeader = Label(self.FmeTableCreate, text='Definition', width=22, height=1)
        self.LblDefHeader.config(font=('Times', 18, 'underline'))
        self.LblDefHeader.grid(row=1, column=3)

        # Header for 'Image' Column
        self.LblImgHeader = Label(self.FmeTableCreate, text='Image Directory', width=12, height=1)
        self.LblImgHeader.config(font=('Times', 17, 'underline'))
        self.LblImgHeader.grid(row=1, column=5)


        # Setting Entry Fields

        # Setting the content for the 'Term' Column
        self.count = 0
        for i in range(2, self.VarTableRowSpan):
            self.LstCardsSub =[]
            if (i % 2) == 1:
                # Setting the content for the 'Term' Column
                self.VarCurrentTerm = StringVar()
                self.VarCurrentTerm.set(self.LstCardsCreate[self.count][0].get())
                self.EntTerm = Entry(self.FmeTableCreate, textvariable=self.VarCurrentTerm, width=12)
                self.LstCardsSub.append(self.VarCurrentTerm)
                self.EntTerm.config(font=('Times', 16))
                self.EntTerm.grid(row=i, column=1)

                # Setting the content for the 'Definition' Column
                self.VarCurrentDef = StringVar()
                self.VarCurrentDef.set(self.LstCardsCreate[self.count][1].get())
                self.EntDef = Entry(self.FmeTableCreate, textvariable=self.VarCurrentDef, width=22)
                self.LstCardsSub.append(self.VarCurrentDef)
                self.EntDef.config(font=('Times', 16))
                self.EntDef.grid(row=i, column=3)

                # Setting the content for the 'Image' Column
                self.VarCurrentImg = StringVar()
                self.VarCurrentImg.set(self.LstCardsCreate[self.count][2].get())
                self.EntImg = Entry(self.FmeTableCreate, textvariable=self.VarCurrentImg, width=12)
                self.LstCardsSub.append(self.VarCurrentImg)
                self.EntImg.config(font=('Times', 16))
                self.EntImg.grid(row=i, column=5)

                self.count += 1
                self.LstCardsCreate.append(self.LstCardsSub)

        # Border
        self.border = []
        for i in range(0, self.VarTableRowSpan):
            for j in range(0, 7):
                # Even row and column = 0, 2, 4, 6 (even)
                if (i % 2) == 0 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableCreate, width=1, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (term)
                elif (i % 2) == 0 and j == 1:
                    self.LblBorder = Label(self.FmeTableCreate, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 3 (def)
                elif (i % 2) == 0 and j == 3:
                    self.LblBorder = Label(self.FmeTableCreate, width=22, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                # Even row and column = 1 (img)
                elif (i % 2) == 0 and j == 5:
                    self.LblBorder = Label(self.FmeTableCreate, width=12, height=1, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0 and i != 1:
                    self.LblBorder = Label(self.FmeTableCreate, width=1, height=3, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.LblBorder = Label(self.FmeTableCreate, width=1, height=2, bg='grey')
                    self.LblBorder.grid(row=i, column=j)
                    self.border.append(self.LblBorder)

    # Function to save the set that has just been made and change the screen back to ViewOverview
    #                                               CLI MERGE
    def CreateSave(self):
            self.LstNew = []
            for i in self.LstCardsCreate:
                self.LstNewSub = []
                for j in i:
                    x = j.get()
                    if x != '':
                        self.LstNewSub.append(x)
                    else:
                        messagebox.showinfo('Saving', 'Set could not saved as there was a blank space.')
                        return
                self.LstNew.append(self.LstNewSub)
            messagebox.showinfo('Saving', 'Set Saved Successfully.')
            # Output is listCard from design and is ready to be merged with CLI

            # Removing the frame containing everything from the create page
            self.FmePage2CreateSet.grid_remove()
            self.ViewOverviewPage(self.master)

    # Function to change the amount of rows in the table      WIP
    def CreateChangeRow(self, numRow, change):
        print('Change Row Function Ran')
        # Does so by incrementing the variable by +2 (+2 because there needs to be a border row)
        # WIP can't get the change to carry through to Create function
        print('\nchange =', change)
        # If the function ran from the 'Add Row' Button, increase the row variable
        if change == 0:
            numRow += 2
        # If the function ran from the 'Remove Row' Button, decrease the row variable
        elif change == 1:
            numRow -= 2

        # Reading the table to rewrite it into the file
        self.LstNew = []
        for i in self.LstCardsCreate:
            self.LstNewSub = []
            for j in i:
                x = j.get()
                self.LstNewSub.append(x)
            self.LstNew.append(self.LstNewSub)

        self.LstNew2 = []
        for i in self.LstNew:
            self.LstNew2Sub = []
            for j in i:
                index = StringVar()
                index.set(j)
                self.LstNew2Sub.append(index)
            self.LstNew2.append(self.LstNew2Sub)
        self.cards = self.LstNew2

        numRow = int(numRow)
        self.VarTableRowSpan = numRow
        self.CreateTable()

    # Function to delete the set being made         COMPLETE
    def CreateDelete(self):
        self.message = 'Are you sure you want to delete this set?\nThis will return you to the Start-up screen and ' \
                       'progress will be lost.\nThis can not be undone.'
        self.VarContinue = messagebox.askokcancel(title='Delete', message=self.message, )
        if self.VarContinue:
            self.FmePage2CreateSet.grid_remove()
            self.ViewOverviewPage(self.master)
            return
        elif not self.VarContinue:
            messagebox.showinfo(title='Delete', message='Delete Cancelled')
        else:
            print('Error self.VarContinue != True or False')
            print('self.VarContinue =', self.VarContinue)

    # Function to import a set                      CLI Merge
    def CreateImport(self):
        self.ImportPageContents = True
        while self.ImportPageContents:
            self.WinImport = Toplevel(root)
            self.WinImport.title('Import')

            self.FmeImportPage = Frame(self.WinImport)
            self.FmeImportPage.grid()

            self.LblImTitle = Label(self.FmeImportPage, text='Import Set', bg='Orange', width=30, height=1)
            self.LblImTitle.config(font=('Arail', 28, 'underline'))
            self.LblImTitle.grid(row=0,column=0,rowspan=1,columnspan=2)

            self.LblImPrompt = Label(self.FmeImportPage, text='Directory of Import File:')
            self.LblImPrompt.config(font=('Times', 16))
            self.LblImPrompt.grid(row=1,column=0,rowspan=1,columnspan=1)

            self.VarDirectory = StringVar()
            self.EntImDir = Entry(self.FmeImportPage, textvariable=self.VarDirectory, width=20)
            self.EntImDir.config(font=('Times', 16))
            self.EntImDir.grid(row=1,column=1,rowspan=1,columnspan=1)

            self.BtnImImport = Button(self.FmeImportPage, text='Import File', width=40, command=lambda *args: ImImport(self, self.VarDirectory))
            self.BtnImImport.config(font=('Times', 16))
            self.BtnImImport.grid(row=2,column=0,rowspan=1,columnspan=2)

            self.VarImTxt = StringVar()
            self.VarImTxt.set('Imported sets must be a CSV (Comma Separated Value) file in the following form;\n'
                     'term,definition,img_directory\nterm,definition,img_directory\n... , ... , ...\nWhere each line '
                     'represents a different card.')
            self.LblImTxt = Label(self.FmeImportPage, textvariable=self.VarImTxt, anchor=NW)
            self.LblImTxt.config(font=('Times', 16))
            self.LblImTxt.grid(row=3,column=0,rowspan=1,columnspan=2)

            self.BtnImExit = Button(self.FmeImportPage, text='Cancel Import', command=self.WinImport.destroy)
            self.BtnImExit.config(font=('Times', 16))
            self.BtnImExit.grid(row=4,column=1,rowspan=1,columnspan=1)

            self.LblBlank = Label(self.FmeImportPage, width=14, height=1)
            self.LblBlank.grid(row=4, column=0,rowspan=1,columnspan=1)

            self.ImportPageContents = False

        # Function to be merged with CLI
        def ImImport(self, directory):
            print('SUB FUNCTION')

    # Function for the Help Page                    Text
    def HelpPage(self):
        # Contains a sub function
        # Needs text which will be added last after final changed
        self.HelpPageContents = True
        while self.HelpPageContents:
            self.WinHelp = Toplevel(root)
            self.WinHelp.title('Help')

            self.FmeHelpPage = Frame(self.WinHelp)
            self.FmeHelpPage.grid()

            self.LblHpTitle = Label(self.FmeHelpPage, text='Help', bg='Orange', width=35, height=1)
            self.LblHpTitle.config(font=('Arail', 52, 'bold underline'))
            self.LblHpTitle.grid(row=0, column=0, rowspan=1, columnspan=9)

            self.LblHpInstructions = Label(self.FmeHelpPage, text='Select the Button that'
                                                                  'corresponding to the area you need help with.')
            self.LblHpInstructions.config(font=('Times', 18))
            self.LblHpInstructions.grid(row=1, column=0, columnspan=9)

            self.BtnHp1Navigation = Button(self.FmeHelpPage, text='General Use', width=10, command=lambda *args: HpText(self, 1))
            self.BtnHp1Navigation.config(font=('Times', 16))
            self.BtnHp1Navigation.grid(row=2, column=0, rowspan=1, columnspan=1)

            self.BtnHp2Creating = Button(self.FmeHelpPage, text='Creating Sets', command=lambda *args: HpText(self, 2))
            self.BtnHp2Creating.config(font=('Times', 16))
            self.BtnHp2Creating.grid(row=2, column=1)

            self.BtnHp3Editing = Button(self.FmeHelpPage, text='Editing Sets', command=lambda *args: HpText(self, 3))
            self.BtnHp3Editing.config(font=('Times', 16))
            self.BtnHp3Editing.grid(row=2, column=2)

            self.BtnHp4Select = Button(self.FmeHelpPage, text='Selecting Different Sets', command=lambda *args: HpText(self, 4))
            self.BtnHp4Select.config(font=('Times', 16))
            self.BtnHp4Select.grid(row=2, column=3)

            self.BtnHp5ViewOverview = Button(self.FmeHelpPage, text='Viewing an Overview of a Set',
                                             command=lambda *args: HpText(self, 5))
            self.BtnHp5ViewOverview.config(font=('Times', 16))
            self.BtnHp5ViewOverview.grid(row=2, column=4)

            self.BtnHp6Viewing = Button(self.FmeHelpPage, text='Viewing Sets',
                                        command=lambda *args: HpText(self, 6))
            self.BtnHp6Viewing.config(font=('Times', 16))
            self.BtnHp6Viewing.grid(row=2, column=5)

            self.BtnHp7DeletingSets = Button(self.FmeHelpPage, text='Deleting Sets',
                                             command=lambda *args: HpText(self, 7))
            self.BtnHp7DeletingSets.config(font=('Times', 16))
            self.BtnHp7DeletingSets.grid(row=2, column=6)

            self.BtnHp8ImportExport = Button(self.FmeHelpPage, text='Importing and Exporting Sets',
                                             command=lambda *args: HpText(self, 8))
            self.BtnHp8ImportExport.config(font=('Times', 16))
            self.BtnHp8ImportExport.grid(row=2, column=7)

            self.BtnHp9ExitHelp = Button(self.FmeHelpPage, text='Exit Help', command=self.WinHelp.destroy)
            self.BtnHp9ExitHelp.config(font=('Times', 16))
            self.BtnHp9ExitHelp.grid(row=2, column=8)

            self.VarHpText = StringVar()
            self.VarHpText.set('\n\n\n\n\n\n\n\n\n\n')

            self.LblHpText = Label(self.FmeHelpPage, textvariable=self.VarHpText, width=155, height=10, anchor=NW)
            self.LblHpText.config(font=('Times', 14))
            self.LblHpText.grid(row=3, column=0, rowspan=10, columnspan=9)

            self.HelpPageContents = False

        # Function to desplay the correct text
        def HpText(self, input):
            text = self.VarHpText.get()
            input = int(input)
            if input == 1:
                text=('This is the help information for navigating the program. It spans 10 lines and has a max width '
                      'of 35 characters.\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10')
            elif input == 2:
                text=('This is the help information for Creating sets. It spans 10 lines and has a max width of 35 '
                      'characters.\nline2\nline3\nline4\nline5\nline6\nline7\nline8\nline9\nline10')
            elif input == 3:
                text=('Button 3')
            elif input == 4:
                text=('Button 4')
            elif input == 5:
                text=('Button 5')
            elif input == 6:
                text=('Button 6')
            elif input == 7:
                text=('Button 7')
            elif input == 8:
                text=('Button 8')
            self.VarHpText.set(text)



        # Will create a label to store all of the text and the text will be a variable that
        # changed is a button is pressed. By default the label will be blank but have space for text in window by having
        # hard coded width and height.

root = Tk()
root.geometry('1000x800')
my_gui = GUI(root)
root.mainloop()
