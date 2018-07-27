from tkinter import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title('Flash Card')

        self.ViewOverviewPageContents = True
        while self.ViewOverviewPageContents:
            self.FmePage1ViewSet = Frame(master)

            # Widget 1
            self.LblSet = Label(self.FmePage1ViewSet, text='setName', bg='orange', width=32)
            self.LblSet.config(font=('Arial', 32, 'bold underline'))
            self.LblSet.grid(row=0, column=0, rowspan=1, columnspan=4)

            # Widget 4
            self.VarEditSaveBtnBool = IntVar()
            self.VarEditSaveBtnBool.set(0)
            self.VarEditSaveBtnText = StringVar()
            self.VarEditSaveBtnText.set('Edit Set')
            self.BtnEditSave = Button(self.FmePage1ViewSet, textvariable=self.VarEditSaveBtnText, width=24, command=self.EditSaveBtn)
            self.BtnEditSave.config(font=('Times', 16))
            self.BtnEditSave.grid(row=2, column=5, rowspan=1, columnspan=3)


            # Widget 2

            self.count = 0
            self.cards = []
            while self.count < 12:
                self.VarCardT = StringVar()
                self.VarCardT = ('term' + str(self.count))

                self.VarCardD = StringVar()
                self.VarCardD = ('def' + str(self.count))

                self.VarCardI = StringVar()
                self.VarCardI = ('IMG' + str(self.count))

                self.cards.append([self.VarCardT, self.VarCardD, self.VarCardI])
                self.count += 1

            # Defining a temporary variable to store the number of card for determining table size
            self.noCards = (len(self.cards) * 2) + 3

            # Creating the View Frame
            self.FmeTableView = Frame(self.FmePage1ViewSet)
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
            self.LblImgHeader = Label(self.FmeTableView, text='Image', width=12, height=1)
            self.LblImgHeader.config(font=('Times', 18, 'underline'))
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
                    self.LblTerm = Label(self.FmeTableView, text=self.cards[self.count][0], anchor='w', width=12, height=3)
                    self.LblTerm.config(font=('Times', 14))
                    self.LblTerm.grid(row=i, column=1)
                    self.count += 1

            # Setting the content for the 'Definition' Column
            self.count = 0
            for i in range(2, self.noCards):
                if (i % 2) == 1:
                    self.LblDef = Label(self.FmeTableView, text=self.cards[self.count][1], anchor='w', width=22, height=3)
                    self.LblDef.config(font=('Times', 14))
                    self.LblDef.grid(row=i, column=3)
                    self.count += 1

            # Setting the content for the 'Image' Column
            self.count = 0
            for i in range(2, self.noCards):
                if (i % 2) == 1:
                    self.LblImg = Label(self.FmeTableView, text=self.cards[self.count][2], anchor='w', width=12, height=3)
                    self.LblImg.config(font=('Times', 14))
                    self.LblImg.grid(row=i, column=5)
                    self.count += 1

            # Setting border around table
            self.border = []
            for i in range(0, self.noCards):
                for j in range(0,7):
                    # Even row and column = 0, 2, 4, 6 (even)
                    if (i % 2) == 0 and (j % 2) == 0:
                        self.LblBorder = Label(self.FmeTableView, width=1, height=1, bg='grey')
                        self.LblBorder.grid(row=i,column=j)
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
            self.FmeTableEdit = Frame(self.FmePage1ViewSet)

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

            # Setting the content for the 'Term' Column
            self.count = 0
            self.LstEditCards = []
            for i in range(2, self.noCards):
                if (i % 2) == 1:
                    self.VarCurrentTerm = StringVar()
                    self.VarCurrentTerm.set(self.cards[self.count][0])
                    self.EntTerm = Entry(self.FmeTableEdit, textvariable=self.VarCurrentTerm, width=12)
                    self.LstEditCards.append([self.VarCurrentTerm])
                    self.EntTerm.config(font=('Times', 14))
                    self.EntTerm.grid(row=i, column=1)
                    self.count += 1

            # Setting the content for the 'Definition' Column
            self.count = 0
            for i in range(2, self.noCards):
                if (i % 2) == 1:
                    self.VarCurrentDef = StringVar()
                    self.VarCurrentDef.set(self.cards[self.count][1])
                    self.EntDef = Entry(self.FmeTableEdit, textvariable=self.VarCurrentDef, width=22)
                    self.LstEditCards[self.count].append([self.VarCurrentDef])
                    self.EntDef.config(font=('Times', 14))
                    self.EntDef.grid(row=i, column=3)
                    self.count += 1

            # Setting the content for the 'Image' Column
            self.count = 0
            for i in range(2, self.noCards):
                if (i % 2) == 1:
                    self.VarCurrentImg = StringVar()
                    self.VarCurrentImg.set(self.cards[self.count][2])
                    self.EntImg = Entry(self.FmeTableEdit, textvariable=self.VarCurrentImg, width=12)
                    self.LstEditCards[self.count].append([self.VarCurrentImg])
                    self.EntImg.config(font=('Times', 14))
                    self.EntImg.grid(row=i, column=5)
                    self.count += 1




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


            # Widget 3
            self.BtnCreate = Button(self.FmePage1ViewSet, text='Create Set', width=24)
            self.BtnCreate.config(font=('Times', 16))
            self.BtnCreate.grid(row=0, column=5, rowspan=1, columnspan=3)


            # Widget 5

            # Need to change to entry field and a button for a search, this will allow for the use of a search function
            # Row = 3, column = 5       Rowspan =1,     Rowspan = 3
            self.VarSelectInput = StringVar()
            self.VarSelectInput.set('Enter the Name of the Set you Wish to Change to then click Select.')
            self.EntSelect = Entry(self.FmePage1ViewSet, textvariable=self.VarSelectInput, width=20)
            self.EntSelect.config(font=('Times', 12))
            self.EntSelect.grid(row=3, column=5, rowspan=1, columnspan=2)

            self.BtnSelect = Button(self.FmePage1ViewSet, text='Select', width=8, command=self.Select)
            self.BtnSelect.config(font=('Times', 16))
            self.BtnSelect.grid(row=3, column=7, rowspan=1, columnspan=1)


            # Widget 6

            # Creating the Frame
            self.FmeOptions = Frame(self.FmePage1ViewSet)
            self.FmeOptions.grid(row=4, column=5, columnspan=3, rowspan=5)

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
            self.BtnView = Button(self.FmePage1ViewSet, text='View Set', width=24)
            self.BtnView.config(font=('Times', 16))
            self.BtnView.grid(row=9, column=5, rowspan=1, columnspan=3)

            # Widget 8
            self.BtnDelete = Button(self.FmePage1ViewSet, text='Delete Set')
            self.BtnView.config(font=('Times', 16))
            self.BtnDelete.grid(row=11, column=5, rowspan=1)

            # Widget 9
            self.BtnHelp = Button(self.FmePage1ViewSet, text='Help', width=8, command=self.Help)
            self.BtnHelp.config(font=('Times', 16))
            self.BtnHelp.grid(row=11, column=7, rowspan=1)

            # Blank Spaces

            blanks = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
             [1, 10], [1, 11], [1, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
            self.countBlank = 0
            while self.countBlank < 9:
                for i in blanks[self.countBlank]:
                    self.LblBlank = Label(self.FmePage1ViewSet, height=1, width=8, bg='green', text='abc')
                    self.LblBlank.config(font=('Arial', 10))
                    # self.LblBlank = Label(self.FmePage1ViewSet, height=1, width=8)
                    self.LblBlank.grid(row=i, column=self.countBlank)
                self.countBlank += 1
            self.ViewOverviewPageContents = False

        self.HelpPageContents = False
        while self.HelpPageContents:
            print('HelpPage While Loop in Class Ran')
            self.WinHelp = Toplevel(master)
            self.WinHelp.title('Help')

            self.FmeHelpPage = Frame(self.WinHelp)
            self.FmeHelpPage.grid()

            self.LblHpTitle = Label(self.FmeHelpPage, text='Help', bg='Orange', width=35, height=2)
            self.LblHpTitle.config(font=('Arail', 52, 'bold underline'))
            self.LblHpTitle.grid(row=0, column=0, rowspan=1, columnspan=9)

            self.LblHpInstructions = Label(self.FmeHelpPage, text='Select the Button that'
                                    'corresponding to the area you need help with.')
            self.LblHpInstructions.config(font=('Times', 18))
            self.LblHpInstructions.grid(row=1, column=0, columnspan=9)

            self.BtnHp1MainMenu = Button(self.FmeHelpPage, text='Main Menu', width=10)
            self.BtnHp1MainMenu.config(font=('Times', 16))
            self.BtnHp1MainMenu.grid(row=2, column=0, rowspan=1, columnspan=1)

            self.BtnHp2Creating = Button(self.FmeHelpPage, text='Creating Sets')
            self.BtnHp2Creating.config(font=('Times', 16))
            self.BtnHp2Creating.grid(row=2,column=1)

            self.BtnHp3Editing = Button(self.FmeHelpPage, text='Editing Sets')
            self.BtnHp3Editing.config(font=('Times', 16))
            self.BtnHp3Editing.grid(row=2, column=2)

            self.BtnHp4Select = Button(self.FmeHelpPage, text='Selecting Different Sets')
            self.BtnHp4Select.config(font=('Times', 16))
            self.BtnHp4Select.grid(row=2, column=3)

            self.BtnHp5ViewOverview = Button(self.FmeHelpPage, text='Viewing an Overview of a Set')
            self.BtnHp5ViewOverview.config(font=('Times', 16))
            self.BtnHp5ViewOverview.grid(row=2, column=4)

            self.BtnHp6Viewing = Button(self.FmeHelpPage, text='Viewing Sets')
            self.BtnHp6Viewing.config(font=('Times', 16))
            self.BtnHp6Viewing.grid(row=2, column=5)

            self.BtnHp7DeletingSets = Button(self.FmeHelpPage, text='Deleting Sets')
            self.BtnHp7DeletingSets.config(font=('Times', 16))
            self.BtnHp7DeletingSets.grid(row=2, column=6)

            self.BtnHp8ImportExport = Button(self.FmeHelpPage, text='Importing and Exporting Sets')
            self.BtnHp8ImportExport.config(font=('Times', 16))
            self.BtnHp8ImportExport.grid(row=2, column=7)

            self.BtnHp9ExitHelp = Button(self.FmeHelpPage, text='Exit Help', command=self.WinHelp.quit())
            self.BtnHp9ExitHelp.config(font=('Times', 16))
            self.BtnHp9ExitHelp.grid(row=2, column=8)

            self.HelpPageContents = False

        # Placing The main Page on the grid as default
        self.FmePage1ViewSet.grid(column=0, row=0, columnspan=3)


    def EditSaveBtn(self):
        print('EditSaveBtn Function Ran')
        status = self.VarEditSaveBtnBool.get()
        print('\nView/Edit Button Clicked')
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

            print('self.LstEditCards =', self.LstEditCards, '\n')

            self.NewI = []
            self.NewJ = []
            for i in self.LstEditCards:
                for j in i:

                    self.NewJ.append(j)
                self.NewI.append(self.NewJ)
            print('self.NewJ =', self.NewJ, '\n')


            # Removes the edit table
            self.FmeTableEdit.grid_remove()

            # Code to place the view version of the table in the grid
            self.FmeTableView.grid(row=2, column=1, rowspan=(len(self.cards) * 3) + (len(self.cards)) + 3, columnspan=3)

            self.VarEditSaveBtnText.set('Edit Set')
        self.VarEditSaveBtnBool.set(status)
        return

    def Select(self):
        print('Select Clicked')
        wantedSet = self.VarSelectInput.get()

        print('self.VarSelectInput =', wantedSet)

    def Help(self):
        print('Help Function Ran')
        self.HelpPageContents = True
        while self.HelpPageContents:
            self.WinHelp = Toplevel(root)
            self.WinHelp.title('Help')

            self.FmeHelpPage = Frame(self.WinHelp)
            self.FmeHelpPage.grid()

            self.LblHpTitle = Label(self.FmeHelpPage, text='Help', bg='Orange', width=35, height=2)
            self.LblHpTitle.config(font=('Arail', 52, 'bold underline'))
            self.LblHpTitle.grid(row=0, column=0, rowspan=1, columnspan=9)

            self.LblHpInstructions = Label(self.FmeHelpPage, text='Select the Button that'
                                                                  'corresponding to the area you need help with.')
            self.LblHpInstructions.config(font=('Times', 18))
            self.LblHpInstructions.grid(row=1, column=0, columnspan=9)

            self.BtnHp1MainMenu = Button(self.FmeHelpPage, text='Main Menu', width=10)
            self.BtnHp1MainMenu.config(font=('Times', 16))
            self.BtnHp1MainMenu.grid(row=2, column=0, rowspan=1, columnspan=1)

            self.BtnHp2Creating = Button(self.FmeHelpPage, text='Creating Sets')
            self.BtnHp2Creating.config(font=('Times', 16))
            self.BtnHp2Creating.grid(row=2, column=1)

            self.BtnHp3Editing = Button(self.FmeHelpPage, text='Editing Sets')
            self.BtnHp3Editing.config(font=('Times', 16))
            self.BtnHp3Editing.grid(row=2, column=2)

            self.BtnHp4Select = Button(self.FmeHelpPage, text='Selecting Different Sets')
            self.BtnHp4Select.config(font=('Times', 16))
            self.BtnHp4Select.grid(row=2, column=3)

            self.BtnHp5ViewOverview = Button(self.FmeHelpPage, text='Viewing an Overview of a Set')
            self.BtnHp5ViewOverview.config(font=('Times', 16))
            self.BtnHp5ViewOverview.grid(row=2, column=4)

            self.BtnHp6Viewing = Button(self.FmeHelpPage, text='Viewing Sets')
            self.BtnHp6Viewing.config(font=('Times', 16))
            self.BtnHp6Viewing.grid(row=2, column=5)

            self.BtnHp7DeletingSets = Button(self.FmeHelpPage, text='Deleting Sets')
            self.BtnHp7DeletingSets.config(font=('Times', 16))
            self.BtnHp7DeletingSets.grid(row=2, column=6)

            self.BtnHp8ImportExport = Button(self.FmeHelpPage, text='Importing and Exporting Sets')
            self.BtnHp8ImportExport.config(font=('Times', 16))
            self.BtnHp8ImportExport.grid(row=2, column=7)

            self.BtnHp9ExitHelp = Button(self.FmeHelpPage, text='Exit Help', command=self.WinHelp.destroy)
            self.BtnHp9ExitHelp.config(font=('Times', 16))
            self.BtnHp9ExitHelp.grid(row=2, column=8)

            self.HelpPageContents = False






root = Tk()
root.geometry('1000x800')
my_gui = GUI(root)
root.mainloop()



